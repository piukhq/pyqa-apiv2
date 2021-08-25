import json
import logging
import time

from json import JSONDecodeError

from pytest_bdd import parsers, scenarios, then, when
from requests.exceptions import HTTPError

import config

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import PaymentCardTestData
from tests.helpers.vault.channel_vault import create_bearer_token
from tests.requests.paymentcard_account import PaymentCards

scenarios("payment_accounts/")

"""Step definitions - Add Payment Account """


def setup_token():
    TestContext.token = create_bearer_token(
        sub=TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.USER_DETAIL), channel=config.BINK.bundle_id
    )
    return TestContext.token


def setup_second_token():
    TestContext.second_token = create_bearer_token(
        sub=TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.USER_DETAIL2), channel=config.BINK.bundle_id
    )
    return TestContext.second_token


@when('I perform POST request to add a new "<payment_card_provider>" payment card to wallet')
def add_payment_account(payment_card_provider="master"):
    setup_token()
    response = PaymentCards.add_new_payment_card(TestContext.token, payment_card_provider)
    TestContext.response_status_code = response.status_code
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
    response = PaymentCards.get_payment_card(TestContext.token, TestContext.current_payment_card_id)
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
        and response_json["status"]
        == PaymentCardTestData.get_data(payment_card_provider).get(constants.PAYMENT_CARD_STATUS)
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
    response = PaymentCards.delete_payment_card(TestContext.token, TestContext.current_payment_card_id)
    assert response.status_code == 202
    TestContext.response = response
    try:
        if response.status_code == 202:
            logging.info("Payment card is deleted successfully")
        elif response.status_code == 404:
            logging.info("Could not find this account")
    except HTTPError as network_response:
        assert network_response.response.status_code == 404 or 400, "Payment card deletion is not successful"


@then("I see a <status_code_returned> status code")
def verify_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned), "Payment_account is not successful"


