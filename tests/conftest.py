import json
import logging
import time

from json import JSONDecodeError

import pytest

from faker import Faker
from pytest_bdd import given, parsers, then, when
from requests.exceptions import HTTPError

import config

from tests import api
from tests.api.base import Endpoint
from tests.api.transactionmatching_base import TransactionMatchingEndpoint
from tests.helpers import constants
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.vault.channel_vault import (
    create_b2b_token,
    create_bearer_token,
    get_private_key_secret,
)
from tests.requests.loyalty_cards import MembershipCards
from tests.requests.paymentcard_account import PaymentCards
from tests.requests.service import CustomerAccount
from tests.requests.token_b2b import Token_b2b


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """This function will log the failed BDD-Step at the end of logs"""
    logging.error(f"Step failed: {step}")
    delete_scheme_account()
    delete_payment_card()
    delete_user()

def pytest_bdd_before_step_call(request, feature, scenario, step, step_func, step_func_args):
    """Called before step function is executed with evaluated arguments"""

    if request.getfixturevalue("selected_merchant").upper() != "ALL":
        if "merchant" in step_func_args:
            merchants_list = request.getfixturevalue("selected_merchant").upper().split(",")
            if (step_func_args["merchant"]).upper() not in merchants_list:
                pytest.skip(msg=f"merchant{step_func_args['merchant']}")


def pytest_bdd_after_scenario():
    delete_scheme_account()
    delete_payment_card()
    delete_user()


def pytest_html_report_title(report):
    """Customized title for html report"""
    report.title = "BANK API 2.0 Automation Result_Pytest_BDD"


"""Reading inputs from terminal"""


def pytest_addoption(parser):
    parser.addoption(
        "--channel",
        action="store",
        default="bink",
        help="Channel: can be bink or lloyds should pass",
    )
    parser.addoption(
        "--env",
        action="store",
        default="staging",
        help="env : can be staging or sandbox or prod",
    )
    parser.addoption(
        "--encryption",
        action="store",
        default="false",
        help="encryption : can be true or false",
    )
    parser.addoption(
        "--selected_merchant",
        action="store",
        default="All",
        help="selected_merchant: can be Viator or SquareMeal combination e.g. Viator,SquareMeal",
    )


"""Terminal parameter Fixtures"""


@pytest.fixture(scope="session")
def selected_merchant(pytestconfig):
    """Returns merchant"""
    return pytestconfig.getoption("selected_merchant")


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
    TransactionMatchingEndpoint.set_environment(env)
    # logging.getLogger().setLevel(level=logging.ERROR)
    logging.info("Environment Setup ready")
    TestDataUtils.set_test_data(env)
    TestContext.environ = env


@pytest.fixture(scope="session", autouse=True)
def handle_optional_encryption(encryption):
    TestContext.flag_encrypt = encryption


@pytest.fixture()
def test_email():
    faker = Faker()
    return constants.EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@pytest.fixture()
def lloyds_test_email():
    faker = Faker()
    return constants.LLOYDS_EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@pytest.fixture()
def bos_test_email():
    faker = Faker()
    return constants.BOS_EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@pytest.fixture()
def halifax_test_email():
    faker = Faker()
    return constants.HALIFAX_EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@pytest.fixture()
def squaremeal_test_email():
    faker = Faker()
    return constants.SQUAREMEAL_EMAIL_TEMPLATE.replace("email", str(faker.random_int(100, 999999)))


@pytest.fixture()
def lloyds_external_id():
    faker = Faker()
    return constants.LLOYDS_EXTERNAL_ID_TEMPLATE.replace("id", str(faker.random_int(100, 999999)))


@pytest.fixture()
def bos_external_id():
    faker = Faker()
    return constants.BOS_EXTERNAL_ID_TEMPLATE.replace("id", str(faker.random_int(100, 999999)))


