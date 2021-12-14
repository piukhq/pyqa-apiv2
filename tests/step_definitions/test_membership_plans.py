import json
import logging

from deepdiff import DeepDiff
from json_diff import Comparator
from pytest_bdd import parsers, scenarios, then, when

from tests.conftest import response_to_json, setup_third_token, setup_token
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import TestData
from tests.requests.membership_plans import MembershipPlans

scenarios("membership_plans/")

""" Step definations - Loyalty Plans"""


@when(parsers.parse('I perform GET request to view journey field for "{loyalty_scheme}"'))
def verify_journey_field(loyalty_scheme, env, channel):
    response = MembershipPlans.get_membership_plan_journey_field(setup_token(), loyalty_scheme)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The Membership plan for " + loyalty_scheme + " is: \n" + json.dumps(response_to_json(response), indent=4)
    )

    with open(TestData.get_expected_membership_plan_json(loyalty_scheme, env, channel)) as json_file:
        json_data = json.load(json_file)

    stored_json = json.dumps(json_data)
    TestContext.expected_membership_plan_journey_field = json.loads(stored_json)
    TestContext.actual_membership_plan_journey_field = response.json()


@when(parsers.parse('I perform GET request to view "{loyalty_scheme}" loyalty plan by id'))
def verify_get_loyalty_plan_by_id(loyalty_scheme, env, channel):
    response = MembershipPlans.get_loyalty_plan_by_id(TestContext.token, loyalty_scheme)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The loyalty plan for " + loyalty_scheme + " is: \n" + json.dumps(response_to_json(response), indent=4)
    )

    with open(TestData.get_expected_loyalty_plan_by_id_json(loyalty_scheme, env, channel)) as json_file:
        expected_data = json.load(json_file)

    # stored_json = json.dumps(json_data)
    difference = json_compare_loyalty(response.json(), expected_data)
    if difference:
        logging.info(
            "The expected and actual loyalty plan of "
            + loyalty_scheme
            + "loyalty plan fields has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual loyalty plan of " + loyalty_scheme + " is not the same")
    else:
        logging.info("The expected and actual loyalty plan of " + loyalty_scheme + " journey fields is same")

    # TestContext.expected_loyalty_plan_by_id_field = json.loads(stored_json)
    # TestContext.actual_loyalty_plan_by_id_field = response.json()


@when(parsers.parse("I perform GET request to view all available loyalty plans"))
def verify_get_all_loyalty_plans(env, channel):
    response = MembershipPlans.get_all_loyalty_plans(setup_token())
    TestContext.response_status_code = response.status_code
    logging.info("The loyalty plans available are: \n" + json.dumps(response_to_json(response), indent=4))

    with open(TestData.get_expected_all_loyalty_plans_json(env, channel)) as json_file:
        json_data = json.load(json_file)

    stored_json = json.dumps(json_data)
    TestContext.expected_all_loyalty_plans_field = json.loads(stored_json)
    TestContext.actual_all_loyalty_plans_field = response.json()


@when(parsers.parse("I perform GET request to view all available loyalty bank plans"))
def verify_get_all_loyalty_bank_plans(env, channel):
    response = MembershipPlans.get_all_loyalty_plans(TestContext.token)
    TestContext.response_status_code = response.status_code
    logging.info("The loyalty bank plans available are: \n" + json.dumps(response_to_json(response), indent=4))

    with open(TestData.get_expected_all_loyalty_plans_json(env, channel)) as json_file:
        json_data = json.load(json_file)

    stored_json = json.dumps(json_data)
    TestContext.expected_all_loyalty_plans_field = json.loads(stored_json)
    TestContext.actual_all_loyalty_plans_field = response.json()


@when(parsers.parse("I perform GET request to view loyalty plans overview"))
def verify_loyalty_plans_overview(env, channel):
    response = MembershipPlans.get_loyalty_plans_overview(setup_third_token())
    TestContext.response_status_code = response.status_code
    logging.info("The loyalty plans Overview is: \n" + json.dumps(response_to_json(response), indent=4))

    # with open(TestData.get_expected_loyalty_plans_overview_json(env, channel)) as json_file:
    #      expected_data = json.load(json_file)

    #   difference = json_compare_loyalty_overview(response.json(), expected_data)
    #   if difference:
    #       logging.info(
    #           "The expected and actual loyalty plan overview "
    #            + "fields has following differences"
    #          + json.dumps(difference, sort_keys=True, indent=4)
    #       )
    #      raise Exception("The expected and actual loyalty plan overview is not the same")
    #   else:
    #      logging.info("The expected and actual loyalty plan overview is same")


