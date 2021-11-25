from tests import api
from tests.api.base import Endpoint
from tests.payload.token_b2b.b2b_token import TokenB2BDetail


class Token_b2b(Endpoint):
    @staticmethod
    def post_b2b_with_grant_type(token, token_type):
        url = Token_b2b.get_add_url()
        header = Endpoint.request_header(token)
        payload = TokenB2BDetail.post_b2btoken_with_grantype(token_type, scope="user")
        return Endpoint.call(url, header, "POST", payload)

    @staticmethod
    def get_add_url():
        return Endpoint.BASE_URL + api.ENDPOINT_TOKEN

    @staticmethod
    def token_invalid_json(token):
        url = Token_b2b.get_add_url()
        header = Endpoint.request_header(token)
        payload = TokenB2BDetail.token_with_invalid_json()
        return Endpoint.call_payload(url, header, "POST", payload)

    @staticmethod
    def unsupported_grant_type(token):
        url = Token_b2b.get_add_url()
        header = Endpoint.request_header(token)
        payload = TokenB2BDetail.unsupported_grant_type()
        return Endpoint.call(url, header, "POST", payload)