@pytest.fixture()
def halifax_external_id():
    faker = Faker()
    return constants.HALIFAX_EXTERNAL_ID_TEMPLATE.replace("id", str(faker.random_int(100, 999999)))


@pytest.fixture()
def squaremeal_external_id():
    faker = Faker()
    return constants.SQUAREMEAL_EXTERNAL_ID_TEMPLATE.replace("id", str(faker.random_int(100, 999999)))


@given("I am a Bink user")
def login_user(channel, env):
    setup_token()


@given("I am a Bink Wallet user1")
def login_user1(channel, env):
    setup_third_token()


def setup_token():
    TestContext.token = create_bearer_token(
        sub=TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.USER_DETAIL),
        channel=config.BINK.bundle_id,
    )
    return TestContext.token


def setup_second_token():
    TestContext.second_token = create_bearer_token(
        sub=TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.USER_DETAIL2),
        channel=config.BINK.bundle_id,
    )
    return TestContext.second_token


def setup_third_token():
    TestContext.third_token = create_bearer_token(
        sub=TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.USER_DETAIL3),
        channel=config.BINK.bundle_id,
    )
    return TestContext.third_token


def setup_b2b_token():
    key_secret = get_private_key_secret(config.BINK.kid)
    user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.B2B_EMAIL)
    external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.B2B_EXTERNAL_ID)
    TestContext.b2btoken = create_b2b_token(key=key_secret, sub=external_id, kid=config.BINK.kid, email=user_email)
    TestContext.external_id["bink_user"] = external_id
    return TestContext.b2btoken


def setup_b2b_token_user2():
    key_secret = get_private_key_secret(config.BINK.kid)
    user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.B2B_EMAIL2)
    external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.B2B_EXTERNAL_ID2)
    TestContext.b2btoken = create_b2b_token(key=key_secret, sub=external_id, kid=config.BINK.kid, email=user_email)
    TestContext.external_id["bink_user2"] = external_id
    return TestContext.b2btoken


def response_to_json(response):
    try:
        response_json = response.json()
    except JSONDecodeError or Exception:
        raise Exception(f"Empty response and the response Status Code is {str(response.status_code)}")
    return response_json


