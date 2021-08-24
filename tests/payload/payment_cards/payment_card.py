import json
import logging

from random import randint

import tests_qa.tests.api as api

from faker import Faker
from shared_config_storage.credentials.encryption import RSACipher
from tests_qa import config
from tests_qa.tests.api.base import Endpoint
from tests_qa.tests.helpers import constants
from tests_qa.tests.helpers.test_context import TestContext
from tests_qa.tests.helpers.test_helpers import PaymentCardTestData
from tests_qa.tests.helpers.vault import channel_vault
from tests_qa.tests.helpers.vault.channel_vault import KeyType


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
            + api.ENDPOINT_PAYMENT_CARDS
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
        TestContext.expiry_month = str(randint(1, 24))
        TestContext.expiry_year = str(randint(1, 12))

        payload = {
            "expiry_month": TestContext.expiry_month,
            "expiry_year": TestContext.expiry_year,
            "name_on_card": TestContext.name_on_payment_card,
            "card_nickname": TestContext.card_nickname,
            "issuer": PaymentCardTestData.get_data(card_provider).get(constants.ISSUER),
            "token": constants.TOKEN + "_pytest" + str(faker.random_int(100, 999999)),
            "last_four_digits": PaymentCardTestData.get_data(card_provider).get(constants.LAST_FOUR_DIGITS),
            "first_six_digits": PaymentCardTestData.get_data(card_provider).get(constants.FIRST_SIX_DIGITS),
            "fingerprint": constants.FINGERPRINT + "_pytest" + str(faker.random_int(100, 999999)),
            "provider": PaymentCardTestData.get_data(card_provider).get(constants.PROVIDER),
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
