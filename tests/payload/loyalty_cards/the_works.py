import json
import logging

from faker import Faker

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils


class TheWorks:
    @staticmethod
    def join_journey(email=None, request_payload=None):
        faker = Faker()
        if request_payload == "invalid_request":
            payload = {}
        elif request_payload == "invalid_json":
            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [{"consent_slug": "email_marketing", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
            }

        else:
            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [{"consent_slug": "email_marketing", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
            }

        logging.info(
            "The Request for Join journey is :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_register_membership_card(email=None, invalid_request=None, invalid_data=None):
        faker = Faker()
        TestContext.card_number = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.REGISTER_CARD)

        if invalid_request:
            payload = {}
        else:
            if invalid_data == "account_already_exists":
                last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.REGISTER_ACCOUNT_ALREADY_EXISTS)
            elif invalid_data == "card_already_registered":
                last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.REGISTER_CARD_ALREADY_REGISTERED)
            elif invalid_data == "invalid_card_num":
                last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.REGISTER_INVALID_CARD_NUMBER)

            payload = {
                "account": {
                    "add_fields": {
                        "credentials": [
                            {
                                "credential_slug": "card_number",
                                "value": TestContext.card_number,
                            }
                        ]
                    },
                    "register_ghost_card_fields": {
                        "credentials": [
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": last_name},
                        ],
                        "consents": [{"consent_slug": "email_marketing", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
            }

        logging.info(
            "The Request for Add_and_register with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
