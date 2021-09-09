from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils


class PaymentCardTestData:
    """This function is for future use - when more testing in payment cards"""

    @staticmethod
    def get_data(payment_card_provider="master"):
        switcher = {
            "amex": TestDataUtils.TEST_DATA.amex_payment_card,
            "visa": TestDataUtils.TEST_DATA.visa_payment_card,
            "master": TestDataUtils.TEST_DATA.master_payment_card,
        }
        return switcher.get(payment_card_provider)


class MembershipCardTestData:
    """Functions used to supply expected data to pytest test_ classes"""

    """Below functions read test data as "object" from test_data_sheet
     and retrieve the data from object inside the test class"""

    # @staticmethod
    # def get_membership_card_status_states():
    #     return TestDataUtils.TEST_DATA.membership_card_status_states
    #
    # @staticmethod
    # def get_membership_card_status_reason_codes():
    #     return TestDataUtils.TEST_DATA.membership_card_status_reason_codes

    # @staticmethod
    # def get_data(merchant):
    #     switcher = {
    #         "Iceland": TestDataUtils.TEST_DATA.iceland_membership_card,
    #         "HarveyNichols": TestDataUtils.TEST_DATA.harvey_nichols_membership_card,
    #         "Wasabi": TestDataUtils.TEST_DATA.wasabi_membership_card,
    #         "WHSmith": TestDataUtils.TEST_DATA.whsmith_membership_card,
    #         "FatFace": TestDataUtils.TEST_DATA.fat_face_membership_card,
    #     }
    #     return switcher.get(merchant)

    @staticmethod
    def get_membership_plan_id(merchant):
        merchant_key = MembershipCardTestData.get_merchant_key(merchant)
        return TestDataUtils.TEST_DATA.membership_plan_id.get(merchant_key)

    @staticmethod
    def get_merchant_key(merchant):
        """Generate the merchant key based on the
        merchant value from bdd feature file"""

        switcher = {
            "Iceland": "iceland",
            "HarveyNichols": "harvey_nichols",
            "FatFace": "fat_face",
            "Wasabi": "wasabi",
            "WHSmith": "whsmith",
        }
        return switcher.get(merchant)

    @staticmethod
    def get_expected_membership_plan_json(loyalty_scheme, env, channel=None):

        merchant_key = MembershipCardTestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = MembershipCardTestData.get_mem_plan_path(env)

        return mem_plan_path + "/mebership_plan_journey_field_" + merchant_key + ".json"
        # if merchant == "Iceland" and channel == "barclays":
        #     """Temporary case as Iceland has different membership plan id for Bink & Barclays"""
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan_bmb.json"
        # else:
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan.json"

    @staticmethod
    def get_mem_plan_path(env):
        """return the base path of stored membership plan json
        for any merchant based on environment"""

        switcher = {"staging": constants.EXPECTED_MEMBERSHIP_PLANS_PATH_STAGING}
        return switcher.get(env)
