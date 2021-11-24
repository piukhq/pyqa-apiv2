import json
import logging

import tests.api as api

from tests.api.base import Endpoint


class TokenB2BDetail:
    @staticmethod
    def post_b2btoken_with_grantype(grand_type, scope):
        token_response = TokenB2BDetail.postb2btoken(grand_type, scope)
        return token_response

    @staticmethod
    def postb2btoken(grand_type, scope):
        payload = {
            "grant_type": grand_type,
            "scope": [scope],
        }

        logging.info(
            "The Request to new Access Token is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_TOKEN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def token_with_invalid_json():
        payload = {
            "grant_type": "'b2b'",
            "scope": ["'user'"],
        }

        logging.info(
            "The Request for token invalid json is :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_TOKEN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def unsupported_grant_type():
        payload = {
            "grant_type": "b2bc",
            "scope": ["user"],
        }

        logging.info(
            "The Request for token unsupported grant type is :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_TOKEN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
