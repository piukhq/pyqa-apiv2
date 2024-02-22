from tests.helpers import constants
from tests.helpers.test_data_utils import TestDataUtils
from tests.payload.loyalty_cards.iceland import IcelandCard
from tests.payload.loyalty_cards.itsu import Itsu
from tests.payload.loyalty_cards.squaremeal import SquareMealCard
from tests.payload.loyalty_cards.the_works import TheWorks
from tests.payload.loyalty_cards.trenette import TrenetteCard
from tests.payload.loyalty_cards.viator import ViatorCard
from tests.payload.loyalty_cards.wasabi import WasabiCard
from tests_resources.test_data.get_wallet.loyalty_card_iceland import IcelandResponse
from tests_resources.test_data.get_wallet.loyalty_card_itsu import ItsuResponse
from tests_resources.test_data.get_wallet.loyalty_card_squaremeal import (
    SquareMealResponse,
)
from tests_resources.test_data.get_wallet.loyalty_card_the_works import TheWorksResponse
from tests_resources.test_data.get_wallet.loyalty_card_viator import ViatorResponse
from tests_resources.test_data.get_wallet.loyalty_card_wasabi import WasabiResponse
from tests_resources.test_data.get_wallet.payment_account import PaymentAccountResponse


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
            case "Bink Test Scheme":
                return "Bink Test Scheme"
            case "Wallis":
                return "Wallis"
            case "Merchant_not_exists":
                return "merchant_not_exists"
            case "The_Works":
                return "the_works"
            case "itsu":
                return "itsu"

    @staticmethod
    def get_expected_journey_fields_json(loyalty_scheme, env, channel=None):
        merchant_key = TestData.get_merchant_key(loyalty_scheme)
        mem_plan_path = TestData.get_mem_plan_path(env)

        return mem_plan_path + "/loyalty_plan_journey_field_" + merchant_key + ".json"

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

    @staticmethod
    def get_merchant_response(merchant):
        """This function will select the correct test data file for the merchant"""

        match merchant:
            case "Iceland":
                return IcelandResponse
            case "Wasabi":
                return WasabiResponse
            case "SquareMeal":
                return SquareMealResponse
            case "Viator":
                return ViatorResponse
            case "The_Works":
                return TheWorksResponse
            case "itsu":
                return ItsuResponse
            case "payment_account":
                return PaymentAccountResponse


class Merchant:
    @staticmethod
    def get_merchant(merchant):
        """Get merchant class object based on the merchnat name from BDD feature file
        Each merchant class contains payload for membership_cads end point"""

        match merchant:
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
            case "itsu":
                return Itsu

    @staticmethod
    def get_scheme_cred_main_ans(merchant):
        """Return main_scheme_account_answers for all merchants"""
        switcher = {
            "Iceland": TestDataUtils.TEST_DATA.iceland_membership_card.get(constants.CARD_NUM),
            "Wasabi": TestDataUtils.TEST_DATA.wasabi_membership_card.get(constants.CARD_NUM),
        }
        return switcher.get(merchant)
