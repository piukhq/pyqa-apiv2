import json
import logging

from shared_config_storage.credentials.encryption import RSACipher

import config

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.vault import channel_vault
from tests.helpers.vault.channel_vault import KeyType


class HarveyNicholsCard:
    @staticmethod
    def add_field_only_membership_card_payload(invalid_data=None):
        if invalid_data:
            value = TestDataUtils.TEST_DATA.harvey_nichols_invalid_data.get(constants.ID)
            logging.info("Invalid data is: " + value)
        else:
            value = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.ID)

        sensitive_value = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.PASSWORD)

        if TestContext.flag_encrypt == "true":
            if TestContext.channel_name == config.BINK.channel_name:
                pub_key = channel_vault.get_key(config.BINK.bundle_id, KeyType.PUBLIC_KEY)

            password = RSACipher().encrypt(sensitive_value, pub_key)

        elif TestContext.flag_encrypt == "false":
            password = sensitive_value

        payload = {
            "account": {
                "authorise_fields": [{"column": "Email", "value": value}, {"column": "Password", "value": password}]
            },
            "membership_plan": TestDataUtils.TEST_DATA.membership_plan_id.get("harvey_nichols"),
        }
        logging.info(
            "The Request for Add_field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    # @staticmethod
    # def authorise_field_only_membership_card_payload(invalid_data=None):
    #     if invalid_data:
    #         value = TestDataUtils.TEST_DATA.harvey_nichols_invalid_data.get(constants.ID)
    #         logging.info("Invalid data is: " + value)
    #     else:
    #         value = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.ID)
    #         password = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.PASSWORD)
    #
    #     payload = {
    #         "account": {
    #             "authorise_fields": [{"column": "Email", "value": value}, {"column": "Password", "value": password}]
    #         },
    #         "membership_plan": TestDataUtils.TEST_DATA.membership_plan_id.get("harvey_nichols"),
    #     }
    #     logging.info(
    #         "The Request for Authorise field only with :\n"
    #         + Endpoint.BASE_URL
    #         + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE
    #         + "\n\n"
    #         + json.dumps(payload, indent=4)
    #     )
    #     return payload
