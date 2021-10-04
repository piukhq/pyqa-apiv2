from tests import api
from tests.api.base import Endpoint
from tests.helpers.test_helpers import Merchant


class MembershipCards(Endpoint):

    # ---------------------------------------- Add Journey---------------------------------------------------
    @staticmethod
    def add_field_only_card(token, merchant, invalid_request=None):
        url = MembershipCards.get_add_url()
        header = Endpoint.request_header(token)
        if not invalid_request:
            payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload()
        else:
            payload = Merchant.get_merchant(merchant).add_field_only_membership_card_payload(invalid_request)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def authorise_field_only_card(token, merchant, scheme_account_id, invalid_request=None):
        url = MembershipCards.get_authorise_url(scheme_account_id)
        header = Endpoint.request_header(token)
        if not invalid_request:
            payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload()
        else:
            payload = Merchant.get_merchant(merchant).authorise_field_only_membership_card_payload(invalid_request)
        return Endpoint.call(url, header, "POST", payload)

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
    def get_add_url(scheme_account_id=None):
        """Return URL for membership_cards and
        membership_card/scheme_account_id"""
        if scheme_account_id is None:
            return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_ADD
        else:
            return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARD.format(scheme_account_id)

    @staticmethod
    def get_authorise_url(scheme_account_id):
        """Return URL for membership_cards and
        membership_card/scheme_account_id"""
        return Endpoint.BASE_URL + api.ENDPOINT_MEMBERSHIP_CARDS_AUTHORISE.format(scheme_account_id)

    @staticmethod
    def add_and_authorise_card(token, merchant, invalid_request=None):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        if not invalid_request:
            payload = Merchant.get_merchant(merchant).add_and_authorise_membership_card_payload()
        else:
            payload = Merchant.get_merchant(merchant).add_and_authorise_membership_card_payload(invalid_request)
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def add_and_authorise_card_with_existing_scheme(token, merchant):
        url = MembershipCards.get_add_and_authorise_url()
        header = Endpoint.request_header(token)
        payload = Merchant.get_merchant(merchant).add_and_authorise_existing_membership_card_payload()
        return Endpoint.call(url, header, "POST", payload)

    # Delete Membership Card
    @staticmethod
    def delete_scheme_account(token, scheme_account_id):
        url = MembershipCards.get_delete_url(scheme_account_id)
        header = Endpoint.request_header(token)
        response = Endpoint.call_payload(url, header, "DELETE")
        return response

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