@when(
    'I replace "<payment_card_provider> <expiry_month> <expiry_year> <name_on_card> <card_nickname>"'
    " into the payment card"
)
def verify_replace_value(payment_card_provider, expiry_month, expiry_year, name_on_card, card_nickname):
    response = PaymentCards.add_existing_payment_card(
        TestContext.token, payment_card_provider, expiry_month, expiry_year, name_on_card, card_nickname
    )
    response_json = response_to_json(response)
    assert (
        response.status_code == 200
        and TestContext.current_payment_card_id == response_json.get("id")
        and response_json.get("status") == "active"
    ), f"Payment card replacement '{payment_card_provider}' is not successful"
    logging.info(
        f"The response of Replacement POST/PaymentCard '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    TestContext.response_status_code = response.status_code
    return TestContext.current_payment_card_id


@then('I perform POST request to add "<payment_card_provider>" payment card to wallet')
def verify_existing_payment_account(payment_card_provider):
    response = PaymentCards.add_existing_payment_card(TestContext.token, payment_card_provider)
    response_json = response_to_json(response)
    assert response.status_code == 200 and TestContext.current_payment_card_id == response_json.get(
        "id"
    ), f"Payment card replacement '{payment_card_provider}' is not successful"
    logging.info(
        f"The response of POST/PaymentCard '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.response_json = response_json
    return TestContext.current_payment_card_id


@when("I perform POST payment_account request with empty json payload")
def verify_empty_json():
    setup_token()
    response = PaymentCards.empty_json(TestContext.token)
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of GET/PaymentCard/id is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 422, "Receiving wrong data"
    return response


@then('I verify "<error_message> <error_slug>" of payment_account response')
def verify_error_message(error_message, error_slug):
    assert TestContext.error_message == error_message and TestContext.error_slug == error_slug, "server error"


@when("I perform POST <payment_card_provider> payment_account request with wrong token")
def verify_wrong_token(payment_card_provider):
    response = PaymentCards.add_new_payment_card(
        PaymentCardTestData.get_data(payment_card_provider).get(constants.TOKEN_2), payment_card_provider
    )
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/PaymentCards with wrong token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Receiving wrong data"
    return response


@when("I perform POST <payment_card_provider> payment_account request with wrong token and bearer prefix")
def verify_wrong_token_bearer_prefix(payment_card_provider):
    response = PaymentCards.add_new_payment_card(
        PaymentCardTestData.get_data(payment_card_provider).get(constants.TOKEN_PREFIX), payment_card_provider
    )
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/PaymentCards with wrong token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Receiving wrong data"
    return response


@when(parsers.parse('I perform POST request to add a new payment card by removing "{field}" field to wallet'))
def verify_optional_field(field):
    setup_token()
    payment_card_provider = "master"
    if field == "optional":
        response = PaymentCards.add_payment_card_with_optional_field(TestContext.token, payment_card_provider)
        assert response.status_code == 201, f"Payment card addition for '{payment_card_provider}' is not successful"
    elif field == "mandatory":
        logging.info("insideMandtoryfiled")
        response = PaymentCards.add_payment_card_with_mandatory_field(TestContext.token, payment_card_provider)
        assert response.status_code == 422, f"Mandatory field required '{payment_card_provider}' "

    TestContext.response_status_code = response.status_code
    response_json = response_to_json(response)
    logging.info(
        f"The response of POST/PaymentCard without optional_filed '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.current_payment_card_id = response_json.get("id")
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")
    TestContext.response_json = response_json
    return TestContext.current_payment_card_id


@then('I perform existing payment card "<payment_card_provider>" to my another wallet')
def add_existing_payment_card_in_another_wallet(payment_card_provider):
    setup_second_token()
    response = PaymentCards.add_second_payment_card(TestContext.second_token, payment_card_provider)
    TestContext.response_status_code = response.status_code
    response_json = response_to_json(response)
    time.sleep(3)
    assert response.status_code == 200 and response_json.get("status") == PaymentCardTestData.get_data(
        payment_card_provider
    ).get(constants.PAYMENT_CARD_STATUS), f"Payment card addition for '{payment_card_provider}' is not successful"
    logging.info(
        f"The response of POST/PaymentCard '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.second_payment_card_id = response_json.get("id")
    TestContext.response_json = response_json
    return TestContext.second_payment_card_id


@then("I see an <existing_payment_card_status> status code")
def verify_status_code_for_existing_account(existing_payment_card_status):
    assert TestContext.response_status_code == int(existing_payment_card_status), "Payment_account is not successful"


@then('I perform DELETE request to delete "<payment_card_provider>" the payment card from another wallet')
def delete_payment_account_from_another_wallet(payment_card_provider):
    response = PaymentCards.delete_payment_card(TestContext.second_token, TestContext.second_payment_card_id)
    assert response.status_code == 202
    TestContext.response = response
    try:
        if response.status_code == 202:
            logging.info("Payment card is deleted successfully")
        elif response.status_code == 404:
            logging.info("Could not find this account")
    except HTTPError as network_response:
        assert network_response.response.status_code == 404 or 400, "Payment card deletion is not successful"


@then(
    'I perform existing payment card "<payment_card_provider>" to my another wallet with different '
    '"<expiry_month> <expiry_year> <name_on_card> <card_nickname>"'
)
def verify_different_detail(payment_card_provider, expiry_month, expiry_year, name_on_card, card_nickname):
    setup_second_token()
    response = PaymentCards.add_existing_payment_card(
        TestContext.second_token, payment_card_provider, expiry_month, expiry_year, name_on_card, card_nickname
    )
    response_json = response_to_json(response)
    TestContext.second_payment_card_id = response_json.get("id")
    time.sleep(4)
    assert (
        response.status_code == 200 and response_json.get("status") == "active"
    ), f"Payment card replacement '{payment_card_provider}' is not successful"
    logging.info(
        f"The response of Replacement POST/PaymentCard '{payment_card_provider}' is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    TestContext.response_status_code = response.status_code
    return TestContext.second_payment_card_id
