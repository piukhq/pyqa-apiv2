import json
import logging

from json_diff import Comparator
from pytest_bdd import scenarios, then, when

from tests.conftest import response_to_json, setup_token
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import MembershipCardTestData
from tests.requests.membership_plans import MembershipPlans

scenarios("membership_plans/")

""" Step definations - Loyalty Plans"""


@when('I perform GET request to view journey field for "<loyalty_scheme>"')
def verify_journey_field(loyalty_scheme, env, channel):
    response = MembershipPlans.get_membership_plan_journey_field(setup_token(), loyalty_scheme)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The Membership plan for " + loyalty_scheme + " is: \n" + json.dumps(response_to_json(response), indent=4)
    )

    with open(MembershipCardTestData.get_expected_membership_plan_json(loyalty_scheme, env, channel)) as json_file:
        json_data = json.load(json_file)

    stored_json = json.dumps(json_data)
    TestContext.expected_membership_plan_journey_field = json.loads(stored_json)
    TestContext.actual_membership_plan_journey_field = response.json()


def json_compare(actual_membership_plan_journey_field, expected_membership_plan_journey_field):
    """This function will compare two Json objects using json_diff and
    create a third json with comparison results"""

    json.dump(actual_membership_plan_journey_field, open(constants.JSON_DIFF_ACTUAL_JSON, "w"), indent=4)
    json.dump(expected_membership_plan_journey_field, open(constants.JSON_DIFF_EXPECTED_JSON, "w"), indent=4)

    engine = Comparator(open(constants.JSON_DIFF_ACTUAL_JSON, "r"), open(constants.JSON_DIFF_EXPECTED_JSON, "r"))
    return engine.compare_dicts()


@then('I can see the journey fields of that merchant "<loyalty_scheme>"')
def verify_journey_field_type(loyalty_scheme):
    difference = json_compare(
        TestContext.actual_membership_plan_journey_field, TestContext.expected_membership_plan_journey_field
    )
    if json.dumps(difference) != "{}":
        logging.info(
            "The expected and actual membership plan of "
            + loyalty_scheme
            + "journey_field has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception(
            "The expected and actual journey type membership plan of " + loyalty_scheme + " is not the same"
        )
    else:
        logging.info("The expected and actual membership plan of " + loyalty_scheme + " journey fields is same")


@then("I verify the <status_code> for journey field appeared")
def verify_success_journey_field(status_code):
    assert TestContext.response_status_code == int(status_code), "Journey field value didnt match"


@when('I perform GET request to view journey field for "<loyalty_scheme>" for invalid token')
def verify_journey_field_invalid_token(loyalty_scheme):
    response = MembershipPlans.get_membership_plan_journey_field(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), loyalty_scheme
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 401
    return response


@then('I verify "<error_message> <error_slug>" in loyalty scheme response')
def verify_plan_response_error_slug_and_error_message(error_message, error_slug):
    assert (
        TestContext.error_message == error_message and TestContext.error_slug == error_slug
    ), "error message didnt appeared in response"


@when('I perform GET request to view journey field for "<loyalty_scheme>" for invalid resource')
def verify_invalid_resource_for_loyalty_scheme(loyalty_scheme):
    response = MembershipPlans.get_membership_plan_journey_field(setup_token(), loyalty_scheme)

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 404
    return response
