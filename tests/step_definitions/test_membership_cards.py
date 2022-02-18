import json
import logging
import time

from deepdiff import DeepDiff
from pytest_bdd import parsers, scenarios, then, when

from tests import api
from tests.api.base import Endpoint
from tests.conftest import response_to_json, setup_third_token
from tests.helpers import constants
from tests.helpers.database.query_hermes import QueryHermes
from tests.helpers.test_context import TestContext
from tests.helpers.test_data_utils import TestDataUtils
from tests.helpers.test_helpers import TestData
from tests.requests.membership_cards import MembershipCards
from tests.step_definitions import test_paymentcard_account

scenarios("membership_cards/")

"""Step definitions - Add_field Journey (store card only) """


@when(parsers.parse('I perform POST request to add "{merchant}" membership card'))
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


@then(parsers.parse('verify the data stored in DB after "{journey_type}" journey for "{merchant}"'))
def verify_loyalty_card_into_database(journey_type, merchant):
    time.sleep(5)

    if journey_type == "Add_field":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.WALLET_ONLY)
            and scheme_account.scheme_id == TestData.get_membership_plan_id(merchant)
        )

    elif journey_type == "add_and_authorise" or journey_type == "add_and_register":

        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id, journey_type + "in database is not success"

    elif journey_type == "delete":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id and scheme_account.is_delete_scheme is True
        ), "Delete in database is not success"

    elif journey_type == "authorise_field" or journey_type == "join" or journey_type == "register_field":
        time.sleep(4)
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.ACTIVE)
        ), (journey_type + " in database is not success")

    elif journey_type == "add_field_then_add_auth":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.WALLET_ONLY)
        )

    elif journey_type == "join_failed":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status is TestDataUtils.TEST_DATA.scheme_status.get(constants.ENROL_FAILED)
            or TestDataUtils.TEST_DATA.scheme_status.get(constants.ENROL_FAILED)
        )

    elif journey_type == "pll":
        pll_links = [{"id": TestContext.current_payment_card_id, "active_link": True}]
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id and scheme_account.pll_links == pll_links
    return scheme_account


@then(parsers.parse('verify that the PLL links are deleted from the scheme account for "{journey_type2}"'))
def verify_pll_links_scheme_account(journey_type2):
    scheme_account = QueryHermes.fetch_scheme_account(journey_type2, TestContext.current_scheme_account_id)
    assert scheme_account.id == TestContext.current_scheme_account_id
    assert scheme_account.pll_links == []


def json_compare_wallet(actual_view_wallet_field, expected_view_wallet_field):
    compare = DeepDiff(
        actual_view_wallet_field, expected_view_wallet_field, ignore_order=True,
        exclude_paths=["root['loyalty_cards'][0]['balance']['updated_at']",
                       "root['loyalty_cards'][1]['balance']['updated_at']"])
    return compare


@then(parsers.parse("I can see all Wallet fields successfully"))
def verify_view_wallet_fields():
    difference = json_compare_wallet(TestContext.actual_view_wallet_field, TestContext.expected_view_wallet_field)
    if json.dumps(difference) != "{}":
        logging.info(
            "The expected and actual wallets"
            + "has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual wallet is not the same")
    else:
        logging.info("The expected and actual wallet is same")


