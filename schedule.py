import os
import random
import string
import subprocess

from datetime import datetime

import requests

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from azure.storage.blob import BlobClient, ContentSettings

name = os.getenv("FRIENDLY_NAME")
blob_storage_dsn = os.getenv("BLOB_STORAGE_DSN")
teams_webhook = os.getenv("TEAMS_WEBHOOK")
schedule = os.getenv("SCHEDULE")
command = os.getenv("COMMAND")
alert_on_success = os.getenv("ALERT_ON_SUCCESS", True)
alert_on_failure = os.getenv("ALERT_ON_FAILURE", True)


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
    scheduler = BlockingScheduler()
    scheduler.add_job(run_test, trigger=CronTrigger.from_crontab(schedule))
    scheduler.start()


if __name__ == "__main__":
    main()
