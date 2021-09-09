from tests import api
from tests.api.base import Endpoint
from tests.helpers.test_helpers import MembershipCardTestData


class MembershipPlans(Endpoint):
    @staticmethod
    def get_membership_plan_journey_field(token, merchant):
        url = Endpoint.BASE_URL + api.ENDPOINT_PLAN_JOURNEY_FIELDS.format(
            MembershipCardTestData.get_membership_plan_id(merchant)
        )
        header = Endpoint.request_header(token, "2.0")
        response = Endpoint.call(url, header, "GET")
        return response
