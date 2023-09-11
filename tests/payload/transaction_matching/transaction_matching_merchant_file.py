import csv
import random
import string

from datetime import datetime
from decimal import Decimal

from pytz import timezone

from tests.helpers import constants
from tests.helpers.test_helpers import PaymentCardTestData
from tests.helpers.test_transaction_matching_context import TestTransactionMatchingContext


def get_retailer_file_data_import(file_name: str) -> None:
    TestTransactionMatchingContext.retailer_transaction_id = get_transaction_id(48)
    TestTransactionMatchingContext.transaction_matching_auth_code = random.randint(100000, 999999)
    TestTransactionMatchingContext.transaction_matching_amount = int(Decimal(str(random.choice(range(10, 1000)))))
    TestTransactionMatchingContext.transaction_matching_currentTimeStamp = datetime.now(
        timezone("Europe/London")
    ).strftime("%Y-%m-%d %H:%M:%S")
    TestTransactionMatchingContext.file_name = file_name + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"


def get_transaction_id(length: int) -> str:
    letters_and_digits = string.ascii_letters + string.digits
    result_str = "".join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def create_retailer_csv(output: any, payment_card_provider: str, retailer_location_id: str) -> None:
    """This function creates itsu retailer CSV File,
    and this needs to be updated if any other retailer comes up with Transaction Matching"""
    merchant_writer = csv.writer(output, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    merchant_writer.writerow(TestTransactionMatchingContext.itsu_file_header)
    get_retailer_file_data_import("itsu_retailer_file")
    card_identity = payment_card_provider.lower()
    merchant_writer.writerow(
        [
            TestTransactionMatchingContext.retailer_transaction_id,
            card_identity,
            # first six should be blank
            "",
            PaymentCardTestData.get_data(payment_card_provider).get(constants.LAST_FOUR_DIGITS),
            TestTransactionMatchingContext.transaction_matching_amount,
            "GBP",
            TestTransactionMatchingContext.transaction_matching_auth_code,
            TestTransactionMatchingContext.transaction_matching_currentTimeStamp,
            # mid should be blank
            "",
            retailer_location_id,
            # transaction data should be blank
            "",
            # customer id should be blank
            "",
        ]
    )
