import logging

from dataclasses import dataclass

import tests.helpers.database.setupdb as db

from tests.helpers.test_context import TestContext


@dataclass
class SchemeAccountRecord:
    id: int
    scheme_id: int
    is_deleted: bool
    pll_links: bool


@dataclass
class NewSchemeAccountRecord:
    id: int
    scheme_id: int
    is_deleted: bool
    alt_main_answer: str
    pll_links: bool
    link_status: int


@dataclass
class PaymentSchemeRecord:
    active_link: bool
    payment_card_account_id: int
    scheme_account_id: int


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
            scheme_account_record = SchemeAccountRecord(record[0], record[1], record[2], record[3])
        db.clear_db(connection)
        return scheme_account_record

    @staticmethod
    def fetch_ubiquity_schemeaccountentry(journey_type, external_id):
        """Fetch the ubiquity scheme account details using scheme_account_id"""
        connection = db.connect_db()
        record = db.execute_query_fetch_one(connection, get_link_status_query(journey_type, external_id))

        if record is None:
            raise Exception(f"Record not found for {external_id}")
        else:
            scheme_account_record = NewSchemeAccountRecord(
                record[0], record[1], record[2], record[3], record[4], record[5]
            )
        db.clear_db(connection)
        return scheme_account_record

    @staticmethod
    def fetch_pll_user_link(journey_type, external_id):
        """Fetch the payment card to membership card association details using pll_link"""
        connection = db.connect_db()
        record = db.execute_query_fetch_one(connection, get_pll_user_query(journey_type, external_id))
        if record is None:
            raise Exception(f"Record not found for {external_id}")
        else:
            payment_scheme_record = PaymentSchemeRecord(record[0], record[1], record[2])
        db.clear_db(connection)
        return payment_scheme_record

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
        if TestContext.environ == "staging":
            query_payment_account = (
                """SELECT id,name_on_card,is_deleted,pll_links
                     FROM hermes.public.payment_card_paymentcardaccount where id='%s'"""
                % payment_card_account_id
            )
        else:
            query_payment_account = (
                """SELECT id,name_on_card,is_deleted,pll_links
                     FROM lloyds_sit_hermes.public.payment_card_paymentcardaccount where id='%s'"""
                % payment_card_account_id
            )

        record = db.execute_query_fetch_one(connection, query_payment_account)
        if record is None:
            raise Exception(f"'{payment_card_account_id}' is an Invalid Payment account id")
        else:
            payment_account_record = PaymentAccountRecord(record[0], record[1], record[2], record[3])
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
    elif TestContext.environ == "staging":
        query_scheme_account = (
            """SELECT id,scheme_id,is_deleted,pll_links
                 FROM hermes.public.scheme_schemeaccount WHERE id='%s'"""
            % scheme_account_id
        )
    elif TestContext.environ == "sandbox":
        query_scheme_account = (
            """SELECT id,scheme_id,is_deleted,pll_links
                     FROM lloyds_sit_hermes.public.scheme_schemeaccount WHERE id='%s'"""
            % scheme_account_id
        )
    return query_scheme_account


def get_link_status_query(journey_type, external_id):
    if journey_type == "":
        logging.info("Scheme didnt attached to the wallet")
    elif TestContext.environ == "staging":
        query_scheme_account = (
            """SELECT sa.id, sa.scheme_id, sa.is_deleted, sa.alt_main_answer, sa.pll_links, sae.link_status
                 FROM hermes.public.scheme_schemeaccount  as sa
                 JOIN hermes.public.ubiquity_schemeaccountentry as sae ON sae.scheme_account_id = sa.id
                 JOIN hermes.public.user as usser ON usser.id = sae.user_id
                 AND usser.external_id ='%s'"""
            % external_id
        )
    elif TestContext.environ == "sandbox":
        query_scheme_account = (
            """SELECT sa.id, sa.scheme_id, sa.is_deleted, sa.alt_main_answer, sa.pll_links, sae.link_status
                 FROM lloyds_sit_hermes.public.scheme_schemeaccount  as sa
                 JOIN lloyds_sit_hermes.public.ubiquity_schemeaccountentry as sae ON sae.scheme_account_id = sa.id
                 JOIN lloyds_sit_hermes.public.user as usser ON usser.id = sae.user_id
                 AND usser.external_id ='%s'"""
            % external_id
        )
    return query_scheme_account


def get_pll_user_query(journey_type, external_id):
    if journey_type == "":
        logging.info("Scheme didnt attached to the wallet")
    elif TestContext.environ == "staging":
        query_scheme_account = (
            """SELECT pse.active_link, pse.payment_card_account_id, pse.scheme_account_id
                 FROM hermes.public.ubiquity_paymentcardschemeentry  as pse
                 JOIN hermes.public.ubiquity_plluserassociation as pua ON pua.pll_id = pse.id
                 JOIN hermes.public.user as usser ON usser.id = pua.user_id
                 AND usser.external_id ='%s'"""
            % external_id
        )
    elif TestContext.environ == "sandbox":
        query_scheme_account = (
            """SELECT pse.active_link, pse.payment_card_account_id, pse.scheme_account_id
                 FROM lloyds_sit_hermes.public.ubiquity_paymentcardschemeentry  as pse
                 JOIN lloyds_sit_hermes.public.ubiquity_plluserassociation as pua ON pll_id = pse.id
                 JOIN  lloyds_sit_hermes.public.user as usser ON usser.id = pua.user_id
                 AND usser.external_id ='%s'"""
            % external_id
        )
    return query_scheme_account


def update_query(scheme_account_id, status):
    if TestContext.environ == "staging":
        query_scheme_account = (
            f"UPDATE hermes.public.scheme_schemeaccount SET status = "
            f"{int(status)} WHERE id= {int(scheme_account_id)}"
        )
    else:
        query_scheme_account = (
            f"UPDATE lloyds_sit_hermes.public.scheme_schemeaccount SET status = "
            f"{int(status)} WHERE id= {int(scheme_account_id)}"
        )

    return query_scheme_account
