import json

import requests

from tests_qa import config


class Endpoint:
    BASE_URL = ""

    @staticmethod
    def set_environment(env):
        Endpoint.BASE_URL = getattr(config, env.upper()).base_url

    @staticmethod
    def request_header(token=None, version="2.0"):
        headers = {
            "Accept": "application/vnd.bink+json;v={}".format(version),
            "Content-Type": "application/json",
        }
        headers["Authorization"] = "bearer " + token
        return headers

    @staticmethod
    def call(url, headers, method="GET", body=None):
        return requests.request(method, url, headers=headers, data=json.dumps(body))
