import json
import logging
import time

from pytest_bdd import parsers, scenarios, then, when

from tests.helpers.database.query_harmonia import QueryHarmonia
from tests.helpers.test_context import TestContext
from tests.helpers.test_transaction_matching_context import (
    TestTransactionMatchingContext,
)
from tests.requests.transaction_matching_merchant_requests import (
    upload_retailer_file_into_blob,
)
from tests.requests.transaction_matching_payment_requests import (
    import_payment_file_into_harmonia,
    import_payment_file_with_duplicate_txn,
    verify_deduped_transaction,
    verify_exported_transaction,
)
from tests.step_definitions import test_loyalty_cards, test_paymentcard_account

scenarios("transaction_matching/")

"""Step definitions - Transaction Matching """


@when(
    parsers.parse(
        "I perform POST request to add a {payment_status} {payment_card_provider} " "payment account to wallet"
    )
)
def add_payment_card(payment_card_provider, payment_status):
    test_paymentcard_account.add_payment_account(payment_card_provider, payment_status)


@when(parsers.parse("I perform POST request to add and authorise {merchant} membership card"))
def add_membership_card(merchant):
    test_loyalty_cards.verify_add_and_auth(merchant)


@when(parsers.parse('I perform POST request to add and authorise "{merchant}" membership card with {card}'))
def verify_add_and_auth_transactions(merchant, card):
    test_loyalty_cards.verify_add_and_auth_transactions(merchant, card)


@when(parsers.parse("And I perform GET {wallet}"))
def verify_wallet(wallet, env, channel):
    test_loyalty_cards.verify_wallet(wallet, env, channel)


@when(parsers.parse("I send Payment Transaction File with {payment_card_transaction} {mid}"))
@when(parsers.parse("I send Payment Transaction File with {payment_card_transaction} and MID as {mid}"))
def import_payment_file(payment_card_transaction, mid):
    TestTransactionMatchingContext.mid = mid
    response = import_payment_file_into_harmonia(payment_card_transaction, mid)
    logging.info("Waiting for transaction to be exported")
    try:
        response_json = response.json()
        logging.info("The response of POST/import Payment File is: \n\n" + json.dumps(response_json, indent=4))
        assert response.status_code == 201 or 200, "Payment file import is not successful"
        """The export time is different for various retailers"""
        time.sleep(60)
    except AttributeError:
        if response is None:
            logging.info(
                "The Master Card Settlement Transaction Text file is uploaded to blob. "
                "Waiting for transaction to be exported"
            )


"""Dedupe transactions before exporting
this is currently a requirement for the works only"""


@when(parsers.parse("I send Payment File with a duplicate transaction using {payment_card_transaction} and {mid}"))
def import_payment_file_with_duplicate_transaction(payment_card_transaction, mid):
    TestTransactionMatchingContext.mid = mid
    response = import_payment_file_with_duplicate_txn(
        payment_card_transaction,
        mid,
    )
    try:
        response_json = response.json()
        logging.info("The response of POST/import Payment File is: \n\n" + json.dumps(response_json, indent=4))
        assert response.status_code == 201 or 200, "Payment file import is not successful"
        """Master card File import or Retailer Transaction File import can
        take up to a minute to transfer from blob storage to harmonia"""
        time.sleep(60)
    except AttributeError:
        if response is None:
            logging.info(
                "The Master Card Settlement Transaction Text file is uploaded to blob. "
                "Waiting for transaction to be exported"
            )


@then(parsers.parse("I verify the reward transaction is exported using {transaction_matching_logic}"))
def verify_exported_transactions(transaction_matching_logic):
    logging.info("Transaction Export:\n")
    matched_transaction = verify_exported_transaction(transaction_matching_logic)

    logging.info(
        "Details of the recent transaction in export_transaction table:\n\n"
        f"provider slug           : {matched_transaction.provider_slug}"
        + f"\ntransaction_date        : {matched_transaction.transaction_date.__str__()}"
        + f"\namount                  : {matched_transaction.spend_amount}"
        + f"\nloyalty_id              : {matched_transaction.loyalty_id}"
        + f"\nmid                     : {matched_transaction.mid}"
        + f"\nscheme_account_id       : {matched_transaction.scheme_account_id}"
        + f"\nstatus                  : {matched_transaction.status}"
        + f"\nfeed_type               : {matched_transaction.feed_type}"
        + f"\npayment_card_account_id : {matched_transaction.payment_card_account_id}"
        + f"\nauth_code               : {matched_transaction.auth_code}"
        + f"\napproval_code           : {matched_transaction.approval_code}"
        + f"\npayment_provider_slug   : {matched_transaction.payment_provider_slug}"
        + f"\nprimary_identifier      : {matched_transaction.primary_identifier}"
        + f"\nexport_uid              : {matched_transaction.export_uid}"
    )

    assert (
        matched_transaction.status == "EXPORTED"
        and matched_transaction.mid == TestTransactionMatchingContext.mid
        and matched_transaction.scheme_account_id == TestContext.current_scheme_account_id
    ), "Transaction is present in transaction_export table, but is not successfully exported"