@then(parsers.parse('I perform DELETE request to delete the first wallet "{merchant}" membership card'))
def delete_first_wallet_scheme_account(merchant=None):
    time.sleep(3)
    print("firsttoken", TestContext.first_wallet_token)
    print("schemeid", TestContext.first_wallet_scheme_account_id)
    response_del_schemes = MembershipCards.delete_scheme_account(
        TestContext.first_wallet_token, TestContext.first_wallet_scheme_account_id
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
    logging.info("The response of delete scheme account (POST) is:\n\n" + Endpoint.BASE_URL + api.ENDPOINT_TOKEN)


@then(parsers.parse('I perform DELETE request to delete the "{merchant}" membership card'))
def delete_scheme_account(merchant=None):
    time.sleep(3)

    response_del_schemes = MembershipCards.delete_scheme_account(
        TestContext.token, TestContext.current_scheme_account_id
    )
    TestContext.response_status_code = response_del_schemes.status_code
    """Even if the scheme account is deleted, it is not updating DB so quickly
     so delay is required before next execution"""
    try:
        if response_del_schemes.status_code == 202:
            logging.info("Loyalty card is deleted successfully")
        elif response_del_schemes.status_code == 404:
            logging.info("Loyalty card is already deleted")
        else:
            logging.info(response_del_schemes.status_code)
            delete_user()

    except HTTPError as network_response:
        assert network_response.response.status_code == 404 or 400


@then(parsers.parse('I perform DELETE request to delete "{payment_card_provider}" the payment card'))
@then("I perform DELETE request to delete the payment card which is already deleted")
def delete_payment_card(payment_card_provider=None):
    time.sleep(3)

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


@then(parsers.parse('I perform DELETE request to delete the first wallet "{payment_card_provider}" the payment card'))
def delete_payment_card_first_wallet(payment_card_provider=None):
    time.sleep(3)

    response = PaymentCards.delete_payment_card(TestContext.first_wallet_token, TestContext.current_payment_card_id)
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


@then("I perform DELETE request to delete all the payment cards")
def delete_all_payment_card():
    time.sleep(3)
    wallet_response = TestContext.actual_view_wallet_field
    print("wallet response", wallet_response)
    for i in range(len(wallet_response["payment_accounts"])):
        response = PaymentCards.delete_payment_card(TestContext.token, wallet_response["payment_accounts"][i]["id"])
        TestContext.response_status_code = response.status_code
        try:
            if response.status_code == 202:
                logging.info(f"Payment card {i} is deleted successfully")
            elif response.status_code == 404:
                response_json = response_to_json(response)
                TestContext.error_message = response_json["error_message"]
                TestContext.error_slug = response_json["error_slug"]
                logging.info(f"Payment card {i} is already deleted")

        except HTTPError as network_response:
            assert network_response.response.status_code == 404 or 400, "Payment card deletion is not successful"


@then("I perform DELETE request to delete all the loyalty cards")
def delete_all_loyalty_card():
    time.sleep(3)
    wallet_response = TestContext.actual_view_wallet_field
    for i in range(len(wallet_response["payment_accounts"][0]["pll_links"])):
        response = MembershipCards.delete_scheme_account(
            TestContext.token,
            wallet_response["payment_accounts"][0]["pll_links"][i]["loyalty_card_id"],
        )
        print(
            "wallet",
            wallet_response["payment_accounts"][0]["pll_links"][i]["loyalty_card_id"],
        )
        TestContext.response_status_code = response.status_code
        try:
            if response.status_code == 202:
                logging.info(f"Loyalty card {i} is deleted successfully")
            elif response.status_code == 404:
                response_json = response_to_json(response)
                TestContext.error_message = response_json["error_message"]
                TestContext.error_slug = response_json["error_slug"]
                logging.info(f"Loyalty card {i} is already deleted")

        except HTTPError as network_response:
            assert network_response.response.status_code == 404 or 400, "Loyalty card deletion is not successful"


@given("I am in Bink channel to get b2b token")
def set_up_client_token_for_b2b_user1():
    setup_b2b_token()


@when("I am in Bink channel to get b2b token for second user")
def set_up_client_token_for_b2b_user2():
    setup_b2b_token_user2()


@when(parsers.parse('I perform POST token request for token type "{token_type}" to get access token'))
def perform_post_b2b_with_user1(token_type):
    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, token_type)
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.first_wallet_token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of B2B token (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.all_users["bink_user"] = TestContext.token
    assert response.status_code == 200, "/token Journey failed to get access token"


@when(parsers.parse('I perform POST token request for token type "{token_type}" to get access token for second user'))
def perform_post_b2b_with_user2(token_type):
    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, token_type)
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of B2B token (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.all_users["bink_user2"] = TestContext.token
    assert response.status_code == 200, "/token Journey failed to get access token"


@given("I am a Lloyds user")
def get_lloyds_user(lloyds_external_id, lloyds_test_email):
    key_secret = get_private_key_secret(config.LLOYDS.kid)
    # user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EMAIL)
    # external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EXTERNAL_ID)
    TestContext.b2btoken = create_b2b_token(
        key=key_secret,
        sub=lloyds_external_id,
        kid=config.LLOYDS.kid,
        email=lloyds_test_email,
    )

    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, "b2b")
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    TestContext.email = TestContext.user_email = lloyds_test_email
    logging.info(
        "The response of B2B token (POST) for lloyds is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
        + "\n"
        + "External Id"
        + "\n"
        + lloyds_external_id
        + "\n"
        + "User Email"
        + "\n"
        + lloyds_test_email
    )
    assert response.status_code == 200, "/token Journey failed to get access token"
    TestContext.all_users["lloyds_user"] = TestContext.token
    TestContext.external_id["lloyds_user"] = lloyds_external_id
    return TestContext.token


