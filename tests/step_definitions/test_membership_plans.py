import json
import logging

from json_diff import Comparator
from pytest_bdd import scenarios, when

from tests.conftest import response_to_json, setup_token
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_helpers import MembershipCardTestData
from tests.requests.membership_plans import MembershipPlans

scenarios("membership_plans/")

""" Step definations - Loyalty Plans"""


@when('I perform GET request to view journey field for "<loyalty_scheme>"')
def verify_journey_field(loyalty_scheme, env, channel):
    setup_token()
    response = MembershipPlans.get_membership_plan_journey_field(TestContext.token, loyalty_scheme)
    logging.info(
        "The Membership plan for " + loyalty_scheme + " is: \n" + json.dumps(response_to_json(response), indent=4)
    )

    with open(MembershipCardTestData.get_expected_membership_plan_json(loyalty_scheme, env, channel)) as json_file:
        json_data = json.load(json_file)

    stored_json = json.dumps(json_data)
    expected_membership_plan_journey_field = json.loads(stored_json)
    actual_membership_plan_journey_field = response.json()

    difference = json_compare(actual_membership_plan_journey_field, expected_membership_plan_journey_field)
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


def json_compare(actual_membership_plan_journey_field, expected_membership_plan_journey_field):
    """This function will compare two Json objects using json_diff and
    create a third json with comparison results"""

    json.dump(actual_membership_plan_journey_field, open(constants.JSON_DIFF_ACTUAL_JSON, "w"), indent=4)
    json.dump(expected_membership_plan_journey_field, open(constants.JSON_DIFF_EXPECTED_JSON, "w"), indent=4)

    engine = Comparator(open(constants.JSON_DIFF_ACTUAL_JSON, "r"), open(constants.JSON_DIFF_EXPECTED_JSON, "r"))
    return engine.compare_dicts()
