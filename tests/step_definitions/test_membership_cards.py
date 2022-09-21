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
    time.sleep(1)
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


@when(parsers.parse('I perform POST request to add "{merchant}" membership card with transactions and vouchers'))
def add_field_loyalty_cards_transactions(merchant):
    time.sleep(1)
    response = MembershipCards.add_field_only_card_transactions(TestContext.token, merchant)
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
    elif journey_type == "account_already_exists":
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert (
            scheme_account.id == TestContext.current_scheme_account_id
            and scheme_account.status is TestDataUtils.TEST_DATA.scheme_status.get(constants.ACCOUNT_ALREADY_EXIST)
            or TestDataUtils.TEST_DATA.scheme_status.get(constants.ACCOUNT_ALREADY_EXIST)
        )

    elif journey_type == "unauthorised":
        if merchant == "Wasabi":
            scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
            assert (
                scheme_account.id == TestContext.current_scheme_account_id
                and scheme_account.status == TestDataUtils.TEST_DATA.scheme_status.get(constants.FAILED_VALIDATION)
            )
            print("scheme ac status", scheme_account.status)

    elif journey_type == "pll":
        pll_links = [{"id": TestContext.current_payment_card_id, "active_link": True}]
        scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
        assert scheme_account.id == TestContext.current_scheme_account_id and scheme_account.pll_links == pll_links
    return scheme_account


@then(parsers.parse('verify the payment data stored in DB after "{journey_type2}" journey for "{merchant}"'))
def verify_payment_card_into_database(journey_type2, merchant):
    pll_links = [{"id": TestContext.current_scheme_account_id, "active_link": True}]
    payment_account = QueryHermes.fetch_payment_account(TestContext.current_payment_card_id)
    assert payment_account.id == TestContext.current_payment_card_id and payment_account.pll_links == pll_links, (
        journey_type2 + " for " + merchant + " in database is not success"
    )
    return payment_account


@then(parsers.parse('verify that the PLL links are deleted from the scheme account for "{journey_type2}"'))
def verify_pll_links_scheme_account(journey_type2):
    time.sleep(5)
    scheme_account = QueryHermes.fetch_scheme_account(journey_type2, TestContext.current_scheme_account_id)
    assert scheme_account.is_delete_scheme is True
    assert scheme_account.id == TestContext.current_scheme_account_id
    assert scheme_account.pll_links == []


@then(parsers.parse('verify that the PLL links are deleted from the payment account for "{journey_type2}"'))
def verify_pll_links_payment_account(journey_type2):
    time.sleep(5)
    payment_account = QueryHermes.fetch_payment_account(TestContext.current_payment_card_id)
    assert payment_account.is_deleted is True
    assert payment_account.id == TestContext.current_payment_card_id
    assert payment_account.pll_links == []


# def json_compare_wallet(actual_view_wallet_field, expected_view_wallet_field):
#     compare = DeepDiff(
#         actual_view_wallet_field,
#         expected_view_wallet_field,
#         ignore_order=True,
#         exclude_paths=[
#             "root['loyalty_cards'][0]['balance']['updated_at']",
#             "root['loyalty_cards'][1]['balance']['updated_at']",
#         ],
#     )
#
#     return compare


def json_compare(actual_field, expected_field, paths=None):

    compare = DeepDiff(
        actual_field,
        expected_field,
        ignore_order=True,
        exclude_paths=paths,
    )

    return compare


# def json_compare_transactions(actual_transactions_field, expected_transactions_field):
#     compare = DeepDiff(
#         actual_transactions_field,
#         expected_transactions_field,
#         ignore_order=True,
#         exclude_paths=["root[0]['id']", "root[1]['id']", "root[2]['id']", "root[3]['id']", "root[4]['id']"],
#     )
#
#     return compare
#
#
# def json_compare_balance(actual_balance_field, expected_balance_field):
#     compare = DeepDiff(
#         actual_balance_field, expected_balance_field, ignore_order=True, exclude_paths=["root['updated_at']"]
#     )
#
#     return compare
#
#
# def json_compare_vouchers(actual_vouchers_field, expected_vouchers_field):
#     compare = DeepDiff(
#         actual_vouchers_field,
#         expected_vouchers_field,
#         ignore_order=True,
#      )
#
#     return compare


