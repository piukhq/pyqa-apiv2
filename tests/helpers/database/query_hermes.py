import datetime
import logging

from dataclasses import dataclass

import tests.helpers.database.setupdb as db


@dataclass
class SchemeAccountRecord:
    id: int
    status: int
    scheme_id: int
    link_or_join_date: datetime.datetime
    main_answer: str
    is_delete_scheme: bool
    pll_links: bool


@dataclass
class PaymentAccountRecord:
    id: int
    name_on_card: str
    is_deleted: bool
    pll_links: bool


@dataclass
class CredentialAns:
    """sub- Set of credential answers
    All credential answers need not be captured as some of them are
    already verifying as apart of response"""

    card_number: int
    email: str
    last_name: str
    postcode: str
    merchant_identifier: str
    date_of_birth: str


class QueryHermes:
    @staticmethod
    def fetch_scheme_account(journey_type, scheme_account_id):
        """Fetch the scheme account details using scheme_account_id"""
        connection = db.connect_db()
        record = db.execute_query_fetch_one(connection, get_query(journey_type, scheme_account_id))

        if record is None:
            raise Exception(f"'{scheme_account_id}' is an Invalid Scheme account id")
        else:
            scheme_account_record = SchemeAccountRecord(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]
            )
        db.clear_db(connection)
        return scheme_account_record

    @staticmethod
    def update_scheme_account(scheme_account_id, status):
        """Fetch the scheme account details using scheme_account_id"""
        connection = db.connect_db()

        logging.info(db.execute_update(connection, update_query(scheme_account_id, status)))

        journey_type = "add_and_register"
        record = db.execute_query_fetch_one(connection, get_query(journey_type, scheme_account_id))

        if record is None:
            raise Exception(f"'{scheme_account_id}' is an Invalid Scheme account id")
        else:
            scheme_account_record = SchemeAccountRecord(
                record[0], record[1], record[2], record[3], record[4], record[5], record[6]
            )
        db.clear_db(connection)
        return scheme_account_record

    @staticmethod
    def fetch_payment_account(payment_card_account_id):
        connection = db.connect_db()
        query_payment_account = """SELECT id,name_on_card,is_deleted,pll_links FROM hermes.public.payment_card_paymentcardaccount
                     where id='%s'""" % payment_card_account_id
        record = db.execute_query_fetch_one(connection, query_payment_account)
        if record is None:
            raise Exception(f"'{payment_card_account_id}' is an Invalid Payment account id")
        else:
            payment_account_record = PaymentAccountRecord(
                record[0], record[1], record[2], record[3]
            )
        db.clear_db(connection)
        return payment_account_record


# def get_credential_qn_label(qn_id, connection):
#     """The label for each credential answer has been fetched using the unique question_id
#     which is obtained from scheme_schemeaccountcredentialanswer table"""
#     query_credential_qns = """SELECT type FROM hermes.public.scheme_schemecredentialquestion where id='%s'""" % qn_id
#     return db.execute_query_fetch_one(connection, query_credential_qns)


def get_query(journey_type, scheme_account_id):

    if journey_type == "":
        logging.info("Scheme didnt attached to the wallet")
    else:
        query_scheme_account = (
            """SELECT id,status,scheme_id,link_date,main_answer,is_deleted,pll_links
                 FROM hermes.public.scheme_schemeaccount WHERE id='%s'"""
            % scheme_account_id
        )
    return query_scheme_account


def update_query(scheme_account_id, status):
    query_scheme_account = (
        f"UPDATE hermes.public.scheme_schemeaccount SET status = " f"{int(status)} WHERE id= {int(scheme_account_id)}"
    )
    return query_scheme_account
