import json
import logging

from faker import Faker

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils


class Itsu:
    @staticmethod
    def add_and_authorise_transactions_card_payload(card_type=None):
        card_num = TestDataUtils.TEST_DATA.itsu_membership_card.get(constants.CARD_NUM)

        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {"credential_slug": "card_number", "value": card_num},
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("itsu"),
        }

        logging.info(
            "The Request for Add_and_Auth journey with for itsu :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_auth_field_only_membership_card_with_unauthorised_json(membership_card=None, request_payload=None):
        if request_payload == "invalid_cardnumber" or "unauthorised":
            TestContext.card_number = TestDataUtils.TEST_DATA.itsu_membership_card.get(constants.INVALID_CARD_NUMBER)
        elif request_payload == "unknown_cardnumber":
            TestContext.card_number = TestDataUtils.TEST_DATA.itsu_membership_card.get(constants.UNKNOWN_CARD_NUMBER)

        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {"credential_slug": "card_number", "value": TestContext.card_number},
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("itsu"),
        }
        logging.info(
            "The Request for Add_and_Auth journey with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def join_journey(email=None, request_payload=None, join_type=None):
        faker = Faker()
        last_name = faker.name()
        if request_payload == "invalid_request":
            payload = {}
        if not join_type:
            last_name = faker.name()
        else:
            """Add itsu Join error journies when data is set up in API reflector"""
        payload = {
            "account": {
                "join_fields": {
                    "credentials": [
                        {"credential_slug": "first_name", "value": faker.name()},
                        {"credential_slug": "last_name", "value": last_name},
                        {"credential_slug": "email", "value": email},
                        {"credential_slug": "password", "value": "Loyalty102"},
                    ],
                    "consents": [{"consent_slug": "hasAgreedToReceiveMarketing", "value": constants.CONSENT}],
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("itsu"),
        }

        logging.info(
            "The Request for Join journey is :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
