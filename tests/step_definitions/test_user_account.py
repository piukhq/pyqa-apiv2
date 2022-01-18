import json
import logging

from pytest_bdd import parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.conftest import response_to_json
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.requests.service import CustomerAccount
from tests.step_definitions import test_membership_cards

scenarios("user_accounts/")


@when(parsers.parse("I perform POST request to update email"))
def update_user_email(channel, env, test_email):
    response = CustomerAccount.user_email_update(TestContext.token, test_email)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "User email update is successful : \n\n "
        + Endpoint.BASE_URL
        + api.ENDPOINT_EMAIL_UPDATE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@when(parsers.parse('I perform POST request to add and authorise "{merchant}" membership card using b2b token'))
def verify_add_and_auth_b2b(merchant):
    test_membership_cards.verify_add_and_auth_b2b(merchant)


@then(parsers.parse('verify the data stored in DB after "{journey_type}" journey for "{merchant}"'))
def verify_loyalty_card_into_database(journey_type, merchant):
    test_membership_cards.verify_loyalty_card_into_database(journey_type, merchant)


@then(parsers.parse('verify that the PLL links are deleted from the scheme account for "{journey_type2}"'))
def verify_pll_links_scheme_account(journey_type2):
    test_membership_cards.verify_pll_links_scheme_account(journey_type2)


@then(parsers.parse("I perform POST request to update email again"))
def update_user_email_again(channel, env, test_email):
    response = CustomerAccount.user_email_update(TestContext.token, test_email)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "User email update is successful : \n\n "
        + Endpoint.BASE_URL
        + api.ENDPOINT_EMAIL_UPDATE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )


@when(parsers.parse("I perform POST request to update email with invalid token"))
def update_user_email_invalid_token(channel, env, test_email):
    response = CustomerAccount.user_email_update(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), test_email
    )
    TestContext.response_status_code = response.status_code
    response_json = response_to_json(response)
    logging.info(
        "The response of POST/email_update with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_EMAIL_UPDATE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when(parsers.parse('I perform POST request to update email with "{request_payload}"' ' with "{status_code}"'))
def update_user_email_invalid_data(test_email, request_payload, status_code):
    if request_payload == "invalid_request":
        response = CustomerAccount.user_email_update_invalid_data(TestContext.token, test_email, request_payload)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        logging.info(
            "The response of Invalid request Journey (POST) for Update Email :\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_EMAIL_UPDATE
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )

    elif request_payload == "invalid_json":
        response = CustomerAccount.user_email_update_invalid_data(TestContext.token, test_email, request_payload)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        logging.info(
            "The response of Invalid json Journey (POST) for Update Email :\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_EMAIL_UPDATE
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )

        assert TestContext.response_status_code == int(status_code), "Invalid data request failed"


@when(parsers.parse('I perform POST request to update email with "{duplicate_email}"  with "{status_code}"'))
def update_user_email_duplicate(test_email, duplicate_email, status_code):
    response = CustomerAccount.user_email_update(TestContext.token, duplicate_email)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json["error_message"]
    TestContext.error_slug = response_json["error_slug"]
    logging.info(
        "The response of Duplicate email Update (POST) is :\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_EMAIL_UPDATE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert TestContext.response_status_code == int(status_code), "Duplicate Email Request"


@then(parsers.parse("I perform DELETE request to delete user successfully"))
def delete_user_successfully(channel, env):
    response = CustomerAccount.delete_user(TestContext.token)
    assert response.status_code == 202, "The user deletion is not successful"
    logging.info("User is deleted successfully from the system")


@when(parsers.parse("I perform DELETE request to delete user with invalid token"))
def delete_user_invalid_token(channel, env):
    response = CustomerAccount.delete_user(TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN))
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of DELETE /me with invalid token is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_DELETE_USER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@then(parsers.parse("I see a {status_code_returned}"))
def verify_membership_card_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned)


@then(parsers.parse('I see a "{error_message}" error message'))
def verify_error_message(error_message):
    assert TestContext.error_message == error_message, "Error Message not returned"


@then(parsers.parse('I see a "{error_slug}" error slug'))
def verify_error_slug(error_slug):
    assert TestContext.error_slug == error_slug, "Error Slug not returned"
