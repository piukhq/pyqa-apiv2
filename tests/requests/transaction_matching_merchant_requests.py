import io
import logging

from azure.storage.blob import BlobServiceClient

from settings import BLOB_STORAGE_DSN
from tests.helpers.test_transaction_matching_context import TestTransactionMatchingContext
from tests.payload.transaction_matching.transaction_matching_merchant_file import create_retailer_csv


def upload_retailer_file_into_blob(
    merchant_container: str, payment_card_provider: str, retailer_location_id: str
) -> None:
    """StringIO creates a text stream using an in-memory text buffer."""
    output = io.StringIO()
    """change below code when more merchants are there to follow blob route.
    Below function will create the merchant csv file and assign it to the output_buffer"""
    create_retailer_csv(output, payment_card_provider, retailer_location_id)

    logging.info(BLOB_STORAGE_DSN)
    bbs = BlobServiceClient.from_connection_string(BLOB_STORAGE_DSN)
    blob_client = bbs.get_blob_client(
        TestTransactionMatchingContext.container_name,
        merchant_container + f"{TestTransactionMatchingContext.file_name}",
    )
    logging.info("The Retailer Transaction File is: \n" + output.getvalue())
    blob_client.upload_blob(output.getvalue().encode())
    logging.info("The Retailer Transaction File is uploaded into the blob")
