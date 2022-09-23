import json
import logging

from pytest_bdd import parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.conftest import response_to_json
from tests.helpers.test_context import TestContext
from tests.requests.token_b2b import Token_b2b
from tests.step_definitions import test_loyalty_cards

scenarios("b2b_token/")

"""Step definitions - /token """


@when(parsers.parse('I perform POST request to add "{merchant}" membership card'))
def add_membership_card_field(merchant):
    test_loyalty_cards.add_field_loyalty_cards(merchant)


@when(parsers.parse('I perform POST refresh token with grant type "{grant_type}"'))
def get_refresh_token(grant_type):
    TestContext.refresh_token_type = "bearer" + " " + TestContext.refresh_token_type
    response = Token_b2b.post_b2b_with_grant_type(TestContext.refresh_token_type, token_type=grant_type)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of refresh B2B token (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 200, "/token Journey failed to get access token"


@when(parsers.parse('I perform POST request for token with "{request_payload}"'))
def verify_invalid_request_for_token(request_payload):
    if request_payload == "unsupported_grant_type":
        response = Token_b2b.unsupported_grant_type(TestContext.token)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json.get("error")
    elif request_payload == "invalid_request":
        response = Token_b2b.token_invalid_json(TestContext.token)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json.get("error")
    elif request_payload == "invalid_client":
        response = Token_b2b.post_b2b_with_grant_type(TestContext.token, "b2b")
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json.get("error")

    assert TestContext.response_status_code == 400, "Unsupported grant type for token has failed"
    logging.info(
        "The response of Invalid Request Journey (POST) for Token Endpoint:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@then(parsers.parse('I see a "{error_message}" error message'))
def verify_token_error_message(error_message):
    assert TestContext.error_message == error_message, "Error Message didnt returned"


@then(parsers.parse("I see a {status_code_returned}"))
def verify_token_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned)