# @then(parsers.parse("I can see all Wallet fields successfully"))
# def verify_view_wallet_fields():
#     difference = json_compare_wallet(TestContext.actual_view_wallet_field, TestContext.expected_view_wallet_field)
#     if json.dumps(difference) != "{}":
#         logging.error(
#             "The expected and actual wallets"
#             + "has following differences"
#             + json.dumps(difference, sort_keys=True, indent=4)
#         )
#         raise Exception("The expected and actual wallet is not the same")
#     else:
#         logging.info("The expected and actual wallet is same")
#


def compare_two_lists(list1: list, list2: list) -> bool:
    """
    Compare two lists and logs the difference.
    :param list1: first list.
    :param list2: second list.
    :return:      if there is difference between both lists.
    """
    diff = [i for i in list1 + list2 if i not in list1 or i not in list2]
    result = len(diff) == 0
    if not result:
        raise Exception(f"There are differences:\n{diff}")
    return result


@then(parsers.parse("All '{Wallet}' fields are correctly populated for {merchant}"))
def verify_get_wallet_fields(Wallet, merchant):
    wallet_response = TestContext.actual_view_wallet_field
    if Wallet == "Wallet":
        assert (
            wallet_response["loyalty_cards"][0]["pll_links"][0]["payment_account_id"]
            == TestContext.current_payment_card_id
        ), "pll_links do not match"

        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.wallet_info[merchant][0].keys():
            if wallet_key not in ["balance", "transactions", "vouchers", "images"]:
                assert (
                    wallet_response["loyalty_cards"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.wallet_info[merchant][0][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for i in range(len(TestDataUtils.TEST_DATA.wallet_info[merchant][0]["transactions"])):
                    for tran_key in TestDataUtils.TEST_DATA.wallet_info[merchant][0]["transactions"][i].keys():
                        assert (
                            wallet_response["loyalty_cards"][0]["transactions"][i][tran_key]
                            == TestDataUtils.TEST_DATA.wallet_info[merchant][0]["transactions"][i][tran_key]
                        ), f"{tran_key} do not match"
                for balance_key in TestDataUtils.TEST_DATA.wallet_info[merchant][0]["balance"].keys():
                    assert (
                        wallet_response["loyalty_cards"][0]["balance"][balance_key]
                        == TestDataUtils.TEST_DATA.wallet_info[merchant][0]["balance"][balance_key]
                    ), f"{balance_key} do not match"
        compare_two_lists(
            wallet_response["loyalty_cards"][0]["vouchers"],
            TestDataUtils.TEST_DATA.wallet_info[merchant][0]["vouchers"],
        )
        compare_two_lists(
            wallet_response["loyalty_cards"][0]["images"],
            TestDataUtils.TEST_DATA.wallet_info[merchant][0]["images"],
        )

        for payment_key in TestDataUtils.TEST_DATA.wallet_info["payment_accounts"][0].keys():
            if payment_key != "images":
                assert (
                    wallet_response["payment_accounts"][0][payment_key]
                    == TestDataUtils.TEST_DATA.wallet_info["payment_accounts"][0][payment_key]
                ), f"{payment_key} do not match"
            else:
                compare_two_lists(
                    wallet_response["payment_accounts"][0]["images"],
                    TestDataUtils.TEST_DATA.wallet_info["payment_accounts"][0]["images"],
                )

    elif Wallet == "Wallet_overview":
        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.wallet_overview_info[merchant][0].keys():
            if wallet_key != "balance":
                assert (
                    wallet_response["loyalty_cards"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.wallet_overview_info[merchant][0][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for balance_key in TestDataUtils.TEST_DATA.wallet_overview_info[merchant][0]["balance"].keys():
                    assert (
                        wallet_response["loyalty_cards"][0]["balance"][balance_key]
                        == TestDataUtils.TEST_DATA.wallet_overview_info[merchant][0]["balance"][balance_key]
                    ), f"{balance_key} do not match"

        for payment_key in TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0].keys():
            if payment_key != "images":
                assert (
                    wallet_response["payment_accounts"][0][payment_key]
                    == TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0][payment_key]
                ), f"{payment_key} do not match"
            else:
                compare_two_lists(
                    wallet_response["payment_accounts"][0]["images"],
                    TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0]["images"],
                )

    elif Wallet == "Wallet_by_card_id":
        assert (
            wallet_response["pll_links"][0]["payment_account_id"] == TestContext.current_payment_card_id
        ), "pll_links do not match"

        assert wallet_response["id"] == TestContext.current_scheme_account_id, "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant].keys():
            if wallet_key not in ["balance", "transactions", "vouchers", "images"]:
                assert (
                    wallet_response[wallet_key] == TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for i in range(len(TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["transactions"])):
                    for tran_key in TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["transactions"][i].keys():
                        assert (
                            wallet_response["transactions"][i][tran_key]
                            == TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["transactions"][i][tran_key]
                        ), f"{tran_key} do not match"
                for balance_key in TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["balance"].keys():
                    assert (
                        wallet_response["balance"][balance_key]
                        == TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["balance"][balance_key]
                    ), f"{balance_key} do not match"
        compare_two_lists(
            wallet_response["vouchers"], TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["vouchers"]
        )
        compare_two_lists(wallet_response["images"], TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["images"])


@then(parsers.parse("I see {pll_linked_payment_accounts},{total_payment_accounts} and {is_fully_pll_linked}"))
def verify_wallet_overview_pll(pll_linked_payment_accounts, total_payment_accounts, is_fully_pll_linked):
    wallet_overview_response = TestContext.actual_view_wallet_field
    assert (
        str(wallet_overview_response["loyalty_cards"][0]["is_fully_pll_linked"]) == is_fully_pll_linked
    ), "is_fully_pll_linked do not match"

    assert (
        str(wallet_overview_response["loyalty_cards"][0]["pll_linked_payment_accounts"]) == pll_linked_payment_accounts
    ), "pll_linked_payment_accounts do not match"

    assert (
        str(wallet_overview_response["loyalty_cards"][0]["total_payment_accounts"]) == total_payment_accounts
    ), "pll_linked_payment_accounts do not match"


@then(parsers.parse("All voucher fields are correctly populated for {merchant}"))
def verify_voucher_field(env, channel, merchant):
    voucher_response = TestContext.actual_view_wallet_field
    compare_two_lists(voucher_response["vouchers"], TestDataUtils.TEST_DATA.wallet_info[merchant][0]["vouchers"])


@when(parsers.parse('I perform GET request to view loyalty card balance for "{merchant}"'))
def verify_loyalty_card_balance(env, channel, merchant):
    time.sleep(4)
    response = MembershipCards.get_loyalty_balance(TestContext.token, TestContext.current_scheme_account_id)
    response_json = response_to_json(response)
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response of GET loyaltycard/balance is : \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_BALANCE.format(TestContext.current_scheme_account_id)
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    difference = json_compare(
        response_json["balance"],
        TestDataUtils.TEST_DATA.wallet_info[merchant][0]["balance"],
        paths=["root['updated_at']"],
    )
    if difference:
        logging.info(
            "The expected and actual balance of "
            + merchant
            + "has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual balance of " + merchant + " is not the same")
    else:
        logging.info("The expected and actual balance of " + merchant + " is same")


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
    parsers.parse('I perform GET request to view loyalty card balance with invalid id "{invalid_id}" for "{merchant}"')
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


@when(parsers.parse('I perform GET request to view loyalty card transactions for "{merchant}"'))
def verify_loyalty_card_transactions(env, channel, merchant):
    time.sleep(6)
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
    difference = json_compare(
        response_json["transactions"],
        TestDataUtils.TEST_DATA.wallet_info[merchant][0]["transactions"],
        paths=["root[0]['id']", "root[1]['id']", "root[2]['id']", "root[3]['id']", "root[4]['id']"],
    )
    if difference:
        logging.info(
            "The expected and actual transactions of "
            + merchant
            + "has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual transactions " + merchant + " is not the same")
    else:
        logging.info("The expected and actual transactions " + merchant + " is same")


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
        'I perform GET request to view loyalty card transactions with invalid id "{invalid_id}" for "{merchant}"'
    )
)
def verify_loyalty_card_invalid_id_transactions(env, channel, invalid_id, merchant):
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


@when(parsers.parse('I perform GET request to view loyalty card voucher for "{merchant}"'))
def verify_loyalty_card_vouchers(env, channel, merchant):
    time.sleep(6)
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
    difference = json_compare(response_json["vouchers"], TestDataUtils.TEST_DATA.wallet_info[merchant][0]["vouchers"])
    if difference:
        logging.info(
            "The expected and actual vouchers of "
            + merchant
            + " has following differences"
            + json.dumps(difference, sort_keys=True, indent=4)
        )
        raise Exception("The expected and actual vouchers of  " + merchant + " is not the same")
    else:
        logging.info("The expected and actual vouchers of  " + merchant + " is same")


@when(parsers.parse('I perform GET request to view loyalty card voucher with invalid token for "{merchant}"'))
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


@when(parsers.parse('I perform GET request to view loyalty card voucher with invalid id "{invalid_id}"'))
def verify_loyalty_card_invalid_id_vouchers(env, channel, invalid_id):
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


# @when(parsers.parse("I perform GET '{Wallet}'"))
# def verify_wallet(Wallet, env, channel):
#     if Wallet == "Wallet":
#         response = MembershipCards.get_view_wallet(TestContext.token)
#         logging.info("The response of get wallet is : \n" + json.dumps(response_to_json(response), indent=4))
#         print("response of Wallet in dictionary format : \n", response_to_json(response))
#         # print("type if response.json : \n", type(response.json()))
#
#     else:
#         response = MembershipCards.get_view_wallet_overview(TestContext.token)
#         logging.info("The response of get wallet overview is : \n" + json.dumps(response_to_json(response), indent=4))
#
#     TestContext.response_status_code = response.status_code
#     TestContext.actual_view_wallet_field = response.json()

@when(parsers.parse("I perform GET '{Wallet}' for first user"))
def verify_wallet(Wallet, env, channel):
    time.sleep(5)
    if Wallet == "Wallet":
        response = MembershipCards.get_view_wallet(TestContext.first_wallet_token)
        logging.info("The response of get wallet is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_overview":
        response = MembershipCards.get_view_wallet_overview(TestContext.first_wallet_token)
        logging.info("The response of get wallet overview is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_by_card_id":
        response = MembershipCards.get_view_wallet_by_card_id(TestContext.first_wallet_token, TestContext.current_scheme_account_id)
        logging.info("The response of get wallet by card id is : \n" + json.dumps(response_to_json(response), indent=4))

    TestContext.response_status_code = response.status_code
    TestContext.actual_view_wallet_field = response.json()


@when(parsers.parse("I perform GET '{Wallet}' for second user"))
def verify_wallet(Wallet, env, channel):
    time.sleep(5)
    if Wallet == "Wallet":
        response = MembershipCards.get_view_wallet(TestContext.second_wallet_token)
        logging.info("The response of get wallet is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_overview":
        response = MembershipCards.get_view_wallet_overview(TestContext.second_wallet_token)
        logging.info("The response of get wallet overview is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_by_card_id":
        response = MembershipCards.get_view_wallet_by_card_id(TestContext.second_wallet_token, TestContext.current_scheme_account_id)
        logging.info("The response of get wallet by card id is : \n" + json.dumps(response_to_json(response), indent=4))

    TestContext.response_status_code = response.status_code
    TestContext.actual_view_wallet_field = response.json()


@when(parsers.parse("I perform GET '{Wallet}'"))
def verify_wallet(Wallet, env, channel):
    time.sleep(5)
    if Wallet == "Wallet":
        response = MembershipCards.get_view_wallet(TestContext.token)
        logging.info("The response of get wallet is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_overview":
        response = MembershipCards.get_view_wallet_overview(TestContext.token)
        logging.info("The response of get wallet overview is : \n" + json.dumps(response_to_json(response), indent=4))

    elif Wallet == "Wallet_by_card_id":
        response = MembershipCards.get_view_wallet_by_card_id(TestContext.token, TestContext.current_scheme_account_id)
        logging.info("The response of get wallet by card id is : \n" + json.dumps(response_to_json(response), indent=4))

    TestContext.response_status_code = response.status_code
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


@when(parsers.parse("I perform GET request to view '{endpoint}' with {invalid}"))
def verify_wallet_with_invalid_token(endpoint, invalid):
    if invalid == "token":
        if endpoint == "Wallet":
            response = MembershipCards.get_view_wallet(
                TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN)
            )
            logging.info(
                "The response of GET/wallet with invalid token is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_WALLET
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
        elif endpoint == "Wallet_overview":
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
        elif endpoint == "Wallet_by_card_id":
            response = MembershipCards.get_view_wallet_by_card_id(
                TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN),
                TestContext.current_scheme_account_id,
            )

        assert response.status_code == 401, "Status is not 401"
    elif invalid == "scheme_account_id" and endpoint == "Wallet_by_card_id":
        response = MembershipCards.get_view_wallet_by_card_id(
            TestContext.token, TestContext.current_scheme_account_id * 90000
        )
        assert response.status_code == 404, "Status is not 404"
    TestContext.response_status_code = response.status_code
    response_json = response.json()
    TestContext.error_message = response_json.get("error_message")
    TestContext.error_slug = response_json.get("error_slug")
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
    elif request_payload == "unauthorised":
        journey_type = request_payload
        response = MembershipCards.add_and_auth_field_with_unauthorised_json(TestContext.token, merchant)
        response_json = response_to_json(response)
        logging.info(response_json)
        TestContext.response_status_code = response.status_code
        TestContext.current_scheme_account_id = response_json.get("id")
        verify_loyalty_card_into_database(journey_type, merchant)

    logging.info(
        "The response of Invalid Journey (POST) for Add and Auth field:\n \n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )

    assert TestContext.response_status_code == int(status_code), "Invalid request for " + merchant + " failed"


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
    time.sleep(7)
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
    response = MembershipCards.register_field_only_card(
        TestContext.token, merchant, test_email, TestContext.current_scheme_account_id
    )
    time.sleep(7)
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
    TestContext.first_wallet_scheme_account_id = TestContext.current_scheme_account_id
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
    time.sleep(3)
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


@when(parsers.parse('I perform PUT request to authorise "{merchant}" wallet only membership card with '
                    'transactions and vouchers'))
def verify_authorise_post_membership_card_transactions(merchant):
    time.sleep(3)
    response = MembershipCards.authorise_field_only_card_transactions(
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
        "which already exist with add credential"
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


@when(parsers.parse("I perform POST request add and register for {merchant}"))
def add_and_register_field(merchant, test_email):
    TestContext.card_number = TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.REGISTER_CARD)
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
    time.sleep(8)
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


@when(
    parsers.parse(
        'I perform POST request to add a {payment_status} "{payment_card_provider}" payment account to wallet'
    )
)
def verify_pll_authorise(payment_card_provider, payment_status):
    test_paymentcard_account.add_payment_account(payment_card_provider, payment_status)


@when(parsers.parse('I perform POST request to add existing payment card "{payment_card_provider}" to second wallet'))
def add_existing_payment_card_in_another_wallet(payment_card_provider):
    test_paymentcard_account.add_existing_payment_card_in_another_wallet(payment_card_provider)


@when(parsers.parse("I perform POST request {journey_type} again for {merchant}"))
def add_and_register_with_existing_credential(journey_type, merchant, test_email):
    scheme_account = QueryHermes.fetch_scheme_account(journey_type, TestContext.current_scheme_account_id)
    TestContext.card_number = scheme_account.main_answer
    response = MembershipCards.add_and_register_field(TestContext.token, merchant, test_email)
    time.sleep(8)
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


@when(parsers.parse('I update the membership card to "{status}" pending in DB'))
def update_scheme_status(status):
    scheme_account = QueryHermes.update_scheme_account(TestContext.current_scheme_account_id, status)
    logging.info(scheme_account)
    assert scheme_account.id == TestContext.current_scheme_account_id and scheme_account.status == int(status)


@when(parsers.parse('I perform POST request to {join} "{merchant}" membership card'))
def join_scheme(join, merchant, test_email):
    if join == "identical_join":
        test_email = TestDataUtils.TEST_DATA.join_emails.get(constants.IDENTICAL_JOIN)
    response = MembershipCards.join_field(TestContext.token, merchant, test_email)
    time.sleep(8)
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


@when(parsers.parse('I perform {scheme_state} POST request to join "{merchant}" membership card'))
def fail_join_scheme(merchant, scheme_state):
    if scheme_state == "enrol_failed":
        response = MembershipCards.join_field(
            TestContext.token, merchant, TestDataUtils.TEST_DATA.join_emails.get(constants.ID)
        )
        time.sleep(15)
    elif scheme_state == "join_success":
        response = MembershipCards.join_field(
            TestContext.token,
            merchant,
            TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
        )
        time.sleep(15)
    elif scheme_state == "asynchronous_join_in_progress":
        response = MembershipCards.join_field(
            TestContext.token, merchant, TestDataUtils.TEST_DATA.join_emails.get(constants.SLOW_JOIN_ID)
        )

    response_json = response_to_json(response)
    TestContext.current_scheme_account_id = response_json.get("id")
    TestContext.response_status_code = response.status_code
    logging.info(
        "The response for "
        + merchant
        + " with \n\n"
        + scheme_state
        + " is :\n\n"
        + Endpoint.BASE_URL
        + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN
        + "\n\n"
        + json.dumps(response_json, indent=4)
    )
    assert response.status_code == 202, "Join Journey for " + merchant + " failed"


@when(parsers.parse('I perform DELETE request to delete the "{scheme_state}" membership card for "{merchant}"'))
def delete_failed_scheme_account(scheme_state, merchant):
    response_del_schemes = MembershipCards.delete_fail_scheme_account(
        TestContext.token, TestContext.current_scheme_account_id
    )
    TestContext.response_status_code = response_del_schemes.status_code

    if scheme_state == "enrol_failed":
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


@then(parsers.parse("I can see '{state}','{slug}' and '{description}' for loyalty card PLL links in the Wallet"))
def verify_loyalty_card_pll_status(state, slug, description):
    wallet_response = TestContext.actual_view_wallet_field
    if state == "active":
        assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["state"] == state, "pll_links do not match"
        assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["slug"] is None, "pll_links do not match"
        assert (
            wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["description"] is None
        ), "pll_links do not match"
    else:
        assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["state"] == state, "pll_links do not match"
        assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["slug"] == slug, "pll_links do not match"
        assert (
            wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["description"] == description
        ), "pll_links do not match"


@then(
    parsers.parse(
        "I can see '{state1}','{state2}','{slug1}','{slug2}','{description1}' and '{description2}' for "
        "loyalty card PLL links in the Wallet"
    )
)
def verify_loyalty_card_pll_status_UC(state1, state2, slug1, slug2, description1, description2):
    wallet_response = TestContext.actual_view_wallet_field
    assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["state"] == state2, "pll_links do not match"
    assert wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["slug"] == slug2, "pll_links do not match"
    assert (
        wallet_response["loyalty_cards"][0]["pll_links"][0]["status"]["description"] == description2
    ), "pll_links do not match"


@then(parsers.parse("I can see '{state}','{slug}' and '{description}' for payment accounts PLL links in the Wallet"))
def verify_payment_card_pll_status(state, slug, description):
    wallet_response = TestContext.actual_view_wallet_field
    if state == "active":
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["state"] == state
        ), "pll_links do not match"
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["slug"] is None
        ), "pll_links do not match"
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["description"] is None
        ), "pll_links do not match"
    else:
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["state"] == state
        ), "pll_links do not match"
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["slug"] == slug
        ), "pll_links do not match"
        assert (
            wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["description"] == description
        ), "pll_links do not match"


@then(parsers.parse("I can see '{state}','{slug}' and '{description}' in PLL links for Wallet loyalty card by id"))
def verify_wallet_loyaltycard_pll_status(state, slug, description):
    wallet_response = TestContext.actual_view_wallet_field
    if state == "active":
        assert wallet_response["pll_links"][0]["status"]["state"] == state, "pll_links do not match"
        assert wallet_response["pll_links"][0]["status"]["slug"] is None, "pll_links do not match"
        assert wallet_response["pll_links"][0]["status"]["description"] is None, "pll_links do not match"
    else:
        assert wallet_response["pll_links"][0]["status"]["state"] == state, "pll_links do not match"
        assert wallet_response["pll_links"][0]["status"]["slug"] == slug, "pll_links do not match"
        assert wallet_response["pll_links"][0]["status"]["description"] == description, "pll_links do not match"


@then(
    parsers.parse(
        "I can see '{state1}','{state2}','{slug1}','{slug2}','{description1}' and '{description2}' for "
        "payment accounts PLL links in the Wallet"
    )
)
def verify_payment_card_pll_status_UC(state1, state2, slug1, slug2, description1, description2):
    wallet_response = TestContext.actual_view_wallet_field
    assert wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["state"] == state1, "pll_links do not match"
    assert wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["slug"] is None, "pll_links do not match"
    assert (
        wallet_response["payment_accounts"][0]["pll_links"][0]["status"]["description"] is None
    ), "pll_links do not match"
    assert wallet_response["payment_accounts"][0]["pll_links"][1]["status"]["state"] == state2, "pll_links do not match"
    assert wallet_response["payment_accounts"][0]["pll_links"][1]["status"]["slug"] == slug2, "pll_links do not match"
    assert (
        wallet_response["payment_accounts"][0]["pll_links"][1]["status"]["description"] == description2
    ), "pll_links do not match"


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
        TestContext.token, merchant, TestDataUtils.TEST_DATA.join_emails.get(constants.SLOW_JOIN_ID)
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


@then(parsers.parse("Verify {Wallet} fields for {merchant} with {scheme_state}"))
def verify_state_slug_desc(Wallet, merchant, scheme_state):
    wallet_response = TestContext.actual_view_wallet_field
    if Wallet == "Wallet" and scheme_state == "join_success":
        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"
        for wallet_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state].keys():
            if wallet_key not in ["balance", "card", "images"]:
                assert (
                    wallet_response["loyalty_cards"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for balance_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["balance"].keys():
                    assert (
                        wallet_response["loyalty_cards"][0]["balance"][balance_key]
                        == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["balance"][balance_key]
                    ), f"{balance_key} do not match"
                for card_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"].keys():
                    assert (
                        wallet_response["loyalty_cards"][0]["card"][card_key]
                        == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"][card_key]
                    ), f"{card_key} do not match"
    elif Wallet in ["Wallet", "Wallet_overview"] and scheme_state == "asynchronous_join_in_progress":
        assert (
            wallet_response["joins"][0]["loyalty_card_id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state].keys():
            if wallet_key not in ["card", "images"]:
                assert (
                    wallet_response["joins"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for card_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"].keys():
                    assert (
                        wallet_response["joins"][0]["card"][card_key]
                        == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"][card_key]
                    ), f"{card_key} do not match"
    elif Wallet in ["Wallet", "Wallet_overview"] and scheme_state == "enrol_failed":
        assert (
            wallet_response["joins"][0]["loyalty_card_id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state].keys():
            if wallet_key not in ["card", "images"]:
                assert (
                    wallet_response["joins"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state][wallet_key]
                ), f"{wallet_key} do not match"
            else:
                for card_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"].keys():
                    assert (
                        wallet_response["joins"][0]["card"][card_key]
                        == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state]["card"][card_key]
                    ), f"{card_key} do not match"
    elif Wallet == "Wallet" and scheme_state == "account_already_exists":
        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"
        for wallet_key in TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state].keys():
            if wallet_key not in ["images"]:
                assert (
                    wallet_response["loyalty_cards"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.Join_Scheme_status[scheme_state][wallet_key]
                ), f"{wallet_key} do not match"
    elif Wallet == "Wallet":
        compare_two_lists(
            wallet_response["joins"][0]["images"],
            TestDataUtils.TEST_DATA.Join_Scheme_status["join_success"]["images"],
        )
    elif Wallet == "Wallet_overview":
        compare_two_lists(
            wallet_response["joins"][0]["images"],
            TestDataUtils.TEST_DATA.Join_Scheme_status["wallet_overview_image"],
        )


@when(parsers.parse("I perform put request with {request_payload} to update failed join for {merchant}"))
def verify_put_join_with_invalid(request_payload, merchant):
    if request_payload == "successful_payload":
        time.sleep(2)
        response = MembershipCards.update_failed_join(
            TestContext.token,
            merchant,
            TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
            TestContext.current_scheme_account_id,
            request_payload,
        )
        response_json = response_to_json(response)
        TestContext.current_scheme_account_id = response_json.get("id")
        TestContext.response_status_code = response.status_code
        logging.info(
            "The response of PUT/join is:\n\n"
            + Endpoint.BASE_URL
            + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(TestContext.current_scheme_account_id)
            + "\n\n"
            + json.dumps(response_json, indent=4)
        )
        assert response.status_code == 202, "Update failed join for " + merchant + " failed"
        time.sleep(12)

    else:
        if request_payload == "invalid_token":
            response = MembershipCards.update_failed_join(
                TestDataUtils.TEST_DATA.invalid_token.get(constants.INVALID_TOKEN),
                merchant,
                TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
                TestContext.current_scheme_account_id,
                request_payload,
            )
            logging.info(
                "The response of put/join with invalid token is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
            assert response.status_code == 401, "Status is not 401"
        elif request_payload == "invalid_scheme_account_id":
            response = MembershipCards.update_failed_join(
                TestContext.token,
                merchant,
                TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
                TestContext.current_scheme_account_id * 90000,
                request_payload,
            )
            logging.info(
                "The response of put/join with invalid scheme account is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
            assert response.status_code == 404, "Status is not 404"
        elif request_payload == "invalid_json":
            response = MembershipCards.update_failed_join(
                TestContext.token,
                merchant,
                TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
                TestContext.current_scheme_account_id,
                request_payload,
            )
            logging.info(
                "The response of put/join with invalid json is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
            assert response.status_code == 400, "Status is not 400"

        elif request_payload == "invalid_request":
            response = MembershipCards.update_failed_join(
                TestContext.token,
                merchant,
                TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
                TestContext.current_scheme_account_id,
                request_payload,
            )
            logging.info(
                "The response of put/join with invalid request is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
            assert response.status_code == 422, "Status is not 422"
        elif request_payload == "conflict":
            response = MembershipCards.update_failed_join(
                TestContext.token,
                merchant,
                TestDataUtils.TEST_DATA.join_emails.get(constants.SUCCESS_EMAIL),
                TestContext.current_scheme_account_id,
                request_payload,
            )
            logging.info(
                "The response of put/join with invalid scheme account is: \n\n"
                + Endpoint.BASE_URL
                + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED
                + "\n\n"
                + json.dumps(response.json(), indent=4)
            )
            assert response.status_code == 409, "Status is not 409"

        TestContext.response_status_code = response.status_code
        response_json = response.json()
        TestContext.error_message = response_json.get("error_message")
        TestContext.error_slug = response_json.get("error_slug")
    return response


@then(parsers.parse("{Wallet} fields are correctly populated for unauthorised LC of {merchant}"))
def verify_get_wallet_lc_unauath(Wallet, merchant):
    wallet_response = TestContext.actual_view_wallet_field
    if Wallet == "Wallet":
        assert (
            wallet_response["loyalty_cards"][0]["pll_links"][0]["payment_account_id"]
            == TestContext.current_payment_card_id
        ), "pll_links do not match"

        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.unauth_wallet_info[merchant][0].keys():
            if wallet_key not in ["images"]:
                assert (
                    wallet_response["loyalty_cards"][0][wallet_key]
                    == TestDataUtils.TEST_DATA.unauth_wallet_info[merchant][0][wallet_key]
                ), f"{wallet_key} do not match"

        compare_two_lists(
            wallet_response["loyalty_cards"][0]["images"],
            TestDataUtils.TEST_DATA.unauth_wallet_info[merchant][0]["images"],
        )

        for payment_key in TestDataUtils.TEST_DATA.unauth_wallet_info["payment_accounts"][0].keys():
            if payment_key != "images":
                assert (
                    wallet_response["payment_accounts"][0][payment_key]
                    == TestDataUtils.TEST_DATA.wallet_info["payment_accounts"][0][payment_key]
                ), f"{payment_key} do not match"
            else:
                compare_two_lists(
                    wallet_response["payment_accounts"][0]["images"],
                    TestDataUtils.TEST_DATA.wallet_info["payment_accounts"][0]["images"],
                )

    elif Wallet == "Wallet_overview":
        assert (
            wallet_response["loyalty_cards"][0]["id"] == TestContext.current_scheme_account_id
        ), "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.unauth_wallet_overview_info[merchant][0].keys():
            assert (
                wallet_response["loyalty_cards"][0][wallet_key]
                == TestDataUtils.TEST_DATA.unauth_wallet_overview_info[merchant][0][wallet_key]
            ), f"{wallet_key} do not match"

        for payment_key in TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0].keys():
            if payment_key != "images":
                assert (
                    wallet_response["payment_accounts"][0][payment_key]
                    == TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0][payment_key]
                ), f"{payment_key} do not match"
            else:
                compare_two_lists(
                    wallet_response["payment_accounts"][0]["images"],
                    TestDataUtils.TEST_DATA.wallet_overview_info["payment_accounts"][0]["images"],
                )

    elif Wallet == "Wallet_by_card_id":
        assert (
            wallet_response["pll_links"][0]["payment_account_id"] == TestContext.current_payment_card_id
        ), "pll_links do not match"

        assert wallet_response["id"] == TestContext.current_scheme_account_id, "account id does not match"

        for wallet_key in TestDataUtils.TEST_DATA.unauth_wallet_info_by_card_id[merchant].keys():
            if wallet_key not in ["images"]:
                assert (
                    wallet_response[wallet_key]
                    == TestDataUtils.TEST_DATA.unauth_wallet_info_by_card_id[merchant][wallet_key]
                ), f"{wallet_key} do not match"
        compare_two_lists(wallet_response["images"], TestDataUtils.TEST_DATA.wallet_info_by_card_id[merchant]["images"])


