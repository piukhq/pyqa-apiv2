import json
import logging
import time

from pytest_bdd import parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.conftest import response_to_json
from tests.helpers import constants
from tests.helpers.database.query_hermes import QueryHermes
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import TestData
from tests.requests.membership_cards import MembershipCards
from tests.step_definitions import test_paymentcard_account

scenarios("membership_cards/")

"""Step definitions - Add_field Journey (store card only) """


@when('I perform POST request to add "<merchant>" membership card')
def add_field_loyalty_cards(merchant):
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
    time.sleep(4)

    if journey_type == "Add_field":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.WALLET_ONLY)
            and scheme_account.scheme_id == TestData.get_membership_plan_id(merchant)
        )
    elif journey_type == "add_and_authorise":

        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id, "add_authorise in database is not success"

    elif journey_type == "delete":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id and scheme_account.is_delete_scheme is True
        ), "Delete in database is not success"

    elif journey_type == "authorise_field":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.ACTIVE)
        ), "Authorise in database is not success"

    elif journey_type == "add_field_then_add_auth":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.WALLET_ONLY)
        )

    elif journey_type == "pll":
        pll_links = [{"id": TestContext.current_payment_card_id, "active_link": True}]
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id and scheme_account.pll_links == pll_links
    return scheme_account


@when('I perform POST request again to verify the "<merchant>" membership card is already added with "<status_code>"')
def verify_membership_card_added_already(merchant, status_code):
    response = MembershipCards.add_field_with_existing_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    logging.info(
        "The response of Add existing Membership card (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 200, "Add existing membership card for " + merchant + " failed"


@when('I perform POST request to add "<merchant>" membership card with "<request_payload>" with "<status_code>"')
def verify_invalid_request_for_add_journey(merchant, request_payload, status_code):
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
        "The response of POST/Membership_card with invalid token is: \n\n"
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
def verify_membership_card_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned)


@when('I perform POST request to add and authorise "<merchant>" membership card')
def verify_add_and_auth(merchant):
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
    time.sleep(3)
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
        "The response of POST/Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when('I perform POST request to authorise "<merchant>" above wallet only membership card')
def verify_authorise_post_membership_card(merchant):
    time.sleep(2)
    response = MembershipCards.authorise_field_only_card(
        TestContext.token, merchant, TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Authorise field Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Authorised Journey for " + merchant + " failed"


@when(
    "I perform POST <merchant> membership_card request with invalid token and bearer prefix for"
    " authorise membership card"
)
def verify_invalid_token_bearer_prefix_for_authorise_membership_card(merchant):
    response = MembershipCards.authorise_field_only_card(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN),
        merchant,
        TestContext.current_scheme_account_id,
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/Authorise Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when('I perform POST request to authorise "<merchant>" membership card with "<request_payload>" with "<status_code>"')
def verify_authorise_invalid_request(merchant, request_payload, status_code):
    if request_payload == "invalid_request":
        response = MembershipCards.authorise_field_only_card(
            TestContext.token, merchant, TestContext.current_scheme_account_id, request_payload
        )
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        logging.info(
            "The response of Invalid request Journey (POST) for Authorise field:\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )

    elif request_payload == "invalid_json":
        response = MembershipCards.authorise_field_with_existing_field(
            TestContext.token, merchant, TestContext.current_scheme_account_id, request_payload
        )
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]

        logging.info(
            "The response of Invalid json Journey (POST) for Authorise field:\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )

    assert TestContext.response_status_code == int(status_code), "Invalid json request for " + merchant + " failed"


@then('I perform DELETE request to delete the "<merchant>" membership card with invalid token')
def verify_delete_invalid_token(merchant):
    response = MembershipCards.delete_scheme_account(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), TestContext.current_scheme_account_id
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of DELETE/Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@then('I perform DELETE request with payload for "<merchant>"')
def verify_delete_request_with_payload(merchant):
    response = MembershipCards.delete_membership_card_with_payload(
        TestContext.token, merchant, TestContext.current_scheme_account_id
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of DELETE/Membership_card with request payload is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 422, "Server error"
    return response


@when("I perform DELETE request to delete the membership card which is already deleted")
def i_perform_delete_request_to_delete_the_mebership_card_which_is_deleted():
    time.sleep(2)

    response = MembershipCards.delete_scheme_account(TestContext.token, TestContext.current_scheme_account_id)
    TestContext.response_status_code = response.status_code
    response_json = response_to_json(response)
    logging.info(
        "The response of DELETE/Membership_card with Already Deleted membership card is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_PAYMENT_ACCOUNTS.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 404, "Server error"
    return response


@when('I perform POST request to authorise "<merchant>" above wallet only membership card again')
def verify_i_perform_authorise_again(merchant):
    time.sleep(3)
    response = MembershipCards.authorise_field_only_card(
        TestContext.token, merchant, TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Authorise field send again is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 200, "Authorised Journey for " + merchant + " failed"


@when(
    'I perform POST request to add and authorise "<merchant>" membership card which already exist with add credentail'
)
def i_perform_post_add_and_authorise_membership_card_which_is_exist_already(merchant):
    response = MembershipCards.add_and_authorise_card(TestContext.token, merchant)
    response_json = response_to_json(response)
    # TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add and Authorise Journey (POST) which is already added with add credential:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json["error_message"]
    TestContext.error_slug = response_json["error_slug"]

    assert response.status_code == 409, "Add only then add and authorise Journey for " + merchant + " failed"


@when('I perform POST request to add and register "<merchant>" membership card')
def add_and_register_field(merchant, test_email):
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
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


@when('I perform POST request to add and authorise "<merchant>" with different auth credential')
def i_perform_post_with_different_credential(merchant):
    time.sleep(4)
    response = MembershipCards.add_and_authorise_card_with_different_credential(TestContext.token, merchant)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add and Authorise Journey (POST) which is already added with add credential:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json["error_message"]
    TestContext.error_slug = response_json["error_slug"]

    assert response.status_code == 409, "Add only then add and authorise Journey for " + merchant + " failed"


@when('I perform POST request to add a new "<payment_card_provider>" payment account to wallet')
def verify_pll_authorise(payment_card_provider):
    test_paymentcard_account.add_payment_account(payment_card_provider)
