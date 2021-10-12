import logging
import time

from json import JSONDecodeError

import pytest

from faker import Faker
from pytest_bdd import given, then
from requests.exceptions import HTTPError

import config

from tests.api.base import Endpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.vault.channel_vault import create_bearer_token
from tests.requests.membership_cards import MembershipCards
from tests.requests.paymentcard_account import PaymentCards


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """This function will log the failed BDD-Step at the end of logs"""
    logging.info(f"Step failed: {step}")


def pytest_bdd_after_scenario():
    delete_scheme_account()
    delete_payment_card()


def pytest_html_report_title(report):
    """Customized title for html report"""
    report.title = "BANK API 2.0 Automation Result_Pytest_BDD"


@pytest.fixture(scope="session", autouse=True)
def configure_html_report_env(request, env, channel):
    """Delete existing data in the test report and add bink api execution details"""
    for ele in list(request.config._metadata.keys()):
        del request.config._metadata[ele]
    # if re.search(r'^(GITLAB_|CI_)', k): for git lab related extra table contents
    request.config._metadata.update({"Test Environment": env.upper(), "Channel": channel.upper()})


"""Reading inputs from terminal"""


def pytest_addoption(parser):
    parser.addoption("--channel", action="store", default="bink", help="Channel: can be bink or barclays should pass")
    parser.addoption("--env", action="store", default="dev", help="env : can be dev or staging or prod")
    parser.addoption("--encryption", action="store", default="false", help="encryption : can be true or false")


"""Terminal parameter Fixtures"""


@pytest.fixture(scope="session")
def channel(pytestconfig):
    """Returns current channel"""
    return pytestconfig.getoption("channel")


@pytest.fixture(scope="session")
def env(pytestconfig):
    """Returns current environment"""
    return pytestconfig.getoption("env")


@pytest.fixture(scope="session")
def encryption(pytestconfig):
    """Returns the choice: with/without encryption"""
    return pytestconfig.getoption("encryption")


@pytest.fixture(scope="session", autouse=True)
def set_environment(env):
    Endpoint.set_environment(env)
    logging.info("Environment Setup ready")
    TestDataUtils.set_test_data(env)


@pytest.fixture(scope="session", autouse=True)
def handle_optional_encryption(encryption):
    TestContext.flag_encrypt = encryption


@pytest.fixture()
def test_email():
    faker = Faker()
    return constants.EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@given("I am a Bink user")
def login_user(channel, env):
    setup_token()
    # TestContext.channel_name = channel
    # if channel == config.BINK.channel_name:
    #     response = CustomerAccount.login_bink_user()
    #     if response is not None:
    #         try:
    #             logging.info(f"POST Login response: {response.json()} ")
    #             assert response.status_code == 200 and response.json().get(
    #                 "email"
    #             ) == TestDataUtils.TEST_DATA.bink_user_accounts.get(
    #                 constants.USER_ID
    #             ), "User login in Bink Channel is not successful"
    #             return TestContext.token
    #         except Exception as e:
    #             logging.info(f"Gateway Timeout error :{e}")


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


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json


@then('I perform DELETE request to delete the "<merchant>" membership card')
def delete_scheme_account(merchant=None):
    time.sleep(2)

    response_del_schemes = MembershipCards.delete_scheme_account(
        TestContext.token, TestContext.current_scheme_account_id
    )
    TestContext.response_status_code = response_del_schemes.status_code
    # response_del_schemes_1 = MembershipCards.delete_scheme_account(TestContext.token_channel_1,
    #                                                                TestContext.scheme_account_id1)
    """Even if the scheme account is deleted, it is not updating DB so quickly
     so delay is required before next execution"""
    try:
        if response_del_schemes.status_code == 202:
            logging.info("Loyalty card is deleted successfully")
        elif response_del_schemes.status_code == 404:
            logging.info("Loyalty card is already deleted")
        else:
            logging.info(response_del_schemes.status_code)

    except HTTPError as network_response:
        assert network_response.response.status_code == 404 or 400


@then('I perform DELETE request to delete "<payment_card_provider>" the payment card')
@then("I perform DELETE request to delete the payment card which is already deleted")
def delete_payment_card(payment_card_provider=None):
    time.sleep(2)

    response = PaymentCards.delete_payment_card(TestContext.token, TestContext.current_payment_card_id)
    TestContext.response_status_code = response.status_code
    try:
        if response.status_code == 202:
            logging.info("Payment card is deleted successfully")
        elif response.status_code == 404:
            response_json = response_to_json(response)
            TestContext.error_message = response_json["error_message"]
            TestContext.error_slug = response_json["error_slug"]
            logging.info("Payment card is already deleted")

    except HTTPError as network_response:
        assert network_response.response.status_code == 404 or 400, "Payment card deletion is not successful"
