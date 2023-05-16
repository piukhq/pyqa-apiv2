import json
import logging

from faker import Faker

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils


class TheWorks:
    @staticmethod
    def join_journey(email=None, request_payload=None, join_type=None):
        faker = Faker()
        last_name = faker.name()
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
            if not join_type:
                last_name = faker.name()
            else:
                if join_type == "account_already_exists":
                    last_name = TestDataUtils.TEST_DATA.the_works.get(constants.JOIN_ACCOUNT_ALREADY_EXIST)
                elif join_type == "join_failed":
                    last_name = TestDataUtils.TEST_DATA.the_works.get(constants.JOIN_FAILED)
                elif join_type == "join_http_failed":
                    last_name = TestDataUtils.TEST_DATA.the_works.get(constants.FAILHTTP_ERROR)

            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": last_name},
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
