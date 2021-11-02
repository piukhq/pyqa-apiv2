import json
import logging

from faker import Faker

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils


class IcelandCard:
    @staticmethod
    def add_field_only_membership_card_payload(invalid_request=None):
        if invalid_request:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM)
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
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
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
    def add_field_only_membership_card_payload_with_existing_id():
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
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
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
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
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
                            "credential_slug": '"card_number"',
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                },
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "last_name",
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.LAST_NAME),
                        },
                        {
                            "credential_slug": "postcode",
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.POSTCODE),
                        },
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
        }

        logging.info(
            "The Request for Add_and_auth field only with single quote json:\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def add_and_authorise_membership_card_payload(invalid_request=None):
        TestContext.card_number = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM)
        TestContext.last_name = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.LAST_NAME)
        TestContext.postcode = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.POSTCODE)

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
                                "credential_slug": "last_name",
                                "value": TestContext.last_name,
                            },
                            {
                                "credential_slug": "postcode",
                                "value": TestContext.postcode,
                            },
                        ]
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
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
    def add_and_authorise_with_different_auth_field():
        faker = Faker()

        payload = {
            "account": {
                "add_fields": {
                    "credentials": [
                        {
                            "credential_slug": "card_number",
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
                        }
                    ]
                },
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "last_name",
                            "value": faker.name(),
                        },
                        {
                            "credential_slug": "postcode",
                            "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.POSTCODE),
                        },
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
        }

        logging.info(
            "The Request for Iceland Add_and_Auth journey with different auth value:\n"
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
                            "credential_slug": "last_name",
                            "value": TestContext.last_name,
                        },
                        {
                            "credential_slug": "postcode",
                            "value": TestContext.postcode,
                        },
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
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
    def authorise_field_only_membership_card_payload(invalid_data=None):
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": '"last_name"',
                                "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.LAST_NAME),
                            },
                            {
                                "credential_slug": '"postcode"',
                                "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.POSTCODE),
                            },
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
                                "credential_slug": "last_name",
                                "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.LAST_NAME),
                            },
                            {
                                "credential_slug": "postcode",
                                "value": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.POSTCODE),
                            },
                        ]
                    }
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

    @staticmethod
    def add_and_register_membership_card(email=None, invalid_request=None):
        faker = Faker()
        if invalid_request:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.REGISTER_CARD)
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
                            {"credential_slug": "title", "value": constants.TITLE},
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "date_of_birth", "value": constants.DATE_OF_BIRTH},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "phone", "value": faker.phone_number()},
                            {"credential_slug": "address_1", "value": faker.building_number()},
                            {"credential_slug": "address_2", "value": faker.street_address()},
                            {"credential_slug": "town_city", "value": faker.city()},
                            {"credential_slug": "county", "value": faker.country()},
                            {"credential_slug": "postcode", "value": faker.postcode()},
                        ],
                        "consents": [{"consent_slug": "marketing_opt_in", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
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
    def add_and_register_field_only_membership_card_with_invalid_json(email=None, invalid_request=None):
        faker = Faker()
        if invalid_request:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.REGISTER_CARD)
            payload = {
                "account": {
                    "add_fields": {
                        "credentials": [
                            {
                                "credential_slug": '"card_number"',
                                "value": TestContext.card_number,
                            }
                        ]
                    },
                    "register_ghost_card_fields": {
                        "credentials": [
                            {"credential_slug": "'title'", "value": constants.TITLE},
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "date_of_birth", "value": constants.DATE_OF_BIRTH},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "phone", "value": "07796511290"},
                            {"credential_slug": "address_1", "value": faker.building_number()},
                            {"credential_slug": "address_2", "value": faker.street_address()},
                            {"credential_slug": "town_city", "value": faker.city()},
                            {"credential_slug": "county", "value": faker.country()},
                            {"credential_slug": "postcode", "value": faker.postcode()},
                        ],
                        "consents": [{"consent_slug": "marketing_opt_in", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
            }

        logging.info(
            "The Request for Add_and_register with invalid request:\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

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
                            {"credential_slug": '"title"', "value": constants.TITLE},
                            {"credential_slug": '"first_name"', "value": faker.name()},
                            {"credential_slug": '"last_name"', "value": faker.name()},
                            {"credential_slug": "'date_of_birth'", "value": constants.DATE_OF_BIRTH},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "phone", "value": faker.phone_number()},
                            {"credential_slug": "address_1", "value": faker.building_number()},
                            {"credential_slug": "address_2", "value": faker.street_address()},
                            {"credential_slug": "town_city", "value": faker.city()},
                            {"credential_slug": "county", "value": faker.country()},
                            {"credential_slug": "postcode", "value": faker.postcode()},
                        ],
                        "consents": [{"consent_slug": "marketing_opt_in", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
            }
        else:
            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "title", "value": constants.TITLE},
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "date_of_birth", "value": constants.DATE_OF_BIRTH},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "phone", "value": faker.phone_number()},
                            {"credential_slug": "address_1", "value": faker.building_number()},
                            {"credential_slug": "address_2", "value": faker.street_address()},
                            {"credential_slug": "town_city", "value": faker.city()},
                            {"credential_slug": "county", "value": faker.country()},
                            {"credential_slug": "postcode", "value": faker.postcode()},
                        ],
                        "consents": [{"consent_slug": "marketing_opt_in", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("iceland"),
            }

        logging.info(
            "The Request for Join with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload
