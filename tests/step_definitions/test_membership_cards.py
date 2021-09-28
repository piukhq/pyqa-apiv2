import json
import logging

from pytest_bdd import parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.conftest import response_to_json, setup_token
from tests.helpers import constants
from tests.helpers.database.query_hermes import QueryHermes
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import TestData
from tests.requests.membership_cards import MembershipCards

scenarios("membership_cards/")

"""Step definitions - Add_field Journey (store card only) """


@when('I perform POST request to add "<merchant>" membership card')
def add_field_loyalty_cards(merchant):
    setup_token()
    response = MembershipCards.add_field_only_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add field Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 201, "Add Journey for " + merchant + " failed"


@when(parsers.parse('I perform GET request to verify the "{merchant}" membership card is added to the wallet'))
def verify_get_add_field_membership_cards(merchant):
    response = MembershipCards.get_add_field_only_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    logging.info(
        "The response of GET field Journey (GET) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@then('verify the data stored in DB after "<journey_type>" journey for "<merchant>"')
def verify_loyalty_card_into_database(journey_type, merchant):

    if journey_type == "Add_field":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.WALLET_ONLY)
            and scheme_account.scheme_id == TestData.get_membership_plan_id(merchant)
        )

    elif journey_type == "add_and_authorise":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id, "Database error"
    # logging.info(f"The scheme account is Active with status '{scheme_account.status}'")
    return scheme_account


@when('I perform POST request again to verify the "<merchant>" membership card is already added with "<status_code>"')
def verify_memebrship_card_added_already(merchant, status_code):
    response = MembershipCards.add_field_with_existing_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    logging.info(
        "The response of Add existing memebrship card (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 200, "Add existing membership card for " + merchant + " failed"


@when('I perform POST request to add "<merchant>" membership card with "<request_payload>" with "<status_code>"')
def verify_invalid_request_for_add_journey(merchant, request_payload, status_code):
    setup_token()
    if request_payload == "invalid_request":
        response = MembershipCards.add_field_only_card(TestContext.token, merchant, request_payload)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
    elif request_payload == "invalid_json":
        response = MembershipCards.add_field_with_invalid_json(TestContext.token, merchant)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]

    logging.info(
        "The response of Invalid json Journey (POST) for Add field:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    assert TestContext.response_status_code == int(status_code), "Invalid json request for " + merchant + " failed"


@when(
    'I perform POST request to add and auth "<merchant>" membership card with "<request_payload>" '
    'with "<status_code>"'
)
def verify_invalid_request_for_add_and_auth_journey(merchant, request_payload, status_code):
    setup_token()
    if request_payload == "invalid_request":
        response = MembershipCards.add_and_authorise_card(TestContext.token, merchant, request_payload)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
    elif request_payload == "invalid_json":
        response = MembershipCards.add_and_auth_field_with_invalid_json(TestContext.token, merchant)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]

    logging.info(
        "The response of Invalid Journey (POST) for Add and Auth field:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    assert TestContext.response_status_code == int(status_code), "Invalid json request for " + merchant + " failed"


@then('I see a "<error_message>" error message')
def verify_error_message(error_message):
    assert TestContext.error_message == error_message, "Error Message didnt returned"


@then('I see a "<error_slug>" error slug')
def verify_error_slug(error_slug):
    assert TestContext.error_slug == error_slug, "Error Slug didnt returned"


@when("I perform POST <merchant> membership_card request with invalid token and bearer prefix")
def verify_invalid_token_bearer_prefix_for_membership_card(merchant):
    response = MembershipCards.add_field_only_card(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), merchant
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/Memebrship_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@then("I see a <status_code_returned>")
def verify_memebrship_card_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned)


@when('I perform POST request to add and authorise "<merchant>" membership card')
def verify_add_and_auth(merchant):
    setup_token()
    response = MembershipCards.add_and_authorise_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add and Authorise Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Add and authorise Journey for " + merchant + " failed"


@when(
    'I perform POST request again with add and authorise to verify the "<merchant>" membership card is already '
    'added with "<status_code_returned>"'
)
def verify_add_and_auth_existing_membership_card(merchant, status_code_returned):
    response = MembershipCards.add_and_authorise_card_with_existing_scheme(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add and Authorise existing scheme Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == int(status_code_returned), (
        "Add and authorise with existing Journey for " + merchant + " failed"
    )


@when("I perform POST <merchant> membership_card request for add and auth with invalid token and bearer prefix")
def verify_add_and_auth_invalid_token_request(merchant):
    response = MembershipCards.add_and_authorise_card(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), merchant
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/Memebrship_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response
