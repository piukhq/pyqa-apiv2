from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils
from tests.payload.membership_cards.harvey_nichols import HarveyNicholsCard
from tests.payload.membership_cards.iceland import IcelandCard
from tests.payload.membership_cards.wasabi import WasabiCard


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


# class MembershipCardTestData:
#     """Functions used to supply expected data to pytest test_ classes"""
#
#     """Below functions read test data as "object" from test_data_sheet
#      and retrieve the data from object inside the test class"""

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


class TestData:
    """Functions used to supply expected data to pytest test_ classes"""

    """Below functions read test data as "object" from test_data_sheet
     and retrieve the data from object inside the test class"""

    @staticmethod
    def get_membership_plan_id(merchant):
        merchant_key = TestData.get_merchant_key(merchant)
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
            "Merchant_not_exists": "merchant_not_exists",
        }
        return switcher.get(merchant)

    @staticmethod
    def get_expected_membership_plan_json(loyalty_scheme, env, channel=None):

        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_mem_plan_path(env)

        return mem_plan_path + "/mebership_plan_journey_field_" + merchant_key + ".json"
        # if merchant == "Iceland" and channel == "barclays":
        #     """Temporary case as Iceland has different membership plan id for Bink & Barclays"""
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan_bmb.json"
        # else:
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan.json"

    @staticmethod
    def get_expected_loyalty_plan_by_id_json(loyalty_scheme, env, channel=None):

        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_loyalty_plan_by_id_path(env)

        return mem_plan_path + "/membership_plan_loyalty_field_" + merchant_key + ".json"

    @staticmethod
    def get_expected_all_loyalty_plans_json(env, channel=None):

        mem_plan_path = TestData.get_loyalty_plan_by_id_path(env)

        return mem_plan_path + "/membership_plan_all_loyalty_plans" + ".json"

    @staticmethod
    def get_expected_view_wallet_json(env, channel=None):
        wallet_path = TestData.get_wallet_path(env)
        return wallet_path + "/view_wallet" + ".json"

    @staticmethod
    def get_expected_view_join_wallet_json(env, channel=None):

        wallet_path = TestData.get_wallet_path(env)
        return wallet_path + "/view_wallet" + "_join.json"

    @staticmethod
    def get_wallet_path(env):
        """return the base path of stored get wallet json
        based on environment"""

        switcher = {"staging": constants.EXPECTED_VIEW_WALLET_STAGING}
        return switcher.get(env)

    @staticmethod
    def get_mem_plan_path(env):
        """return the base path of stored membership plan json
        for any merchant based on environment"""

        switcher = {"staging": constants.EXPECTED_MEMBERSHIP_PLANS_PATH_STAGING}
        return switcher.get(env)

    @staticmethod
    def get_loyalty_plan_by_id_path(env):
        """return the base path of stored membership plan json
        for any merchant based on environment"""

        switcher = {"staging": constants.EXPECTED_LOYALTY_PLANS_STAGING}
        return switcher.get(env)

    @staticmethod
    def get_loyalty_status():
        return TestDataUtils.TEST_DATA.scheme_status


class Merchant:
    @staticmethod
    def get_merchant(merchant):
        """Get merchant class object based on the merchnat name from BDD feature file
        Each merchant class contains payload for membership_cads end point"""

        switcher = {
            "HarveyNichols": HarveyNicholsCard,
            "Iceland": IcelandCard,
            "Wasabi": WasabiCard,
        }
        return switcher.get(merchant)

    @staticmethod
    def get_scheme_cred_main_ans(merchant):
        """Return main_scheme_account_answers for all merchants"""
        switcher = {
            "Iceland": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
            "Wasabi": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
        }
        return switcher.get(merchant)
