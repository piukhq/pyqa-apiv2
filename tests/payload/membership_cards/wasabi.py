import json
import logging

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils


class WasabiCard:
    @staticmethod
    def add_field_only_membership_card_payload(invalid_data=None):
        if invalid_data:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM)
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
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
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
    def add_field_only_membership_card_payload_with_existing_id(invalid_request=None):
        if invalid_request:
            payload = {}
        else:
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
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
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
    def add_field_only_membership_card_with_invalid_json():
        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": "'card_number'",
                            "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
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
    def add_and_authorise_membership_card_payload(invalid_request=None):
        TestContext.card_number = TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM)
        TestContext.email = TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.EMAIL)
        if invalid_request:
            payload = {}
        else:
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
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            }
                        ]
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
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
    def add_and_authorise_existing_membership_card_payload():
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
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "email",
                            "value": TestContext.email,
                        }
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
        }

        logging.info(
            "The Request for Add_and_Auth with existing scheme journey with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_auth_field_only_membership_card_with_invalid_json():
        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": "'card_number'",
                            "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                },
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "'email'",
                            "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.EMAIL),
                        }
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
        }

        logging.info(
            "The Request for Add_and_Auth journey with invalid json:\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def authorise_field_only_membership_card_payload(invalid_data=None):
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "'email'",
                                "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.EMAIL),
                            }
                        ]
                    },
                }
            }
        else:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.EMAIL),
                            }
                        ]
                    },
                },
            }
        logging.info(
            "The Request for Authorise field only with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
