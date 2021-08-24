import json
import logging
import time
from json import JSONDecodeError

from pytest_bdd import scenarios, then, when
from requests.exceptions import HTTPError

from tests_qa.tests import api
from tests_qa.tests.api.base import Endpoint
from tests_qa.tests.helpers import constants
from tests_qa.tests.helpers.test_context import TestContext
from tests_qa.tests.helpers.test_helpers import PaymentCardTestData
from tests_qa.tests.requests.paymentcard_account import PaymentCards

scenarios("payment_accounts/")

"""Step definitions - Add Payment Account """


@when('I perform POST request to add a new "<payment_card_provider>" payment card to wallet')
def add_payment_account(payment_card_provider="master"):
    response = PaymentCards.add_new_payment_card(
        PaymentCardTestData.get_data(payment_card_provider).get(constants.TOKEN_2), payment_card_provider
    )
    assert response.status_code == 201, f"Payment card addition for '{payment_card_provider}' is not successful"
    response_json = response_to_json(response)
    logging.info(
        f"The response of POST/PaymentCard '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.current_payment_card_id = response_json.get("id")
    TestContext.response_json = response_json
    return TestContext.current_payment_card_id


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json


@when(
    'I perform the GET request to verify the new payment card "<payment_card_provider>" has been '
    "added successfully to the wallet"
)
def verify_get_payment_account_added(payment_card_provider="master"):
    response = PaymentCards.get_payment_card(
        PaymentCardTestData.get_data(payment_card_provider).get(constants.TOKEN_2), TestContext.current_payment_card_id
    )
    response_json = response.json()
    logging.info(
        "The response of GET/PaymentCard/id is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert (
        response.status_code == 200
        and response_json["id"] == TestContext.current_payment_card_id
        and response_json["status"] == PaymentCardTestData.get_data().get(constants.PAYMENT_CARD_STATUS)
    ), "Payment card addition is not successful"
    return response


@then('I verify the paymentcard "<payment_card_provider>" been added into my wallet')
def verify_payment_account_added_in_wallet(payment_card_provider):
    logging.info(TestContext.response_json)
    assert (
        TestContext.current_payment_card_id == TestContext.response_json.get("id")
        and TestContext.name_on_payment_card == TestContext.response_json.get("name_on_card")
        and TestContext.card_nickname == TestContext.response_json.get("card_nickname")
        and PaymentCardTestData.get_data(payment_card_provider).get(constants.ISSUER)
        == TestContext.response_json.get("issuer")
        and TestContext.expiry_month == TestContext.response_json.get("expiry_month")
        and TestContext.expiry_year == TestContext.response_json.get("expiry_year")
    )


@then('I perform DELETE request to delete "<payment_card_provider>" the payment card')
def delete_payment_card(payment_card_provider):
    response = PaymentCards.delete_payment_card(
        PaymentCardTestData.get_data(payment_card_provider).get(constants.TOKEN_2), TestContext.current_payment_card_id
    )
    TestContext.response = response
    logging.info(TestContext.response)
    time.sleep(2)

    try:
        if response.status_code == 200:
            logging.info("Payment card is deleted successfully")
        elif response.status_code == 404:
            logging.info("Payment card is already  deleted")

    except HTTPError as network_response:

        assert network_response.response.status_code == 404 or 400, "Payment card deletion is not successful"
