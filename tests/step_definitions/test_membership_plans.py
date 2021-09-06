import json
import logging
import time

from json import JSONDecodeError
from json_diff import Comparator


from pytest_bdd import (
    scenarios,
    then,
    when,
    parsers
)
from requests.exceptions import HTTPError

import config

from tests import api
from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import PaymentCardTestData, TestData
from tests.helpers.vault.channel_vault import create_bearer_token
from tests.requests.membership_plans import MembershipPlans
from tests.requests.paymentcard_account import PaymentCards

scenarios("membership_plans/")

"""Step definitions - Add plans """


@then(parsers.parse('I can ensure the "{merchant}" plan details match with expected data'))
def ensure_the_merchants_plan_details_match_with_expected_data(merchant, env, channel):
    """GET a merchant's membership plan and compare with
     expected membership plan of that merchant"""

    response = MembershipPlans.get_membership_plan(TestContext.token, merchant)
    logging.info("The Membership plan for " + merchant + " is: \n" + json.dumps(response_to_json(response), indent=4))
    with open(TestData.get_expected_membership_plan_json(merchant, env, channel)) as json_file:
        json_data = json.load(json_file)
    stored_json = json.dumps(json_data)
    expected_membership_plan = json.loads(stored_json)
    actual_membership_plan = response.json()
    difference = json_compare(actual_membership_plan, expected_membership_plan)
    if json.dumps(difference) != "{}":
        logging.info(
            "The expected and actual membership plan of "
            + merchant
            + " has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual membership plan of " + merchant + " is not the same")
    else:
        logging.info("The expected and actual membership plan of " + merchant + " is same")


def json_compare(actual_membership_plan, expected_membership_plan):
    """This function will compare two Json objects using json_diff and
    create a third json with comparison results """

    json.dump(actual_membership_plan, open(constants.JSON_DIFF_ACTUAL_JSON, "w"), indent=4)
    json.dump(expected_membership_plan, open(constants.JSON_DIFF_EXPECTED_JSON, "w"), indent=4)
    actual_membership_plan = open(constants.JSON_DIFF_ACTUAL_JSON, "r")
    expected_membership_plan = open(constants.JSON_DIFF_EXPECTED_JSON, "r")
    engine = Comparator(actual_membership_plan, expected_membership_plan)
    return engine.compare_dicts()


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json