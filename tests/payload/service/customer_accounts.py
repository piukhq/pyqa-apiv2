import json
import logging

from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils
from tests import api
from tests.api.base import Endpoint


class UserDetails:
    @staticmethod
    def bink_login_user_payload(client_id, bundle_id):
        """Login for Bink user"""
        payload = {
            "email": TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.UID),
            "password": TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.PWD),
            "client_id": client_id,
            "bundle_id": bundle_id,
        }
        logging.info("Request body for POST Login" + json.dumps(payload, indent=4))
        return payload

    @staticmethod
    def bink_user_email_update(test_email):
        payload = {
            "email": test_email
        }

        logging.info("Request body for POST email update : \n" + json.dumps(payload, indent=4))

        return payload

    @staticmethod
    def bink_user_email_update_invalid_data(test_email, invalid_data=None):
        if invalid_data == "invalid_request":
            payload = {"email2": test_email}
        elif invalid_data == "invalid_json":
            payload = ""
        else:
            payload = {
                "email": test_email
            }

        logging.info(
            "The Request for email update with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_EMAIL_UPDATE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