def json_compare(actual_membership_plan_journey_field, expected_membership_plan_journey_field):
    """This function will compare two Json objects using json_diff and
    create a third json with comparison results"""

    json.dump(actual_membership_plan_journey_field, open(constants.JSON_DIFF_ACTUAL_JSON, "w"), indent=4)
    json.dump(expected_membership_plan_journey_field, open(constants.JSON_DIFF_EXPECTED_JSON, "w"), indent=4)

    engine = DeepDiff(open(constants.JSON_DIFF_ACTUAL_JSON, "r"), open(constants.JSON_DIFF_EXPECTED_JSON, "r"),
                      ignore_order=True)
    return engine


def json_compare_loyalty(actual_loyalty_plan_by_id_field, expected_loyalty_plan_by_id_field):
    compare = DeepDiff(actual_loyalty_plan_by_id_field, expected_loyalty_plan_by_id_field, ignore_order=True)
    return compare


def json_compare_loyalty_overview(actual_loyalty_plans_overview, expected_loyalty_plans_overview):
    compare = DeepDiff(actual_loyalty_plans_overview, expected_loyalty_plans_overview, ignore_order=True)
    return compare


@then(parsers.parse('I can see the journey fields of that merchant "{loyalty_scheme}"'))
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


@then(parsers.parse('I can see the loyalty plan fields of that merchant "{loyalty_scheme}"'))
def verify_loyalty_plan_fields_by_id(loyalty_scheme):
    difference = json_compare_loyalty(
        TestContext.actual_loyalty_plan_by_id_field, TestContext.expected_loyalty_plan_by_id_field
    )
    if json.dumps(difference) != "{}":
        logging.info(
            "The expected and actual loyalty plan of "
            + loyalty_scheme
            + "loyalty plan fields has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual loyalty plan of " + loyalty_scheme + " is not the same")
    else:
        logging.info("The expected and actual loyalty plan of " + loyalty_scheme + " journey fields is same")


@then(parsers.parse("I verify the {status_code} for journey field appeared"))
def verify_success_journey_field(status_code):
    assert TestContext.response_status_code == int(status_code), "Journey field value didnt match"


@then(parsers.parse("I verify the {status_code} for loyalty plan"))
def verify_success_loyalty_plan_field(status_code):
    assert TestContext.response_status_code == int(status_code), "Loyalty plan status code did not match"


@when(parsers.parse('I perform GET request to view journey field for "{loyalty_scheme}" for invalid token'))
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


@when(parsers.parse("I perform GET request to view loyalty plans overview with invalid token"))
def verify_loyalty_plan_overview_invalid_token():
    response = MembershipPlans.get_loyalty_plans_overview(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN)
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 401
    return response


@when(parsers.parse('I perform GET request to view "{loyalty_scheme}" loyalty plan by id with invalid token'))
def verify_loyalty_plan_fields_invalid_token(loyalty_scheme):
    response = MembershipPlans.get_loyalty_plan_by_id(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), loyalty_scheme
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 401
    return response


@when("I perform GET request to view all available loyalty plans with invalid token")
def verify_all_loyalty_plans_invalid_token():
    response = MembershipPlans.get_all_loyalty_plans(TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN))

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of all loyalty plans with invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 401
    return response


@then(parsers.parse('I verify "{error_message}" "{error_slug}" in loyalty scheme response'))
def verify_plan_response_error_slug_and_error_message(error_message, error_slug):
    assert (
        TestContext.error_message == error_message and TestContext.error_slug == error_slug
    ), "error message didnt appeared in response"


@when(parsers.parse('I perform GET request to view journey field for "{loyalty_scheme}" for invalid resource'))
def verify_invalid_resource_for_loyalty_scheme(loyalty_scheme):
    response = MembershipPlans.get_membership_plan_journey_field(setup_token(), loyalty_scheme)
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 404
    return response


@when(parsers.parse('I perform GET request to view "{loyalty_scheme}" loyalty plan by id with invalid resource'))
def verify_invalid_resource_for_loyalty_plan(loyalty_scheme):
    response = MembershipPlans.get_loyalty_plan_by_id(setup_token(), loyalty_scheme)
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info("The response of invalid token is: \n\n" + json.dumps(response_json, indent=4))
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert TestContext.response_status_code == 404
    return response


@then("I verify all plans appeared correctly")
def verify_plans_in_lloyds():
    difference = json_compare(TestContext.expected_all_loyalty_plans_field, TestContext.actual_all_loyalty_plans_field)
    if json.dumps(difference) != "{}":
        logging.info(
            "The expected and actual all membership plans of has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual all membership plans are not the same")
    else:
        logging.info("The expected and actual all membership plans are same")

