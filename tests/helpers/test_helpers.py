from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils
from tests.payload.loyalty_cards.harvey_nichols import HarveyNicholsCard
from tests.payload.loyalty_cards.iceland import IcelandCard
from tests.payload.loyalty_cards.squaremeal import SquareMealCard
from tests.payload.loyalty_cards.the_works import TheWorks
from tests.payload.loyalty_cards.trenette import TrenetteCard
from tests.payload.loyalty_cards.viator import ViatorCard
from tests.payload.loyalty_cards.wasabi import WasabiCard


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

        # switcher = {
        #     "Iceland": "iceland",
        #     "HarveyNichols": "harvey_nichols",
        #     "SquareMeal": "square_meal",
        #     "FatFace": "fat_face",
        #     "Wasabi": "wasabi",
        #     "WHSmith": "whsmith",
        #     "Merchant_not_exists": "merchant_not_exists",
        #     "Wallis": "Wallis",
        #     "Bink Test Scheme": "Bink Test Scheme",
        #     "Asos": "asos",
        #     "Trenette": "trenette",
        #     "Viator": "viator",
        # }
        # return switcher.get(merchant)

        match merchant:
            case "Iceland":
                return "iceland"
            case "Wasabi":
                return "wasabi"
            case "SquareMeal":
                return "square_meal"
            case "Trenette":
                return "trenette"
            case "Viator":
                return "viator"
            case "HarveyNichols":
                return "harvey_nichols"
            case "Bink Test Scheme":
                return "Bink Test Scheme"
            case "Merchant_not_exists":
                return "merchant_not_exists"
            case "The_Works":
                return "the_works"

    @staticmethod
    def get_expected_journey_fields_json(loyalty_scheme, env, channel=None):
        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_mem_plan_path(env)

        return mem_plan_path + "/loyalty_plan_journey_field_" + merchant_key + ".json"
        # if merchant == "Iceland" and channel == "barclays":
        #     """Temporary case as Iceland has different membership plan id for Bink & Barclays"""
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan_bmb.json"
        # else:
        #     return mem_plan_path + "/" + merchant_key + "_membership_plan.json"

    @staticmethod
    def get_expected_loyalty_plans_overview_json(env, channel=None):
        loyalty_plan_overview_path = TestData.get_loyalty_plans_overview_path(env)
        return loyalty_plan_overview_path + "/loyalty_plans_overview" + ".json"

    @staticmethod
    def get_expected_loyalty_plan_details_json(loyalty_scheme, env, channel=None):
        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_loyalty_plan_by_id_path(env)
        return mem_plan_path + "/loyalty_plan_details_" + merchant_key + ".json"

    @staticmethod
    def get_expected_loyalty_plan_by_id_json(loyalty_scheme, env, channel=None):
        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_loyalty_plan_by_id_path(env)

        return mem_plan_path + "/loyalty_plan_by_id_" + merchant_key + ".json"

    @staticmethod
    def get_expected_all_loyalty_plans_json(env, channel=None):
        mem_plan_path = TestData.get_loyalty_plan_by_id_path(env)

        return mem_plan_path + "/loyalty_plans_all" + ".json"

    @staticmethod
    def get_expected_view_wallet_json(env, channel=None):
        wallet_path = TestData.get_wallet_path(env)
        return wallet_path + "/view_wallet" + ".json"

    @staticmethod
    def get_expected_view_wallet_overview_json(env):
        wallet_path = TestData.get_wallet_path(env)
        return wallet_path + "/view_wallet_overview" + ".json"

    @staticmethod
    def get_expected_view_join_wallet_json(env, channel=None):
        wallet_path = TestData.get_wallet_path(env)
        return wallet_path + "/view_wallet" + "_join.json"

    @staticmethod
    def get_wallet_path(env):
        """return the base path of stored get wallet json
        based on environment"""

        switcher = {
            "staging": constants.EXPECTED_VIEW_WALLET_STAGING,
            "sandbox": constants.EXPECTED_VIEW_WALLET_SANDBOX,
        }
        return switcher.get(env)

    @staticmethod
    def get_loyalty_plans_overview_path(env):
        """return the base path of stored get loyalty plans overview json
        based on environment"""

        switcher = {
            "staging": constants.EXPECTED_LOYALTY_PLANS_OVERVIEW_STAGING,
            "sandbox": constants.EXPECTED_LOYALTY_PLANS_OVERVIEW_SANDBOX,
        }

        return switcher.get(env)

    @staticmethod
    def get_mem_plan_path(env):
        """return the base path of stored membership plan json
        for any merchant based on environment"""

        switcher = {
            "staging": constants.EXPECTED_JOURNEY_FIELDS_PATH_STAGING,
            "sandbox": constants.EXPECTED_JOURNEY_FIELDS_PATH_SANDBOX,
        }
        return switcher.get(env)

    @staticmethod
    def get_loyalty_plan_by_id_path(env):
        """return the base path of stored membership plan json
        for any merchant based on environment"""

        switcher = {
            "staging": constants.EXPECTED_LOYALTY_PLANS_STAGING,
            "sandbox": constants.EXPECTED_LOYALTY_PLANS_SANDBOX,
        }
        return switcher.get(env)

    @staticmethod
    def get_loyalty_status():
        return TestDataUtils.TEST_DATA.scheme_status


class Merchant:
    @staticmethod
    def get_merchant(merchant):
        """Get merchant class object based on the merchnat name from BDD feature file
        Each merchant class contains payload for membership_cads end point"""

        match merchant:
            case "HarveyNicholsCard":
                return HarveyNicholsCard
            case "Iceland":
                return IcelandCard
            case "Wasabi":
                return WasabiCard
            case "SquareMeal":
                return SquareMealCard
            case "Trenette":
                return TrenetteCard
            case "Viator":
                return ViatorCard
            case "The_Works":
                return TheWorks

    @staticmethod
    def get_scheme_cred_main_ans(merchant):
        """Return main_scheme_account_answers for all merchants"""
        switcher = {
            "Iceland": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
            "Wasabi": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
        }
        return switcher.get(merchant)
