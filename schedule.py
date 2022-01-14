import os
import random
import string
import subprocess
import time

from datetime import datetime

import requests

# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.triggers.cron import CronTrigger
from azure.storage.blob import BlobClient, ContentSettings

from kubernetes import client, config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream

name = os.getenv("FRIENDLY_NAME")
blob_storage_dsn = os.getenv("BLOB_STORAGE_DSN")
teams_webhook = os.getenv("TEAMS_WEBHOOK")
schedule = os.getenv("SCHEDULE")
command = os.getenv("COMMAND")
alert_on_success = os.getenv("ALERT_ON_SUCCESS", True)
alert_on_failure = os.getenv("ALERT_ON_FAILURE", True)


def exec_commands(api_instance, name):
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name, namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)

    if not resp:
        print("Pod %s does not exist. Creating it..." % name)
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'image': 'busybox',
                    'name': 'sleep',
                    "args": [
                        "/bin/sh",
                        "-c",
                        "while true;do date;sleep 5; done"
                    ]
                }]
            }
        }
        resp = api_instance.create_namespaced_pod(body=pod_manifest,
                                                  namespace='default')
        while True:
            resp = api_instance.read_namespaced_pod(name=name,
                                                    namespace='default')
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)
        print("Done.")

        # Calling exec and waiting for response
    exec_command = [
        'pytest',
        '-m',
        'bink_regression_api21',
        '--channel',
        'bink',
        '--env'
        'staging']
    resp = stream(api_instance.connect_get_namespaced_pod_exec,
                  name,
                  'default',
                  command=exec_command,
                  stderr=True, stdin=False,
                  stdout=True, tty=False)
    print("Response: " + resp)

    # # Calling exec interactively
    # exec_command = ['/bin/sh']
    # resp = stream(api_instance.connect_get_namespaced_pod_exec,
    #               name,
    #               'default',
    #               command=exec_command,
    #               stderr=True, stdin=True,
    #               stdout=True, tty=False,
    #               _preload_content=False)
    # # commands = [
    # #     "echo This message goes to stdout",
    # #     "echo \"This message goes to stderr\" >&2",
    # # ]
    #
    # while resp.is_open():
    #     resp.update(timeout=1)
    #     if resp.peek_stdout():
    #         print("STDOUT: %s" % resp.read_stdout())
    #     if resp.peek_stderr():
    #         print("STDERR: %s" % resp.read_stderr())
    #     if commands:
    #         c = commands.pop(0)
    #         print("Running command... %s\n" % c)
    #         resp.write_stdin(c + "\n")
    #     else:
    #         break

    # resp.write_stdin("date\n")
    # sdate = resp.readline_stdout(timeout=3)
    # print("Server date command returns: %s" % sdate)
    # resp.write_stdin("whoami\n")
    # user = resp.readline_stdout(timeout=3)
    # print("Server user is: %s" % user)
    resp.close()


def run_test():
    try:
        process = subprocess.run(command.split(" "), timeout=7200, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.TimeoutExpired:
        print("Timeout occurred, skipping run")
        return
    print(process.stdout.decode())
    alert = False
    if process.returncode == 0:
        print("SCHEDULER - run success")
        status = "Success"
        if alert_on_success:
            alert = True
    else:
        print("SCHEDULER - run failed")
        status = "Failure"
        if alert_on_failure:
            alert = True
    url = upload("report.html")
    if alert:
        print("SCHEDULER - sending teams notification")
        resp = post(teams_webhook, status, url)
        if resp.status_code > 299:
            print(f"SCHEDULER - teams webhook failed {resp.body}")


def upload(filename):
    try:
        suffix = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
        blob = BlobClient.from_connection_string(
            conn_str=blob_storage_dsn,
            container_name="qareports",
            blob_name=f"pytest_report/apiv2-{datetime.now().strftime('%Y%m%d-%H%M')}-{suffix}.html",
        )
        with open(filename, "rb") as f:
            blob.upload_blob(f, content_settings=ContentSettings(content_type="text/html"))
        return blob.url
    except Exception as err:
        print(f"SCHEDULER - failed to upload {err}")
        raise


def post(webhook, status, url):
    if status == "Success":
        themeColor = "00FF00"
    else:
        themeColor = "FF0000"
    template = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "themeColor": themeColor,
        "summary": f"{name} Test Results",
        "Sections": [
            {
                "activityTitle": f"{name} Test Results",
                "facts": [
                    {"name": "Status", "value": status},
                    {"name": "URL", "value": f"[{url}]({url})"},
                ],
                "markdown": True,
            }
        ],
    }
    return requests.post(webhook, json=template)


def main():
    # scheduler = BlockingScheduler()
    # scheduler.add_job(run_test, trigger=CronTrigger.from_crontab(schedule))
    # scheduler.start()
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        pod_name = i.metadata.name
        if pod_name.startswith("hermes-api-"):
            return pod_name

    try:
        c = Configuration().get_default_copy()
    except AttributeError:
        c = Configuration()
        c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    exec_commands(core_v1, pod_name)


if __name__ == "__main__":
    main()
