import datetime

from dataclasses import dataclass

import tests.helpers.database.setupdb as db


@dataclass
class SchemeAccountRecord:
    id: int
    status: int
    scheme_id: int
    link_or_join_date: datetime.datetime
    main_answer: str


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
        """Fetch the scheme account details using scheme_account_id """
        connection = db.connect_db()
        record = db.execute_query_fetch_one(connection, get_query(journey_type, scheme_account_id))

        if record is None:
            raise Exception(f"'{scheme_account_id}' is an Invalid Scheme account id")
        else:
            scheme_account_record = SchemeAccountRecord(record[0], record[1], record[2], record[3], record[4])
        db.clear_db(connection)
        return scheme_account_record


def get_credential_qn_label(qn_id, connection):
    """The label for each credential answer has been fetched using the unique question_id
    which is obtained from scheme_schemeaccountcredentialanswer table"""
    query_credential_qns = """SELECT type FROM hermes.public.scheme_schemecredentialquestion where id='%s'""" % qn_id
    return db.execute_query_fetch_one(connection, query_credential_qns)


def get_query(journey_type, scheme_account_id):

    if journey_type == "Add_field":
        query_scheme_account = (
            """SELECT id,status,scheme_id,link_date,main_answer
                 FROM hermes.public.scheme_schemeaccount WHERE id='%s'"""
            % scheme_account_id
        )

    return query_scheme_account
