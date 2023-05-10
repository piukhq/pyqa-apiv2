import json
import logging
from faker import Faker
from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
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
    def add_and_authorise_transactions_card_payload():
        value = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.ID)
        password = TestDataUtils.TEST_DATA.harvey_nichols_membership_card.get(constants.PASSWORD)
        payload = {
            "account": {
                "authorise_fields": {
                    "credentials": [
                        {"credential_slug": "email", "value": value},
                        {"credential_slug": "password", "value": password},
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("harvey_nichols"),
        }

        return payload
