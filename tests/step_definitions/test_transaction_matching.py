import json
import logging
import time

from pytest_bdd import parsers, scenarios, then, when

from tests.requests.transaction_matching_payment_cards import TransactionMatching
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


@when(parsers.parse("And I perform GET {wallet}"))
def verify_wallet(wallet, env, channel):
    test_loyalty_cards.verify_wallet(wallet, env, channel)


@when(parsers.parse("I send matching {payment_card_transaction} {mid} Authorisation"))
def import_payment_file(payment_card_transaction, mid):
    response = TransactionMatching.import_payment_file(payment_card_transaction, mid)
    response_json = response.json()
    logging.info("The response of POST/import Payment File is: \n\n" + json.dumps(response_json, indent=4))
    assert response.status_code == 201 or 200, "Payment file import is not successful"
    time.sleep(60)
    return response_json


@then(parsers.parse("I verify {payment_card_transaction},{mid} is spotted and exported"))
def verify_exported_transaction(payment_card_transaction, mid):
    spotted_transaction_count = TransactionMatching.exported_transaction(payment_card_transaction)
    assert spotted_transaction_count.count == 1, "Transaction not spotted and the status is not exported"
    logging.info(f"The Transaction got spotted and exported : '{spotted_transaction_count.count}'")