"""clearing the values at the end of tests to support e2e tests"""
TestTransactionMatchingContext.transaction_id = ""
TestTransactionMatchingContext.spend_amount = " "


@then(parsers.parse("I verify the reward transaction is de-duplicated using dedupe and spotting"))
def verify_transaction_dedupe():
    logging.info("Transaction Export:\n")
    deduped_transaction = verify_deduped_transaction()
    logging.info(
        "Details of the recent transaction in export_transaction table:\n\n"
        f"\nstatus                  : {deduped_transaction.status}"
        + f"\nprovider slug           : {deduped_transaction.provider_slug}"
        + f"\ntransaction_date        : {deduped_transaction.transaction_date.__str__()}"
        + f"\namount                  : {deduped_transaction.spend_amount}"
        + f"\nloyalty_id              : {deduped_transaction.loyalty_id}"
        + f"\nmid                     : {deduped_transaction.mid}"
        + f"\nscheme_account_id       : {deduped_transaction.scheme_account_id}"
        + f"\nfeed_type               : {deduped_transaction.feed_type}"
        + f"\npayment_card_account_id : {deduped_transaction.payment_card_account_id}"
        + f"\nauth_code               : {deduped_transaction.auth_code}"
        + f"\napproval_code           : {deduped_transaction.approval_code}"
        + f"\npayment_provider_slug   : {deduped_transaction.payment_provider_slug}"
        + f"\nprimary_identifier      : {deduped_transaction.primary_identifier}"
        + f"\nexport_uid              : {deduped_transaction.export_uid}"
    )

    assert (
        deduped_transaction.status == "PENDING"
        and deduped_transaction.mid == TestTransactionMatchingContext.mid
        and deduped_transaction.scheme_account_id == TestContext.current_scheme_account_id
    ), "Transaction is present in transaction_export table, but is not successfully exported"


@then(parsers.parse("I verify transaction is not streamed and exported"))
@then(parsers.parse("I verify transaction is not spotted and exported"))
@then(parsers.parse("I verify transaction is not exported"))
def verify_transaction_not_matched():
    matched_count = QueryHarmonia.fetch_match_transaction_count_invalid_mid(
        TestTransactionMatchingContext.transaction_matching_id,
        (TestTransactionMatchingContext.transaction_matching_amount * 100),
    )
    assert matched_count.count == 0, (
        f"Transaction didn't match and the exported transaction count" f" is '{matched_count.count}'"
    )
    logging.info(f" Transaction not matched and the exported transaction count is'{matched_count.count}'")


@then(parsers.parse("I verify transaction is not streamed/spotted and exported"))
def verify_transaction_not_spotted():
    spotted_transaction_count = QueryHarmonia.fetch_spotted_transaction_count(
        TestTransactionMatchingContext.transaction_id
    )
    assert spotted_transaction_count.count == 0, "The Transaction got spotted and exported"
    logging.info(f" Transaction not spotted and the status is not exported: '{spotted_transaction_count.count}'")


# @then(parsers.parse("I verify transaction is imported into the import_transaction table"))
# def verify_transaction_is_imported():
#     imported_transaction_count = QueryHarmonia.fetch_imported_transaction_count(
#         TestTransactionMatchingContext.transaction_id
#     )
#     assert impod_transaction_count.count == 1, "The Transaction is not imported into the import_transaction table"
#     logging.info(f" Transaction is imported into the import_transaction table: '{imported_transaction_count}'")


@when(
    parsers.parse(
        'Send Retailer Transaction File with "{retailer_scheme}" "{payment_card_provider}" and "{retailer_location_id}"'
    )
)
def import_merchant_file(retailer_scheme: str, payment_card_provider: str, retailer_location_id: str) -> None:
    upload_retailer_file_into_blob(retailer_scheme, payment_card_provider, retailer_location_id)
