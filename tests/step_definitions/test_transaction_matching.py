import json
import logging
import time
from datetime import datetime

import pytz
from pytest_bdd import parsers, scenarios, then, when
from tests.requests.transaction_matching_payment_cards import  TransactionMatching
from tests.step_definitions import test_loyalty_cards, test_paymentcard_account
from tests.helpers.test_transaction_matching_context import TestTransactionMatchingContext
from tests.helpers.database.query_harmonia import QueryHarmonia



scenarios("transaction_matching/")

"""Step definitions - Transaction Matching """

@when(
    parsers.parse(
        'I perform POST request to add a {payment_status} "{payment_card_provider}" ' "payment account to wallet"
    )
)
def add_payment_card(payment_card_provider, payment_status):
    test_paymentcard_account.add_payment_account(payment_card_provider, payment_status)

@when(parsers.parse('I perform POST request to add and authorise "{merchant}" membership card'))
def add_membership_card(merchant):
    test_loyalty_cards.verify_add_and_auth(merchant)

@when(parsers.parse('I send matching "{payment_card_transaction}" "{mid}" Authorisation'))
def import_payment_file(payment_card_transaction, mid):

    response = TransactionMatching.import_payment_file(payment_card_transaction,mid)
    response_json = response.json()
    logging.info("The response of POST/import Payment File is: \n\n" + json.dumps(response_json, indent=4))
    assert response.status_code == 201 or 200, "Payment file is not successful"
    return response_json

@then(parsers.parse('I verify "{payment_card_transaction}","{mid}" and "{auth_code}" is spotted and exported'))
def verify_spotted_mastercard_transaction(payment_card_transaction, mid, auth_code):
        transaction_id = TestTransactionMatchingContext.third_party_id
        if payment_card_transaction == "master-auth-spotting":
            logging.info(f"Third_party_id: '{transaction_id}'")
            spotted_transaction_count = QueryHarmonia.fetch_auth_mastercard_spotted_transaction_count(
                TestTransactionMatchingContext.spend_amount, transaction_id)
            assert spotted_transaction_count.count == 1, "Transaction not spotted and the status is not exported"
            logging.info(f"The Transaction got spotted and exported : '{spotted_transaction_count.count}'")

        elif payment_card_transaction == "master-settlement-spotting":
            t = str(TestTransactionMatchingContext.created_at)
            form = '%Y-%m-%dT%H:%M:%S.%f%z'
            utc_time = datetime.strptime(t, form)
            created_at = utc_time.astimezone(pytz.UTC)
            logging.info(f"Transaction time: '{created_at}'")
            spotted_transaction_count = QueryHarmonia.fetch_mastercard_spotted_transaction_count(
                TestTransactionMatchingContext.spend_amount, created_at)
            assert spotted_transaction_count.count == 1, "Transaction not spotted and the status is not exported"
            logging.info(f"The Transaction got spotted and exported : '{spotted_transaction_count.count}'")

        elif payment_card_transaction == "master-refund-spotting":
            t = str(TestTransactionMatchingContext.created_at)
            form = '%Y-%m-%dT%H:%M:%S.%f%z'
            utc_time = datetime.strptime(t, form)
            created_at = utc_time.astimezone(pytz.UTC)
            logging.info(f"Transaction time: '{created_at}'")
            spotted_transaction_count = QueryHarmonia.fetch_mastercard_spotted_transaction_count(
                TestTransactionMatchingContext.spend_amount, created_at)
            assert spotted_transaction_count.count == 1, "Transaction not spotted and the status is not exported"
            logging.info(f"The Transaction got spotted and exported : '{spotted_transaction_count.count}'")

        else:
            spotted_transaction_count = QueryHarmonia.fetch_spotted_transaction_count(
                TestTransactionMatchingContext.transaction_id
            )
            assert spotted_transaction_count.count == 1, "Transaction not spotted and the status is not exported"
            logging.info(f"The Transaction got spotted and exported : '{spotted_transaction_count.count}'")

