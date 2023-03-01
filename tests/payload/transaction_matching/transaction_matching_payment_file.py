import random
import string
import uuid
from pytz import timezone

from tests.helpers.test_context import TestContext
from tests.helpers.test_helpers import PaymentCardTestData
import tests.helpers.constants as constants
from tests.helpers.test_transaction_matching_context import TestTransactionMatchingContext
from datetime import date
from datetime import datetime
import typing as t

WidthField = t.Tuple[t.Any, int]


def join(*args: WidthField) -> str:
    return "".join(str(value).ljust(length) for value, length in args)


def get_data_to_import():
    TestTransactionMatchingContext.spend_amount = random.choice(range(1, 20)) / 100
    TestTransactionMatchingContext.transaction_id = (
        TransactionMatchingPaymentFileDetails.get_random_alphanumeric_string(48)
    )
    TestTransactionMatchingContext.transaction_auth_code = random.randint(100000, 999999)
    TestTransactionMatchingContext.current_time_stamp = datetime.now(timezone("Europe/London")).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


class TransactionMatchingPaymentFileDetails:

    @staticmethod
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = "".join((random.choice(letters_and_digits) for i in range(length)))
        return result_str

    @staticmethod
    def get_visa_spotting_merchant_auth_data(mid):
        return {
            "CardId": TestTransactionMatchingContext.transaction_id,
            "ExternalUserId": TestContext.payment_card_token,
            "MessageElementsCollection": [
                {"Key": "Transaction.MerchantCardAcceptorId", "Value": mid},
                {"Key": "Transaction.MerchantAcquirerBin", "Value": "3423432"},
                {"Key": "Transaction.TransactionAmount", "Value": TestTransactionMatchingContext.spend_amount},
                {"Key": "Transaction.VipTransactionId", "Value": TestTransactionMatchingContext.transaction_id},
                {"Key": "Transaction.VisaMerchantName", "Value": ""},
                {"Key": "Transaction.VisaMerchantId", "Value": ""},
                {"Key": "Transaction.VisaStoreName", "Value": ""},
                {"Key": "Transaction.VisaStoreId", "Value": ""},
                {"Key": "Transaction.CurrencyCodeNumeric", "Value": "840"},
                {"Key": "Transaction.BillingCurrencyCode", "Value": "840"},
                {"Key": "Transaction.USDAmount", "Value": TestTransactionMatchingContext.spend_amount},
                {"Key": "Transaction.MerchantLocalPurchaseDate", "Value": str(date.today())},
                {"Key": "Transaction.MerchantGroup.0.Name", "Value": "SPOTTING-MERCHANT"},
                {"Key": "Transaction.MerchantGroup.0.ExternalId", "Value": "Spotting Merchant"},
                {"Key": "Transaction.AuthCode", "Value": TestTransactionMatchingContext.transaction_auth_code},
                {
                    "Key": "Transaction.PanLastFour",
                    "Value": PaymentCardTestData.get_data("visa").get(constants.LAST_FOUR_DIGITS),
                },
                {"Key": "Transaction.MerchantDateTimeGMT", "Value": TestTransactionMatchingContext.current_time_stamp},
                {"Key": "Transaction.BillingAmount", "Value": TestTransactionMatchingContext.spend_amount},
                {"Key": "Transaction.TimeStampYYMMDD", "Value": TestTransactionMatchingContext.current_time_stamp},
                {"Key": "Transaction.SettlementDate", "Value": ""},
                {"Key": "Transaction.SettlementAmount", "Value": "0"},
                {"Key": "Transaction.SettlementCurrencyCodeNumeric", "Value": "0"},
                {"Key": "Transaction.SettlementBillingAmount", "Value": "0"},
                {"Key": "Transaction.SettlementBillingCurrency", "Value": ""},
                {"Key": "Transaction.SettlementUSDAmount", "Value": "0"},
            ],
            "MessageId": str(uuid.uuid4()),
            "MessageName": "AuthMessageTest",
            "UserDefinedFieldsCollection": [{"Key": "TransactionType", "Value": "Auth"}],
            "UserProfileId": str(uuid.uuid4()),
        }