@when(parsers.parse('I perform GET request to view loyalty card balance for "{merchant}" with "{balance}"'))
def verify_loyalty_card_balance(env, channel, merchant, balance):
    time.sleep(7)
    response = MembershipCards.get_loyalty_balance(TestContext.token, TestContext.current_scheme_account_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.current_balance = response_json.get("current_display_value")
    logging.info(
        "The response of GET loyaltycard/balance is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_BALANCE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response_json["balance"]["current_display_value"] == balance


@when(parsers.parse('I perform GET request to view loyalty card balance for "{merchant}" with invalid token'))
def verify_loyalty_card_invalid_token_balance(env, channel, merchant):
    response = MembershipCards.get_loyalty_balance(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/balance with invalid token is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_BALANCE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(
    parsers.parse('I perform GET request to view loyalty card balance for "{merchant}" with invalid id "{invalid_id}"')
)
def verify_loyalty_card_invalid_id_balance(env, channel, merchant, invalid_id):
    response = MembershipCards.get_loyalty_balance(TestContext.token, invalid_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/balance with invalid id is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_BALANCE.format(invalid_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(
    parsers.parse(
        'I perform GET request to view loyalty card transactions for "{merchant}" '
        'with "{transaction0}" "{transaction1}" and "{transaction3}"'
    )
)
def verify_loyalty_card_transactions(env, channel, merchant, transaction0, transaction1, transaction3):
    time.sleep(4)
    response = MembershipCards.get_loyalty_transactions(TestContext.token, TestContext.current_scheme_account_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/transactions is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_TRANSACTIONS.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response_json["transactions"][0]["display_value"] == transaction0
    assert response_json["transactions"][1]["display_value"] == transaction1
    assert response_json["transactions"][3]["display_value"] == transaction3


@when(parsers.parse('I perform GET request to view loyalty card transactions for "{merchant}" with invalid token'))
def verify_loyalty_card_invalid_token_transactions(env, channel, merchant):
    response = MembershipCards.get_loyalty_transactions(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/transactions with invalid token is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_TRANSACTIONS.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(
    parsers.parse(
        "I perform GET request to view loyalty card transactions" ' for "{merchant}" with invalid id "{invalid_id}"'
    )
)
def verify_loyalty_card_invalid_id_transactions(env, channel, merchant, invalid_id):
    response = MembershipCards.get_loyalty_transactions(TestContext.token, invalid_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/transactions with invalid id is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_TRANSACTIONS.format(invalid_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(
    parsers.parse(
        "I perform GET request to view loyalty card vouchers "
        'for "{merchant}" with "{state}", "{progress_display_text}", '
        '"{current_value}", "{target_value}", "{suffix}" and "{barcode_type}"'
    )
)
def verify_loyalty_card_vouchers(
    env, channel, merchant, state, progress_display_text, current_value, target_value, suffix, barcode_type
):
    time.sleep(3)
    response = MembershipCards.get_loyalty_vouchers(TestContext.token, TestContext.current_scheme_account_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/vouchers is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_VOUCHERS.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response_json["vouchers"][0]["state"] == state
    assert response_json["vouchers"][0]["progress_display_text"] == progress_display_text
    assert response_json["vouchers"][0]["current_value"] == current_value
    assert response_json["vouchers"][0]["target_value"] == target_value
    assert response_json["vouchers"][0]["suffix"] == suffix
    assert response_json["vouchers"][0]["prefix"] is None
    assert response_json["vouchers"][0]["barcode_type"] == int(
        barcode_type
    ), "actual and expected barcode type is not matching"


@when(parsers.parse('I perform GET request to view loyalty card vouchers for "{merchant}" with invalid token'))
def verify_loyalty_card_invalid_token_vouchers(env, channel, merchant):
    response = MembershipCards.get_loyalty_vouchers(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/vouchers with invalid token is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_VOUCHERS.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(
    parsers.parse(
        'I perform GET request to view loyalty card vouchers for "{merchant}" with' ' invalid id "{invalid_id}"'
    )
)
def verify_loyalty_card_invalid_id_vouchers(env, channel, merchant, invalid_id):
    response = MembershipCards.get_loyalty_vouchers(TestContext.token, invalid_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/vouchers with invalid id is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_VOUCHERS.format(invalid_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")


@when(parsers.parse("I perform GET request to view '{Wallet}'"))
def verify_view_wallet(Wallet, env, channel):
    if Wallet == "Wallet":
        response = MembershipCards.get_view_wallet(setup_third_token())
        logging.info("The response of Wallet is : \n" + json.dumps(response_to_json(response), indent=4))
        with open(TestData.get_expected_view_wallet_json(env, channel)) as json_file:
            json_data = json.load(json_file)
    else:
        response = MembershipCards.get_view_wallet_overview(setup_third_token())
        logging.info("The response of Wallet overview is : \n" + json.dumps(response_to_json(response), indent=4))
        with open(TestData.get_expected_view_wallet_overview_json(env)) as json_file:
            json_data = json.load(json_file)

    TestContext.response_status_code = response.status_code
    stored_json = json.dumps(json_data)
    TestContext.expected_view_wallet_field = json.loads(stored_json)
    TestContext.actual_view_wallet_field = response.json()


@when(parsers.parse("I perform GET request to view wallet overview with empty list"))
def verify_empty_list_wallet_overview():
    response = MembershipCards.get_view_wallet_overview(TestContext.token)
    TestContext.response_status_code = response.status_code

    response_json = response_to_json(response)
    logging.info(response_json)
    TestContext.response_join = response_json.get("joins")
    TestContext.response_loyalty_card = response_json.get("loyalty_cards")
    TestContext.response_payment_account = response_json.get("payment_accounts")


@when(parsers.parse("I perform GET request to view '{endpoint}' with invalid token"))
def verify_wallet_with_invalid_token(endpoint):
    if endpoint == "Wallet":
        response = MembershipCards.get_view_wallet(TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN))
        logging.info(
            "The response of GET/wallet with invalid token is: \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_WALLET
            + "\n\n"
            + json.dumps(response.json(), indent=4)
        )
    else:
        response = MembershipCards.get_view_wallet_overview(
            TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN)
        )
        logging.info(
            "The response of GET/wallet_overview with invalid token is: \n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_WALLET_OVERVIEW
            + "\n\n"
            + json.dumps(response.json(), indent=4)
        )

    TestContext.response_status_code = response.status_code
    response_json = response.json()

    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when(
    parsers.parse(
        'I perform POST request again to verify the "{merchant}" membership card is already added '
        'with "{status_code}"'
    )
)
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


@when(
    parsers.parse(
        'I perform POST request to add "{merchant}" membership card with "{request_payload}" ' 'with "{status_code}"'
    )
)
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
    parsers.parse(
        'I perform POST request to add and auth "{merchant}" membership card '
        'with "{request_payload}" with "{status_code}"'
    )
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


@when(
    parsers.parse(
        'I perform POST request to add and register "{merchant}" membership card '
        'with "{request_payload}" with "{status_code}"'
    )
)
def verify_invalid_request_for_add_and_register_journey(merchant, request_payload, status_code, test_email):
    if request_payload == "invalid_request":
        response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email, request_payload)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
    elif request_payload == "invalid_json":
        response = MembershipCards.add_and_register_field_with_invalid_json(TestContext.token, merchant)
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]

    logging.info(
        "The response of Invalid Journey (POST) for Add and Register field:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    assert TestContext.response_status_code == int(status_code), "Invalid json request for " + merchant + " failed"


@when(parsers.parse('I perform POST request to add "{merchant}" membership card before register'))
def add_before_register_field_loyalty_cards(merchant):
    response = MembershipCards.add_before_register_field_only_card(TestContext.token, merchant)
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


@when(parsers.parse('I perform PUT request to register "{merchant}" above wallet only membership card'))
def verify_register_post_membership_card(merchant, test_email):
    time.sleep(2)
    response = MembershipCards.register_field_only_card(
        TestContext.token, merchant, test_email, TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Register field Journey (PUT) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Register Journey for " + merchant + " failed"


@when(parsers.parse('I perform PUT request to register "{merchant}" above wallet only membership card again'))
def verify_i_perform_register_again(merchant, test_email):
    time.sleep(3)
    response = MembershipCards.register_field_only_card(
        TestContext.token, merchant, test_email, TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json["error_message"]
    TestContext.error_slug = response_json["error_slug"]
    logging.info(
        "The response of Register field Journey (PUT) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 409, "Register Journey for " + merchant + " failed"


@when(
    parsers.parse(
        'I perform PUT request to register "{merchant}" membership card with "{request_payload}" with "{status_code}"'
    )
)
def verify_register_invalid_data(merchant, test_email, request_payload, status_code):
    if request_payload == "invalid_request":
        response = MembershipCards.register_field_only_card(
            TestContext.token, merchant, test_email, TestContext.current_scheme_account_id, request_payload
        )
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        logging.info(
            "The response of Invalid request Journey (PUT) for Register field:\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )
    elif request_payload == "invalid_json":
        response = MembershipCards.register_field_with_invalid_json(
            TestContext.token, merchant, test_email, TestContext.current_scheme_account_id, request_payload
        )
        response_json = response_to_json(response)
        TestContext.response_status_code = response.status_code
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        logging.info(
            "The response of Invalid json Journey (POST) for Register field:\n \n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )

    assert TestContext.response_status_code == int(status_code), "Invalid json request for " + merchant + " failed"


@when(
    parsers.parse(
        'I perform PUT request to register "{merchant}" membership card ' "with invalid token and bearer prefix"
    )
)
def verify_invalid_token_bearer_prefix_for_register_membership_card(merchant, test_email):
    response = MembershipCards.register_field_only_card(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN),
        merchant,
        test_email,
        TestContext.current_scheme_account_id,
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of PUT/Register Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@then(parsers.parse('I see a "{error_message}" error message'))
def verify_error_message(error_message):
    assert TestContext.error_message == error_message, "Error Message didnt returned"


@then(parsers.parse('I see a "{error_slug}" error slug'))
def verify_error_slug(error_slug):
    assert TestContext.error_slug == error_slug, "Error Slug didnt returned"


@when(parsers.parse("I perform POST {merchant} membership_card request with invalid token and bearer prefix"))
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


@then(parsers.parse("I see a {status_code_returned}"))
def verify_membership_card_status_code(status_code_returned):
    assert TestContext.response_status_code == int(status_code_returned)


@then(parsers.parse("I see '{journey}' list appearing"))
def verify_wallet_join(journey):
    if journey == "join":
        assert TestContext.response_join == []
    elif journey == "loyalty_card":
        assert TestContext.response_loyalty_card == []
    else:
        assert TestContext.response_payment_account == []


@when(parsers.parse('I perform POST request to add and authorise "{merchant}" membership card'))
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


@when(parsers.parse('I perform POST request to add and authorise "{merchant}" membership card using b2b token'))
def verify_add_and_auth_b2b(merchant):
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
    parsers.parse(
        'I perform POST request to add and authorise "{merchant}" membership card with transactions and vouchers'
    )
)
def verify_add_and_auth_transactions(merchant):
    time.sleep(3)
    response = MembershipCards.add_and_authorise_transactions_card(TestContext.token, merchant)
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
    parsers.parse(
        'I perform POST request again with add and authorise to verify the "{merchant}" '
        'membership card is already added with "{status_code_returned}"'
    )
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


@when(
    parsers.parse(
        "I perform POST {merchant} membership_card request for add and auth " "with invalid token and bearer prefix"
    )
)
def verify_add_and_auth_invalid_token_request(merchant):
    response = MembershipCards.add_and_authorise_card(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), merchant
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when(
    parsers.parse(
        "I perform POST {merchant} membership_card request for add and register " "with invalid token and bearer prefix"
    )
)
def verify_add_and_register_invalid_token_request(merchant, test_email):
    response = MembershipCards.add_and_register_field(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), merchant, test_email
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of POST/Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when(parsers.parse('I perform PUT request to authorise "{merchant}" above wallet only membership card'))
def verify_authorise_post_membership_card(merchant):
    time.sleep(2)
    response = MembershipCards.authorise_field_only_card(
        TestContext.token, merchant, TestContext.current_scheme_account_id
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Authorise field Journey (PUT) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Authorised Journey for " + merchant + " failed"


@when(
    parsers.parse(
        "I perform PUT {merchant} membership_card request with invalid token and bearer "
        "prefix for authorise membership card"
    )
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
        "The response of PUT/Authorise Membership_card with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_payment_card_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401, "Server error"
    return response


@when(
    parsers.parse(
        'I perform PUT request to authorise "{merchant}" membership card with '
        '"{request_payload}" with "{status_code}"'
    )
)
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
            "The response of Invalid request Journey (PUT) for Authorise field:\n \n"
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


@then(parsers.parse('I perform DELETE request to delete the "{merchant}" membership card with invalid token'))
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


@then(parsers.parse('I perform DELETE request with payload for "{merchant}"'))
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
        + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 404, "Server error"
    return response


@when(parsers.parse('I perform PUT request to authorise "{merchant}" above wallet only membership card again'))
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
    parsers.parse(
        'I perform POST request to add and authorise "{merchant}" membership card '
        "which already exist with add credentail"
    )
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


@when(parsers.parse('I perform POST request to add and register "{merchant}" membership card'))
def add_and_register_field(merchant, test_email):
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Add and Register field Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Add and Register Journey for " + merchant + " failed"


@when(
    parsers.parse(
        'I perform POST request to add and register "{merchant}" membership card where ' "membership card is in pending"
    )
)
def add_and_register_field_for_in_pending_state_scheme(merchant, test_email):
    time.sleep(4)
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
    response_json = response_to_json(response)
    logging.info(response_json)
    # TestContext.current_scheme_account_id = response_json.get("id")
    # TestContext.response_status_code = response.status_code
    # logging.info(
    #     "The response of Add and Register field Journey (POST) where scheme is in pending:\n\n"
    #     + Endpoint.BASE_URL
    #     + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
    #     + "\n\n"
    #     + json.dumps(response_json, indent=4)
    # )
    # assert response.status_code == 200, "Add and Register Journey which is in pending " + merchant + " failed"


@when(parsers.parse('I perform POST request to add and authorise "{merchant}" with different auth credential'))
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


@when(parsers.parse('I perform POST request to add a new "{payment_card_provider}" payment account to wallet'))
def verify_pll_authorise(payment_card_provider):
    test_paymentcard_account.add_payment_account(payment_card_provider)


@when(
    parsers.parse(
        'I perform POST request again with add and register to verify the "{merchant}"'
        ' membership card is already added with "{status_code_returned}"'
    )
)
def add_and_register_with_existing_credential(merchant, status_code_returned, test_email):
    time.sleep(3)
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")
    logging.info(
        "The response of Add and Register existing scheme Journey (POST) is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert TestContext.response_status_code == int(status_code_returned), (
        "Add and register with existing Journey for " + merchant + " failed"
    )


@when(parsers.parse('I update the membership card to "{status}" pending in DB'))
def update_scheme_status(status):
    scheme_account = QueryHermes.update_scheme_account(TestContext.current_scheme_account_id, status)
    logging.info(scheme_account)
    assert scheme_account.id == TestContext.current_scheme_account_id and scheme_account.status == int(status)


@when(parsers.parse('I perform POST request to join "{merchant}" membership card'))
def join_scheme(merchant, test_email):
    response = MembershipCards.join_field(TestContext.token, merchant, test_email)
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Join Journey (POST) for "
        + merchant
        + " is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Join Journey for " + merchant + " failed"


@when(
    parsers.parse(
        'I perform POST request to join "{merchant}" membership card with "{request_payload}" with "{status_code}"'
    )
)
def perform_join_with_bad_request(merchant, request_payload, status_code, test_email):
    response = MembershipCards.join_field(TestContext.token, merchant, test_email, request_payload)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    TestContext.error_message = response_json["error_message"]
    TestContext.error_slug = response_json["error_slug"]

    logging.info(
        "The response of"
        + request_payload
        + "Invalid Journey (POST) for join journey:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    assert TestContext.response_status_code == int(status_code), "Invalid request for " + merchant + "failed"


@when(parsers.parse('I perform POST request to join "{merchant}" with invalid token'))
def join_with_invalid_token(merchant, test_email):
    response = MembershipCards.join_field(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), merchant, test_email
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of join journey for POST/join with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 401
    return response


@when(parsers.parse('I perform fail POST request to join "{merchant}" membership card'))
def fail_join_scheme(merchant):
    response = MembershipCards.join_field(
        TestContext.token, merchant, TestDataUtils.TEST_DATA.harvey_nichols_invalid_data.get(constants.ID)
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of Enrol with failed Journey (POST) for "
        + merchant
        + " is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Join Journey for " + merchant + " failed"


@when(parsers.parse('I perform DELETE request to delete the "{scheme_state}" membership card for "{merchant}"'))
def delete_failed_scheme_account(scheme_state, merchant):
    time.sleep(5)
    response_del_schemes = MembershipCards.delete_fail_scheme_account(
        TestContext.token, TestContext.current_scheme_account_id
    )
    TestContext.response_status_code = response_del_schemes.status_code

    if scheme_state == "fail":
        assert response_del_schemes.status_code == 200, "Enrol Journey for " + merchant + " failed"
    else:
        response_json = response_to_json(response_del_schemes)
        TestContext.error_message = response_json["error_message"]
        TestContext.error_slug = response_json["error_slug"]
        assert response_del_schemes.status_code == 409, "Enrol Journey for " + merchant + " failed"


@when(parsers.parse('I perform DELETE request to delete the membership card for "{merchant}" with invalid token'))
def delete_fail_scheme_with_invalid_token(merchant):
    response = MembershipCards.delete_fail_scheme_account(
        TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN), TestContext.current_scheme_account_id
    )

    TestContext.response_status_code = response.status_code
    response_json = response.json()
    logging.info(
        "The response of delete failed scheme for with invalid token is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")
    assert response.status_code == 401
    return response


@when(parsers.parse("I perform DELETE request to delete the failed membership card which is already deleted"))
def delete_failed_scheme_again():
    time.sleep(4)
    response = MembershipCards.delete_fail_scheme_account(TestContext.token, TestContext.current_scheme_account_id)
    TestContext.response_status_code = response.status_code
    response_json = response_to_json(response)
    logging.info(
        "The response of DELETE/Membership_card with Already Deleted membership card is: \n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")

    assert response.status_code == 404, "Server error"
    return response


@when(parsers.parse('I perform POST request to join in progress "{merchant}" membership card'))
def delete_join_in_progress_scheme(merchant):
    response = MembershipCards.join_field(
        TestContext.token, merchant, TestDataUtils.TEST_DATA.harvey_nichols_invalid_data.get(constants.SLOW_JOIN_ID)
    )
    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of scheme stayed Join in progress for "
        + merchant
        + " is:\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Join Journey for " + merchant + " failed"