@given("I am a bos user")
def get_bos_user(bos_external_id, bos_test_email):
    key_secret = get_private_key_secret(config.BOS.kid)
    # user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EMAIL)
    # external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EXTERNAL_ID)
    TestContext.b2btoken = create_b2b_token(
        key=key_secret, sub=bos_external_id, kid=config.BOS.kid, email=bos_test_email
    )

    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, "b2b")
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    TestContext.user_email = bos_test_email
    logging.info(
        "The response of B2B token (POST) for bos is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
        + "\n"
        + "External Id"
        + "\n"
        + bos_external_id
        + "\n"
        + "User Email"
        + "\n"
        + bos_test_email
    )
    assert response.status_code == 200, "/token Journey failed to get access token"
    TestContext.all_users["bos_user"] = TestContext.token
    TestContext.external_id["bos_user"] = bos_external_id
    return TestContext.token


@given("I am a halifax user")
def get_halifax_user(halifax_external_id, halifax_test_email):
    key_secret = get_private_key_secret(config.HALIFAX.kid)
    # user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EMAIL)
    # external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EXTERNAL_ID)
    TestContext.b2btoken = create_b2b_token(
        key=key_secret,
        sub=halifax_external_id,
        kid=config.HALIFAX.kid,
        email=halifax_test_email,
    )
    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, "b2b")
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    TestContext.email = TestContext.user_email = halifax_test_email
    logging.info(
        "The response of B2B token (POST) for halifax is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
        + "\n\n"
        + "External Id"
        + "\n"
        + halifax_external_id
        + "\n"
        + "User Email"
        + "\n"
        + halifax_test_email
    )
    assert response.status_code == 200, "/token Journey failed to get access token"
    TestContext.all_users["halifax_user"] = TestContext.token
    TestContext.external_id["halifax_user"] = halifax_external_id
    return TestContext.token


@given("I am a squaremeal user")
def get_squaremeal_user(squaremeal_external_id, squaremeal_test_email):
    key_secret = get_private_key_secret(config.SQUAREMEAL.kid)
    # user_email = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EMAIL)
    # external_id = TestDataUtils.TEST_DATA.bink_user_accounts.get(constants.LLOYDS_EXTERNAL_ID)
    TestContext.b2btoken = create_b2b_token(
        key=key_secret,
        sub=squaremeal_external_id,
        kid=config.SQUAREMEAL.kid,
        email=squaremeal_test_email,
    )

    response = Token_b2b.post_b2b_with_grant_type(TestContext.b2btoken, "b2b")
    time.sleep(1)
    response_json = response_to_json(response)
    TestContext.access_token = response_json.get("access_token")
    TestContext.token_type = response_json.get("token_type")
    TestContext.refresh_token_type = response_json.get("refresh_token")
    TestContext.token = TestContext.token_type + " " + TestContext.access_token
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of B2B token (POST) for squaremeal is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_TOKEN
        + "\n\n"
        + json.dumps(response_json, indent=4)
        + "\n\n"
        + "External Id"
        + "\n"
        + squaremeal_external_id
        + "\n"
        + "User Email"
        + "\n"
        + squaremeal_test_email
    )
    assert response.status_code == 200, "/token Journey failed to get access token"
    TestContext.all_users["squaremeal_user"] = TestContext.token
    TestContext.external_id["squaremeal_user"] = squaremeal_external_id
    return TestContext.token


@then(parsers.parse("I perform DELETE request to delete user successfully"))
def delete_user(env="staging"):
    all_users = TestContext.all_users
    external_id = TestContext.external_id
    if all_users != {}:
        for i in all_users:
            response = CustomerAccount.delete_user(all_users[i])
            assert response.status_code == 202, "The user deletion is not successful"
            logging.info(f"User {i} is deleted successfully from the system")
        all_users.clear()
        external_id.clear()
