import json
import logging

from random import randint

from faker import Faker
from shared_config_storage.credentials.encryption import RSACipher

import config
import tests.api as api

from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_helpers import PaymentCardTestData
from tests.helpers.vault import channel_vault
from tests.helpers.vault.channel_vault import KeyType


class PaymentCardDetails:
    FIELDS_TO_ENCRYPT = ("first_six_digits", "last_four_digits", "month", "year", "hash")
    #
    # @staticmethod
    # def add_payment_card_payload_encrypted(card_provider):
    #
    #     payment_card = PaymentCardDetails.get_card(card_provider)
    #     if TestContext.channel_name == config.BINK.channel_name:
    #         pub_key = channel_vault.get_key(config.BINK.bundle_id, KeyType.PUBLIC_KEY)
    #     elif TestContext.channel_name == config.BARCLAYS.channel_name:
    #         pub_key = channel_vault.get_key(config.BARCLAYS.bundle_id, KeyType.PUBLIC_KEY)
    #     payload = PaymentCardDetails.encrypt(payment_card, pub_key)
    #     logging.info("The Request to add encrypted payment card is : \n\n"
    #                  + Endpoint.BASE_URL + api.ENDPOINT_PAYMENT_CARDS + "\n\n" + json.dumps(payload, indent=4))
    #     return payload

    @staticmethod
    def enrol_payment_card_payload_encrypted(card_provider):

        payment_card = PaymentCardDetails.enrol_payment_card_payload_unencrypted(card_provider)
        if TestContext.channel_name == config.BINK.channel_name:
            pub_key = channel_vault.get_key(config.BINK.bundle_id, KeyType.PUBLIC_KEY)
        # elif TestContext.channel_name == config.BARCLAYS.channel_name:
        #     pub_key = channel_vault.get_key(config.BARCLAYS.bundle_id, KeyType.PUBLIC_KEY)
        payload = PaymentCardDetails.encrypt(payment_card, pub_key)
        logging.info(
            "The Request to enrol encrypted new payment card is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def encrypt(payment_card, pub_key):
        for field in PaymentCardDetails.FIELDS_TO_ENCRYPT:
            cred = payment_card["card"].get(field)
            if not cred:
                raise ValueError(f"Missing credential {field}")
            try:
                encrypted_val = RSACipher().encrypt(cred, pub_key=pub_key)
            except Exception as e:
                raise ValueError(f"Value: {cred}") from e
            payment_card["card"][field] = encrypted_val

        return payment_card

    @staticmethod
    def enrol_payment_card_payload_unencrypted(card_provider):
        faker = Faker()
        TestContext.name_on_payment_card = faker.first_name()
        TestContext.card_nickname = faker.last_name()
        TestContext.expiry_month = str(randint(1, 12))
        TestContext.expiry_year = str(randint(2999, 3999))
        if TestContext.payment_status == "new":
            TestContext.payment_card_token = constants.TOKEN + "_pytest_api2_" + str(faker.random_int(100, 999999))
        elif TestContext.payment_status == "invalid_card_detail":
            TestContext.payment_card_token = "ERRADD_RCCMP009"
        elif TestContext.payment_status == "duplicate":
            TestContext.payment_card_token = "ERRADD_RCCMP005"
        elif TestContext.payment_status == "pending":
            TestContext.payment_card_token = "ERRRET_500"
        TestContext.finger_print = (constants.FINGERPRINT + "_pytest_api2_" + str(faker.random_int(100, 999999))
                                    + "_" + TestContext.card_nickname)

        payload = {
            "expiry_month": TestContext.expiry_month,
            "expiry_year": TestContext.expiry_year,
            "name_on_card": TestContext.name_on_payment_card,
            "card_nickname": TestContext.card_nickname,
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "token": TestContext.payment_card_token,
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
            "fingerprint": TestContext.finger_print,
            # "provider": PaymentCardTestData.get_data(card_provider).get(constants.PROVIDER),
            "type": PaymentCardTestData.get_data(card_provider).get(constants.TYPE),
            "country": PaymentCardTestData.get_data(card_provider).get(constants.COUNTRY),
            "currency_code": PaymentCardTestData.get_data(card_provider).get(constants.CURRENCY_CODE),
        }

        logging.info(
            "The Request to new payment card is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def enrol_existing_payment_card_into_another_wallet(card_provider):
        payload = {
            "expiry_month": TestContext.expiry_month,
            "expiry_year": TestContext.expiry_year,
            "name_on_card": TestContext.name_on_payment_card,
            "card_nickname": TestContext.card_nickname,
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "token": TestContext.payment_card_token,
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
            "fingerprint": TestContext.finger_print,
            # "provider": PaymentCardTestData.get_data(card_provider).get(constants.PROVIDER),
            "type": PaymentCardTestData.get_data(card_provider).get(constants.TYPE),
            "country": PaymentCardTestData.get_data(card_provider).get(constants.COUNTRY),
            "currency_code": PaymentCardTestData.get_data(card_provider).get(constants.CURRENCY_CODE),
        }

        logging.info(
            "The Request to enrol new payment card is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def existing_payment_card_payload_unencrypted(
        card_provider, expiry_month, expiry_year, name_on_card, card_nickname
    ):
        payload = {
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "name_on_card": name_on_card,
            "card_nickname": card_nickname,
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "token": TestContext.payment_card_token,
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
            "fingerprint": TestContext.finger_print,
            # "provider": PaymentCardTestData.get_data(card_provider).get(constants.PROVIDER),
            "type": PaymentCardTestData.get_data(card_provider).get(constants.TYPE),
            "country": PaymentCardTestData.get_data(card_provider).get(constants.COUNTRY),
            "currency_code": PaymentCardTestData.get_data(card_provider).get(constants.CURRENCY_CODE),
        }

        logging.info(
            "The Request to existing payment card is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def payment_card_with_empty_field(card_provider):
        payload = {
            "expiry_month": "",
            "expiry_year": "",
            "name_on_card": "QA_empty_string_name01",
            "card_nickname": "QA_empty_string_nickname01",
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "token": "",
            "last_four_digits": "",
            "first_six_digits": "",
            "fingerprint": "",
            # "provider": PaymentCardTestData.get_data(card_provider).get(constants.PROVIDER),
            "type": PaymentCardTestData.get_data(card_provider).get(constants.TYPE),
            "country": PaymentCardTestData.get_data(card_provider).get(constants.COUNTRY),
            "currency_code": PaymentCardTestData.get_data(card_provider).get(constants.CURRENCY_CODE),
        }

        logging.info(
            "The Request to payment card with empty string is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def empty_payload():
        payload = {}
        return payload

    @staticmethod
    def without_optional_field(card_provider):
        faker = Faker()

        payload = {
            "expiry_month": str(randint(1, 12)),
            "expiry_year": str(randint(2999, 3999)),
            "token": constants.TOKEN + "_pytest" + str(faker.random_int(100, 999999)),
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
            "fingerprint": constants.FINGERPRINT + "_pytest" + str(faker.random_int(100, 999999)),
        }

        logging.info(
            "The Request to enrol new payment card without optional field is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def without_mandatory_field(card_provider):
        faker = Faker()
        payload = {
            "name_on_card": faker.first_name(),
            "card_nickname": faker.last_name(),
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
        }
        logging.info(
            "The Request to enrol new payment card without mandatory field is : \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_PAYMENT_ACCOUNTS
            + "\n\n"
            + json.dumps(payload, indent=4)
        )
        return payload

    @staticmethod
    def update_payment_card_payload(card_provider, update_field):
        faker = Faker()
        if update_field == "expiry_month":
            TestContext.expiry_month = str(randint(1, 12))
            payload = {
                "expiry_month": TestContext.expiry_month,
            }
        elif update_field == "expiry_year":
            logging.info(update_field)
            TestContext.expiry_year = str(randint(2999, 3999))
            payload = {
                "expiry_year": TestContext.expiry_year,
            }
            logging.info(payload)

        elif update_field == "name_on_card":
            TestContext.name_on_payment_card = faker.first_name()
            payload = {
                "name_on_card": TestContext.name_on_payment_card,
            }
        elif update_field == "card_nickname":
            TestContext.card_nickname = faker.last_name()
            payload = {
                "card_nickname": TestContext.card_nickname,
            }
        elif update_field == "issuer":
            payload = {
                "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER_UPDATED),
            }
        else:
            TestContext.name_on_payment_card = faker.first_name()
            TestContext.card_nickname = faker.last_name()
            TestContext.expiry_month = str(randint(1, 12))
            TestContext.expiry_year = str(randint(2999, 3999))
            TestContext.payment_card_token = constants.TOKEN + "_pytest_api2_" + str(faker.random_int(100, 999999))
            TestContext.finger_print = constants.FINGERPRINT + "_pytest_api2_" + str(faker.random_int(100, 999999))

            payload = {
                "expiry_month": TestContext.expiry_month,
                "expiry_year": TestContext.expiry_year,
                "name_on_card": TestContext.name_on_payment_card,
                "card_nickname": TestContext.card_nickname,
                "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            }
            logging.info(
                "The New Request to update expiry_month, expiry_year, name_on_card, card_nickname, issuer to "
                "existing payment card is : \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_PAYMENT_ACCOUNTS
                + "\n\n"
                + json.dumps(payload, indent=4)
            )
        return payload
