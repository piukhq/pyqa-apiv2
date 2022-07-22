import config

from tests import api
from tests.api.base import Endpoint
from tests.helpers.test_context import TestContext
from tests.payload.service.customer_accounts import UserDetails


class CustomerAccount:
    """Functions used to Create a new user, Service consent and Delete a user
    and
    Login using an existing user(User Login credentials are kept in test_data_sheet based in environment)"""

    @staticmethod
    def login_bink_user():
        url = Endpoint.BASE_URL + api.ENDPOINT_LOGIN
        headers = Endpoint.request_header()
        client_id = config.BINK.client_id
        payload = UserDetails.bink_login_user_payload(client_id, config.BINK.bundle_id)
        response = Endpoint.call(url, headers, "POST", payload)
        TestContext.token = response.json().get("api_key")
        return response

    @staticmethod
    def get_email_update_url():
        return Endpoint.BASE_URL + api.ENDPOINT_EMAIL_UPDATE

    @staticmethod
    def get_delete_user_url():
        return Endpoint.BASE_URL + api.ENDPOINT_DELETE_USER

    @staticmethod
    def user_email_update(token, test_email):
        url = CustomerAccount.get_email_update_url()
        header = Endpoint.request_header(token)
        payload = UserDetails.bink_user_email_update(test_email)

        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def user_duplicate_email_update(token, duplicate_email):
        url = CustomerAccount.get_email_update_url()
        header = Endpoint.request_header(token)
        payload = UserDetails.bink_user_email_update(duplicate_email)

        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def user_email_update_invalid_data(token, test_email, invalid_data):
        url = CustomerAccount.get_email_update_url()
        header = Endpoint.request_header(token)
        if invalid_data == "invalid_request":
            payload = UserDetails.bink_user_email_update_invalid_data(test_email, invalid_data)
            return Endpoint.call(url, header, "POST", payload)
        else:
            payload = UserDetails.bink_user_email_update_invalid_data(test_email, invalid_data)
            return Endpoint.call_payload(url, header, "POST", payload)

    @staticmethod
    def delete_user(token):
        url = CustomerAccount.get_delete_user_url()
        header = Endpoint.request_header(token)
        response = Endpoint.call(url, header, "DELETE")
        return response
