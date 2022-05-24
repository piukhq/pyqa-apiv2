from tests import api
from tests.api.base import Endpoint
from tests.helpers.test_context import TestContext
from tests.helpers.test_helpers import Merchant
from tests.requests.encryption import encrypted_payload_token


class MembershipCards(Endpoint):

    # ---------------------------------------- Add Journey---------------------------------------------------
    #   @staticmethod
    #   def add_field_only_card(token, merchant, invalid_request=None):
    #       url = MembershipCards.get_add_url()
    #       header = Endpoint.request_header(token)
    #       if not invalid_request:
    #           payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload()
    #       else:
    #          payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload(invalid_request)
    #      return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_field_only_card(token, merchant, invalid_request=None):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not invalid_request:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload()
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "POST", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload()
                return Endpoint.call(url, header, "POST", payload)
        else:
            payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload(invalid_request)
            return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_before_register_field_only_card(token, merchant, invalid_request=None):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        if not invalid_request:
            payload = Merchant.get_merchant(merchant).add_field_before_register_membership_card_payload()
        else:
            payload = Merchant.get_merchant(merchant).add_field_before_register_membership_card_payload(invalid_request)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def get_view_wallet(token):
        url = Endpoint.BASE_URL + api.ENDPOINT_WALLET
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_view_wallet_overview(token):
        url = Endpoint.BASE_URL + api.ENDPOINT_WALLET_OVERVIEW
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_view_wallet_by_card_id(token, scheme_account_id):
        url = MembershipCards.get_loyalty_card_by_id_url(scheme_account_id)
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_balance(token, scheme_account_id):
        url = MembershipCards.get_balance_url(scheme_account_id)
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_vouchers(token, scheme_account_id):
        url = MembershipCards.get_vouchers_url(scheme_account_id)
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_transactions(token, scheme_account_id):
        url = MembershipCards.get_transactions_url(scheme_account_id)
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def register_field_only_card(token, merchant, email, scheme_account_id, invalid_data=None):
        url = MembershipCards.get_register_url(scheme_account_id)
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not invalid_data:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).register_field_only_membership_card_payload(email)
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "PUT", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).register_field_only_membership_card_payload(email)
                return Endpoint.call(url, header, "PUT", payload)
        else:
            payload = Merchant.get_merchant(merchant).register_field_only_membership_card_payload(email, invalid_data)
            return Endpoint.call(url, header, "PUT", payload)

    @staticmethod
    def register_field_with_invalid_json(token, merchant, email, scheme_account_id, invalid_data=None):
        url = MembershipCards.get_register_url(scheme_account_id)
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).register_field_only_membership_card_payload(email, invalid_data)
        return Endpoint.call_payload(url, header, "PUT", payload)

    @staticmethod
    def add_and_register_field(token, merchant, email, invalid_request=None):
        url = MembershipCards.get_add_and_register_url()
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not invalid_request:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).add_and_register_membership_card(email)
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "POST", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).add_and_register_membership_card(email)
                return Endpoint.call(url, header, "POST", payload)
        else:
            payload = Merchant.get_merchant(merchant).add_and_register_membership_card(email, invalid_request)
            return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def delete_fail_scheme_account(token, scheme_account_id):
        url = MembershipCards.get_fail_delete_url(scheme_account_id)
        header = Endpoint.request_header(token)
        response = Endpoint.call_payload(url, header, "DELETE")
        return response

    @staticmethod
    def get_fail_delete_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN_FAILED.format(scheme_account_id)

    @staticmethod
    def join_field(token, merchant, email, request_payload=None):
        url = MembershipCards.get_join_url()
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not request_payload:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).join_journey(email)
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "POST", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).join_journey(email)
                return Endpoint.call(url, header, "POST", payload)
        else:
            payload = Merchant.get_merchant(merchant).join_journey(email, request_payload)
            if request_payload == "invalid_json":
                return Endpoint.call_payload(url, header, "POST", payload)
            else:
                return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def authorise_field_only_card(token, merchant, scheme_account_id, invalid_data=None):
        url = MembershipCards.get_authorise_url(scheme_account_id)
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not invalid_data:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload()
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "PUT", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload()
                return Endpoint.call(url, header, "PUT", payload)
        else:
            payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload(invalid_data)
            return Endpoint.call(url, header, "PUT", payload)

    @staticmethod
    def authorise_field_with_existing_field(token, merchant, scheme_account_id, invalid_data):
        url = MembershipCards.get_authorise_url(scheme_account_id)
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload(invalid_data)
        return Endpoint.call_payload(url, header, "PUT", payload)

    @staticmethod
    def add_field_with_existing_card(token, merchant):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload_with_existing_id()
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_field_with_invalid_json(token, merchant):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_field_only_membership_card_with_invalid_json()
        return Endpoint.call_payload(url, header, "POST", payload)

    @staticmethod
    def add_and_auth_field_with_invalid_json(token, merchant):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_auth_field_only_membership_card_with_invalid_json()
        return Endpoint.call_payload(url, header, "POST", payload)

    @staticmethod
    def add_and_auth_field_with_unauthorised_json(token, merchant):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_auth_field_only_membership_card_with_unauthorised_json()
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_and_register_field_with_invalid_json(token, merchant):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_register_field_only_membership_card_with_invalid_json()
        return Endpoint.call_payload(url, header, "POST", payload)

    @staticmethod
    def get_add_url(scheme_account_id=None):
        """Return URL for membership_cards and
        membership_card/scheme_account_id"""
        if scheme_account_id is None:
            return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        else:
            return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARD.format(scheme_account_id)

    @staticmethod
    def get_loyalty_card_by_id_url(scheme_account_id):
        """Return URL for get_loyalty_card_by_id"""
        return Endpoint.BASE_URL + api.ENDPOINT_WALLET_BY_CARD_ID.format(scheme_account_id)

    @staticmethod
    def get_authorise_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(scheme_account_id)

    @staticmethod
    def get_add_and_register_url():
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_REGISTER

    @staticmethod
    def get_join_url():
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_JOIN

    @staticmethod
    def get_register_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_REGISTER.format(scheme_account_id)

    @staticmethod
    def get_balance_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_BALANCE.format(scheme_account_id)

    @staticmethod
    def get_vouchers_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_VOUCHERS.format(scheme_account_id)

    @staticmethod
    def get_transactions_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_TRANSACTIONS.format(scheme_account_id)

    @staticmethod
    def add_and_authorise_card(token, merchant, invalid_request=None):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        encrypt_header = Endpoint.encrypt_header(token)
        if not invalid_request:
            if TestContext.flag_encrypt == "true":
                payload = Merchant.get_merchant(merchant).add_and_authorise_membership_card_payload()
                data = encrypted_payload_token(payload)
                return Endpoint.call_payload(url, encrypt_header, "POST", data)
            elif TestContext.flag_encrypt == "false":
                payload = Merchant.get_merchant(merchant).add_and_authorise_membership_card_payload()
                return Endpoint.call(url, header, "POST", payload)
        else:
            payload = Merchant.get_merchant(merchant).add_and_authorise_membership_card_payload(invalid_request)
            return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_and_authorise_transactions_card(token, merchant):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_authorise_transactions_card_payload()
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_and_authorise_card_with_different_credential(token, merchant):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_authorise_with_different_auth_field()
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_and_authorise_card_with_existing_scheme(token, merchant):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_authorise_existing_membership_card_payload()
        return Endpoint.call(url, header, "POST", payload)

    #
    # @staticmethod
    # def add_and_register_card_with_existing_scheme(token, merchant):
    #     url = MembershipCards.get_add_and_register_url()
    #     header = Endpoint.request_header(token)
    #     payload = Merchant.get_merchant(merchant).add_and_register_membership_card()
    #     return Endpoint.call(url, header, "POST", payload)
    # Delete Membership Card

    @staticmethod
    def delete_scheme_account(token, scheme_account_id):
        url = MembershipCards.get_delete_url(scheme_account_id)
        header = Endpoint.request_header(token)
        response = Endpoint.call_payload(url, header, "DELETE")
        return response

    @staticmethod
    def delete_membership_card_with_payload(token, merchant, scheme_account_id):
        url = MembershipCards.get_delete_url(scheme_account_id)
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload()
        return Endpoint.call(url, header, "DELETE", payload)

    @staticmethod
    def get_delete_url(scheme_account_id):
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS.format(scheme_account_id)

    @staticmethod
    def get_add_and_authorise_url():
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_ADD_AND_AUTHORISE
