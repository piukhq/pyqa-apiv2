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
                            {"credential_slug": '"first_name"', "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [
                            {
                                "consent_slug": "email_marketing",
                                "value": constants.CONSENT,
                            }
                        ],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
            }

        else:
            if not join_type:
                last_name = faker.name()
            else:
                if join_type == "account_already_exists":
                    last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                        constants.JOIN_REGISTER_ACCOUNT_ALREADY_EXISTS_EMAIL
                    )
                elif join_type == "join_failed":
                    last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                        constants.JOIN_REGISTER_NON_RETRYABLE_ERROR
                    )
                elif join_type == "join_http_failed":
                    last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                        constants.JOIN_REGISTER_NON_RETRYABLE_HTTP_ERROR
                    )

            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": last_name},
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [
                            {
                                "consent_slug": "email_marketing",
                                "value": constants.CONSENT,
                            }
                        ],
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
        TestContext.last_name = faker.name()
        if invalid_request:
            payload = {}
        else:
            if invalid_data == "account_already_exists":
                TestContext.last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                    constants.JOIN_REGISTER_ACCOUNT_ALREADY_EXISTS_EMAIL
                )
            elif invalid_data == "card_already_registered":
                TestContext.last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                    constants.REGISTER_ACCOUNT_EXISTS_CARDNUM
                )
            elif invalid_data == "ghost_card_registration_failed_non_retryable_http_error":
                TestContext.last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                    constants.JOIN_REGISTER_NON_RETRYABLE_HTTP_ERROR
                )
            elif invalid_data == "ghost_card_registration_failed_non_retryable_other_errors":
                TestContext.last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                    constants.JOIN_REGISTER_NON_RETRYABLE_ERROR
                )
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
                            {
                                "credential_slug": "last_name",
                                "value": TestContext.last_name,
                            },
                        ],
                        "consents": [
                            {
                                "consent_slug": "email_marketing",
                                "value": constants.CONSENT,
                            }
                        ],
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

    @staticmethod
    def add_field_before_register_membership_card_payload(invalid_request=None):
        if invalid_request:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.REGISTER_CARD)
            payload = {
                "account": {
                    "add_fields": {
                        "credentials": [
                            {
                                "credential_slug": "card_number",
                                "value": TestContext.card_number,
                            }
                        ]
                    }
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
            }

        logging.info(
            "The Request for Add_field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def register_field_only_membership_card_payload(email=None, invalid_data=None):
        faker = Faker()
        TestContext.last_name = faker.name()
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "register_ghost_card_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [
                            {
                                "consent_slug": "email_marketing",
                                "value": constants.CONSENT,
                            }
                        ],
                    }
                }
            }
        else:
            if invalid_data == "registration_failed":
                TestContext.last_name = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                    constants.JOIN_REGISTER_NON_RETRYABLE_HTTP_ERROR
                )
            payload = {
                "account": {
                    "register_ghost_card_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {
                                "credential_slug": "last_name",
                                "value": TestContext.last_name,
                            },
                            {"credential_slug": "email", "value": email},
                        ],
                        "consents": [
                            {
                                "consent_slug": "email_marketing",
                                "value": constants.CONSENT,
                            }
                        ],
                    }
                }
            }
        logging.info(
            "The Request for Register field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_authorise_transactions_card_payload(card=None):
        value = TestDataUtils.TEST_DATA.the_works_membership_card.get(constants.CARD_NUM)

        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {"credential_slug": "card_number", "value": value},
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
        }

        logging.info(
            "The Request for Add_and_Auth journey with for The_Works :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_auth_field_only_membership_card_with_unauthorised_json(membership_card=None, request_payload=None):
        if request_payload == "invalid_cardnumber" or "unauthorised":
            TestContext.card_number = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                constants.INVALID_CARD_NUMBER
            )
        elif request_payload == "unknown_cardnumber":
            TestContext.card_number = TestDataUtils.TEST_DATA.the_works_membership_card.get(
                constants.UNKNOWN_CARD_NUMBER
            )

        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": "card_number",
                            "value": TestContext.card_number,
                        },
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("the_works"),
        }
        logging.info(
            "The Request for Add_and_Auth journey with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
