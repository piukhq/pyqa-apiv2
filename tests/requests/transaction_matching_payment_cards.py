import json
import logging

import tests.api as api

from tests.api.base import Endpoint
from tests.api.transactionmatching_base import TransactionMatchingEndpoint
from tests.helpers.database.query_harmonia import QueryHarmonia
from tests.helpers.test_transaction_matching_context import TestTransactionMatchingContext
from tests.payload.transaction_matching.transaction_matching_payment_file import (
    TransactionMatchingPaymentFileDetails,
    get_data_to_import,
)


class TransactionMatching:
    @staticmethod
    def get_visa_spotting_merchant_auth_file(mid):
        get_data_to_import()
        url = TransactionMatching.get_visa_url()
        logging.info(url)
        header = TransactionMatchingEndpoint.request_header_visa()
        payload = TransactionMatchingPaymentFileDetails.get_visa_spotting_merchant_auth_data(mid)
        response = Endpoint.call(url, header, "POST", payload)
        print(json.dumps(payload, indent=4))
        return response

    @staticmethod
    def get_visa_url():
        return TransactionMatchingEndpoint.TRANSACTION_MATCHING_BASE_URL_ZEPHYRUS + api.ENDPOINT_VISA_CARD

    @staticmethod
    def import_payment_file(transaction_type, mid):
        """This function will decide which way( API, Blob storage etc.,) the Payment Transaction needs to be
        imported into Harmonia"""

        match transaction_type:
            case "visa-auth-spotting":
                return TransactionMatching.get_visa_spotting_merchant_auth_file(mid)
            # case "amex-settlement": TransactionMatching.get_master_auth_csv(TestContext.mid)

    @staticmethod
    def exported_transaction(transaction_type):
        """This function will return the exported transactions"""

        match transaction_type:
            case "visa-auth-spotting":
                return QueryHarmonia.fetch_spotted_transaction_count(TestTransactionMatchingContext.transaction_id)
            # case _ : return "default function"
