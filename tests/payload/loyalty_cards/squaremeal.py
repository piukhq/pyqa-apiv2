import json
import logging
import uuid

from faker import Faker

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils


class SquareMealCard:
    @staticmethod
    def add_field_only_membership_card_payload(invalid_data=None):
        if invalid_data:
            payload = {}
        else:
            TestContext.card_number = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.CARD_NUM)
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
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
    def add_loyalty_card_trusted_payload(invalid_data=None):
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL)
        TestContext.email2 = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL2)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.PASSWORD)
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "email2":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email2,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.MERCHANT_ID),
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }
        elif invalid_data == "merchantid2":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.MERCHANT_ID2),
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "'email'",
                                "value": TestContext.email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.MERCHANT_ID),
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }
        else:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.MERCHANT_ID),
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }
        logging.info(
            "The Request for Add trusted loyalty card with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_TRUSTED
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    # @staticmethod
    # def add_field_only_membership_card_payload_with_existing_id(invalid_request=None):
    #     if invalid_request:
    #         payload = {}
    #     else:
    #         payload = {
    #             "account": {
    #                 "add_fields": {
    #                     "credentials": [
    #                         {
    #                             "credential_slug": "card_number",
    #                             "value": TestContext.card_number,
    #                         }
    #                     ]
    #                 }
    #             },
    #             "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
    #         }
    #     logging.info(
    #         "The Request for Add_field only with :\n"
    #         + Endpoint.BASE_URL
    #         + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
    #         + "\n\n"
    #         + json.dumps(payload, indent=4)
    #     )
    #     return payload

    # @staticmethod
    # def add_field_only_membership_card_with_invalid_json():
    #     payload = {
    #         "account": {
    #             "add_fields": {
    #                 "credentials": [
    #                     {
    #                         "credential_slug": "'card_number'",
    #                         "value": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
    #                     }
    #                 ]
    #             }
    #         },
    #         "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("wasabi"),
    #     }
    #     logging.info(
    #         "The Request for Add_field only with :\n"
    #         + Endpoint.BASE_URL
    #         + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
    #         + "\n\n"
    #         + json.dumps(payload, indent=4)
    #     )
    #     return payload

    @staticmethod
    def add_and_authorise_membership_card_payload(invalid_request=None):
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.PASSWORD)
        if invalid_request:
            payload = {}
        else:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            },
                            {
                                "credential_slug": "password",
                                "value": TestContext.password,
                            },
                        ]
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
    def add_and_authorise_transactions_card_payload(card=None):
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.TRANSACTIONS_EMAIL)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.TRANSACTIONS_PASSWORD)
        payload = {
            "account": {
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "email",
                            "value": TestContext.email,
                        },
                        {
                            "credential_slug": "password",
                            "value": TestContext.password,
                        },
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "email",
                            "value": TestContext.email,
                        },
                        {
                            "credential_slug": "password",
                            "value": TestContext.password,
                        },
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "'email'",
                            "value": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL),
                        },
                        {
                            "credential_slug": "'password'",
                            "value": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.PASSWORD),
                        },
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
    def add_and_auth_field_only_membership_card_with_unauthorised_json(card=None, request_payload=None):
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.INVALID_PASSWORD)
        payload = {
            "account": {
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "email",
                            "value": TestContext.email,
                        },
                        {
                            "credential_slug": "password",
                            "value": TestContext.password,
                        },
                    ]
                }
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
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
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.PASSWORD)
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "'email'",
                                "value": TestContext.email,
                            },
                            {
                                "credential_slug": "password",
                                "value": TestContext.password,
                            },
                        ]
                    }
                }
            }
        else:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            },
                            {
                                "credential_slug": "password",
                                "value": TestContext.password,
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
    def authorise_field_only_transactions_membership_card_payload(invalid_data=None):
        TestContext.email = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.TRANSACTIONS_EMAIL)
        TestContext.password = TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.TRANSACTIONS_PASSWORD)
        if invalid_data == "invalid_request":
            payload = {}
        elif invalid_data == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "'email'",
                                "value": TestContext.email,
                            },
                            {
                                "credential_slug": "password",
                                "value": TestContext.password,
                            },
                        ]
                    }
                }
            }
        else:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": TestContext.email,
                            },
                            {
                                "credential_slug": "password",
                                "value": TestContext.password,
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
    def add_and_authorise_with_different_auth_field():
        payload = {
            "account": {
                "authorise_fields": {
                    "credentials": [
                        {
                            "credential_slug": "email",
                            "value": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.EMAIL),
                        },
                        {
                            "credential_slug": "password",
                            "value": TestDataUtils.TEST_DATA.square_meal_membership_card.get(
                                constants.INVALID_PASSWORD
                            ),
                        },
                    ]
                },
            },
            "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
        }
        logging.info(
            "The Request for Wasabi Add_and_Auth journey with different auth value:\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def join_journey(email=None, request_payload=None, join_type=None):
        faker = Faker()
        if request_payload == "invalid_request":
            payload = {}
        elif request_payload == "invalid_json":
            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": '"first_name"', "value": faker.name()},
                            {"credential_slug": '"last_name"', "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "password", "value": "testpass"},
                        ],
                        "consents": [{"consent_slug": "Subscription", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }
        else:
            payload = {
                "account": {
                    "join_fields": {
                        "credentials": [
                            {"credential_slug": "first_name", "value": faker.name()},
                            {"credential_slug": "last_name", "value": faker.name()},
                            {"credential_slug": "email", "value": email},
                            {"credential_slug": "password", "value": "testpass"},
                        ],
                        "consents": [{"consent_slug": "Subscription", "value": constants.CONSENT}],
                    },
                },
                "loyalty_plan_id": TestDataUtils.TEST_DATA.membership_plan_id.get("square_meal"),
            }

        logging.info(
            "The Request for Join with :\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def update_trusted_add_payload(email=None, request_payload=None):
        if request_payload == "invalid_request":
            payload = {}
        elif request_payload == "invalid_json":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "'email'",
                                "value": email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(
                            constants.TRANSACTIONS_MERCHANT_ID
                        ),
                    },
                }
            }
        elif request_payload == "conflict":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(
                            constants.TRANSACTIONS_MERCHANT_ID
                        ),
                    },
                }
            }
        elif request_payload == "new_merchant_id":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": f"{uuid.uuid4()}",
                    },
                }
            }
        elif request_payload in ["successful_payload", "invalid_scheme_account_id", "invalid_token"]:
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(
                            constants.TRANSACTIONS_MERCHANT_ID
                        ),
                    },
                }
            }
        elif request_payload == "update_email":
            payload = {
                "account": {
                    "authorise_fields": {
                        "credentials": [
                            {
                                "credential_slug": "email",
                                "value": email,
                            }
                        ]
                    },
                    "merchant_fields": {
                        "account_id": TestDataUtils.TEST_DATA.square_meal_membership_card.get(constants.MERCHANT_ID),
                    },
                }
            }
        else:
            payload = {}
            logging.info("payload for" + request_payload + "is not defined:")

        logging.info("The Request for put/{id}/trusted_add is :" + "\n\n" + json.dumps(payload, indent=4))
        return payload
