import json
import logging
import random

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils


class IcelandCard:
    @staticmethod
    def add_field_only_membership_card_payload(invalid_request=None):
        if invalid_request:
            payload = {}
        else:
            payload = {
                "account": {
                    "add_fields": {
                        "credentials": [
                            {
                                "credential_slug": "card_number",
                                "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM)
                                + str(random.randint(10, 999999)),
                            }
                        ]
                    }
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
            }

        logging.info(
            "The Request for Add_field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_field_only_membership_card_payload_with_existing_id():
        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": "card_number",
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
        }

        logging.info(
            "The Request for Add_field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_field_only_membership_card_with_invalid_json():
        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": '"card_number"',
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
        }

        logging.info(
            "The Request for Add_field only with single quote:\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload