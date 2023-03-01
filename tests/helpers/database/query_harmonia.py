import logging
from dataclasses import dataclass
import tests.helpers.database.setupdb as db


@dataclass
class MatchedTransactionRecord:
    count: int


class QueryHarmonia:
    @staticmethod
    def fetch_spotted_transaction_count(transaction_id):
        """Fetch the spotted account details using spotted_transaction_id and amount"""
        connection = db.connect_harmonia_db()
        record = db.execute_query_fetch_one(connection, get_spotted_transaction(transaction_id))
        if record is None:
            raise Exception(f"'{transaction_id}' is an Invalid transaction_id")
        else:
            spotted_transaction_record = MatchedTransactionRecord(record[0])
        db.clear_db(connection)
        return spotted_transaction_record


def get_spotted_transaction(transaction_id):
    spotted_transaction = (
        "SELECT count(*) from harmonia.public.export_transaction "
        "WHERE transaction_id = '{}'"
        "and status = 'EXPORTED'".format(transaction_id)
    )
    logging.info(spotted_transaction)
    return spotted_transaction
