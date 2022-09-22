from tests import api
from tests.api.base import Endpoint
from tests.helpers.test_helpers import TestData


class MembershipPlans(Endpoint):
    @staticmethod
    def get_membership_plan_journey_field(token, merchant):
        url = Endpoint.BASE_URL + api.ENDPOINT_PLAN_JOURNEY_FIELDS.format(TestData.get_membership_plan_id(merchant))
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_plan_by_id(token, merchant):
        url = Endpoint.BASE_URL + api.ENDPOINT_LOYALTY_PLAN_BY_ID.format(TestData.get_membership_plan_id(merchant))
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_all_loyalty_plans(token):
        url = Endpoint.BASE_URL + api.ENDPOINT_LOYALTY_PLANS
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_plans_overview(token):
        url = Endpoint.BASE_URL + api.ENDPOINT_LOYALTY_PLANS_OVERVIEW
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response

    @staticmethod
    def get_loyalty_plan_details(token, merchant):
        url = Endpoint.BASE_URL + api.ENDPOINT_LOYALTY_PLAN_DETAILS.format(TestData.get_membership_plan_id(merchant))
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response
