"""Email Template"""
EMAIL_TEMPLATE = "pytest+2.0_regression_email@bink.com"
LLOYDS_EMAIL_TEMPLATE = "pytest+2.0_auto_lloyds_email@bink.com"
BOS_EMAIL_TEMPLATE = "pytest+2.0_auto_bos_email@bink.com"
HALIFAX_EMAIL_TEMPLATE = "pytest+2.0_auto_halifax_email@bink.com"
SQUAREMEAL_EMAIL_TEMPLATE = "pytest+2.0_auto_squaremeal_email@bink.com"
LLOYDS_EXTERNAL_ID_TEMPLATE = "Auto_lloyds_external_id"
BOS_EXTERNAL_ID_TEMPLATE = "Auto_bos_external_id"
HALIFAX_EXTERNAL_ID_TEMPLATE = "Auto_halifax_external_id"
SQUAREMEAL_EXTERNAL_ID_TEMPLATE = "Auto_squaremeal_external_id"

"""Channel User Details"""
UID = "uid"
PWD = "pwd"
USER_DETAIL = "user_detail"
USER_DETAIL2 = "user_detail2"
USER_DETAIL3 = "user_detail3"
B2B_EMAIL = "b2b_email"
B2B_EXTERNAL_ID = "b2b_external_id"
B2B_EMAIL2 = "b2b_email2"
B2B_EXTERNAL_ID2 = "b2b_external_id2"
LLOYDS_EMAIL = "lloyds_email"
LLOYDS_EXTERNAL_ID = "lloyds_external_id"

"""Event Details"""
ORIGIN = ("origin",)
CHANNEL_BINK = "channel_bink"
CHANNEL_LLOYDS = "channel_lloyds"
CHANNEL_HALIFAX = "channel_halifax"
CHANNEL_BOS = "channel_bos"
STATUS = "status"
USER_CREATED = "user_created"

""" Contants for Add journey"""
ID = "id"
SLOW_JOIN_ID = "slow_join_id"
SUCCESS_EMAIL = "success_email"
IDENTICAL_JOIN = "identical_join"
PASSWORD = "password"
LAST_NAME = "last_name"
REGISTER_LASTNAME = "register_lastname"
POSTCODE = "postcode"
CARD_NUM = "card_num"
MERCHANT_ID = "merchant_id"
MERCHANT_ID2 = "merchant_id2"
TRANSACTIONS_MERCHANT_ID = "transactions_merchant_id"
TRANSACTIONS2_CARD = "transactions2_card"
TRANSACTIONS2_LASTNAME = "transactions2_lastname"
TRANSACTIONS2_UNAUTH_LASTNAME = "transactions2_unauth_lastname"
REGISTER_CARD = "register_card"
REGISTER_FAILED_CARD = "register_failed_card"
REGISTER_FAILED_EMAIL = "register_failed_email"
TRANSACTIONS_CARD = "transactions_card"
TRANSACTIONS_LAST_NAME = "transactions_card_last_name"
UNAUTHORISED_LAST_NAME = "unauthorised_last_name"
TRANSACTIONS_POSTCODE = "transactions_postcode"
TRANSACTIONS_EMAIL = "transactions_email"
TRANSACTIONS_PASSWORD = "transactions_password"
EMAIL = "email"
EMAIL2 = "email2"
INVALID_EMAIL = "invalid_email"
INVALID_PASSWORD = "invalid_password"
UNAUTHORISED_EMAIL = "unauthorised_email"
WALLET_ONLY = "wallet_only"
ENROL_FAILED = "enrol_failed"
ACCOUNT_ALREADY_EXIST = "account_already_exist"
ACTIVE = "active"
PENDING = "pending"
FAILED_VALIDATION = "failed_validation"
INVALID_CREDENTIALS = "invalid_credentials"
"""Register ghost card"""
TITLE = "Mr"
DATE_OF_BIRTH = "01/01/2000"
PASSWORD_ENROL = "Password01"
EMAIL_MARKETING = "true"
CONSENT = "true"

""" Payment Cards Constant"""
FIRST_SIX_DIGITS = "first_six_digits"
LAST_FOUR_DIGITS = "last_four_digits"
ISSUER = "issuer"
ISSUER_UPDATED = "issuer_updated"
TOKEN = "token"
FINGERPRINT = "fingerprint"
# PROVIDER = "provider"
CURRENCY_CODE = "currency_code"
COUNTRY = "country"
TYPE = "type"
TOKEN_2 = "token_2"
TOKEN_PREFIX = "token_prefix"
PAYMENT_CARD_STATUS = "status"
INVALID_TOKEN = "invalid_token1"

EXPECTED_JOURNEY_FIELDS_PATH_STAGING = "tests_resources/test_data/loyalty_plan" "/loyalty_plan_journey_field_staging"
EXPECTED_JOURNEY_FIELDS_PATH_SANDBOX = "tests_resources/test_data/loyalty_plan" "/loyalty_plan_journey_field_sandbox"

JSON_DIFF_EXPECTED_JSON = (
    "tests_resources/test_data/loyalty_plan/journey_type_diff_comparator" "/expected_membership_plan.json"
)
JSON_DIFF_ACTUAL_JSON = (
    "tests_resources/test_data/loyalty_plan/journey_type_diff_comparator" "/actual_membership_plan.json"
)

EXPECTED_LOYALTY_PLANS_STAGING = "tests_resources/test_data/loyalty_plan" "/loyalty_plans_staging"
EXPECTED_LOYALTY_PLANS_SANDBOX = "tests_resources/test_data/loyalty_plan" "/loyalty_plans_sandbox"
EXPECTED_VIEW_WALLET_STAGING = "tests_resources/test_data/get_wallet" "/get_wallet_staging"
EXPECTED_LOYALTY_PLANS_OVERVIEW_STAGING = "tests_resources/test_data/loyalty_plan" "/loyalty_plans_staging"
# PAYMENT_CARD_STATUS = "status"
# ACTIVE_LINK = "active_link"
# PAYMENT_PROVIDER = "payment_provider"
# PAYMENT_URL = "payment_url"
# PAYMENT_ENCODING = "payment_encoding"
# PAYMENT_DISCRIPTION = "payment_discription"
# PAYMENT_VERIFICATION = "payment_verification"
