import logging
import time

from json import JSONDecodeError

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_helpers import PaymentCardTestData
from tests.payload.payment_cards.payment_card import PaymentCardDetails


class PaymentCards(Endpoint):
    @staticmethod
    def add_new_payment_card(token, card_provider):
        url = PaymentCards.get_url()
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.enrol_payment_card_payload_unencrypted(card_provider)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def update_payment_card(token, card_provider, update_field= None, payment_card_id=None):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.update_payment_card_payload(card_provider, update_field)
        return Endpoint.call(url, header, "PATCH", payload)

    @staticmethod
    def update_all_payment_card(token, card_provider, payment_card_id=None):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.enrol_payment_card_payload_unencrypted(card_provider)
        return Endpoint.call(url, header, "PATCH", payload)

    @staticmethod
    def add_second_payment_card(token, card_provider):
        url = PaymentCards.get_url()
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.enrol_existing_payment_card_into_another_wallet(card_provider)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_payment_card_with_optional_field(token, card_provider):
        url = PaymentCards.get_url()
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.without_optional_field(card_provider)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_payment_card_with_mandatory_field(token, card_provider):
        url = PaymentCards.get_url()
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.without_mandatory_field(card_provider)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_existing_payment_card(token, card_provider, expiry_month, expiry_year, name_on_card, card_nickname):
        url = PaymentCards.get_url()
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.existing_payment_card_payload_unencrypted(
            card_provider, expiry_month, expiry_year, name_on_card, card_nickname
        )
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def get_payment_card(token, payment_card_id):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)

        for i in range(1, 30):
            response = Endpoint.call(url, header, "GET")
            try:
                response_json = response.json()
                if not response_json["status"] == PaymentCardTestData.get_data().get(constants.PAYMENT_CARD_STATUS):
                    time.sleep(i)
                    continue
                else:
                    break
            except (JSONDecodeError, KeyError):
                logging.info(
                    "The response text:  " + response.text + "\n The response Status Code: " + str(response.status_code)
                )
                logging.info("No response generated for end point " + url)
        return response

    @staticmethod
    def delete_payment_card(token, payment_card_id):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)
        response = Endpoint.call(url, header, "DELETE")
        return response

    @staticmethod
    def get_url(payment_card_id=None):
        if payment_card_id is None:
            return Endpoint.BASE_URL + api.ENDPOINT_PAYMENT_ACCOUNTS
        else:
            return Endpoint.BASE_URL + api.ENDPOINT_PAYMENT_ACCOUNT.format(payment_card_id)

    @staticmethod
    def empty_json(token, call, payment_card_id=None):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.empty_payload()
        return Endpoint.call(url, header, call, payload)

    @staticmethod
    def null_json(token, call, payment_card_id=None):
        url = PaymentCards.get_url(payment_card_id)
        header = Endpoint.request_header(token)
        payload = PaymentCardDetails.empty_payload()
        return Endpoint.call_payload(url, header, call, payload)
