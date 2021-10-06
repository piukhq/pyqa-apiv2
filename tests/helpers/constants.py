"""Email Template"""
EMAIL_TEMPLATE = "pytest_2.0_regression_email@bink.com"

"""Channel User Details"""
UID = "uid"
PWD = "pwd"
USER_DETAIL = "user_detail"
USER_DETAIL2 = "user_detail2"

""" Contants for Add journey"""
ID = "id"
PASSWORD = "password"
LAST_NAME = "last_name"
POSTCODE = "postcode"
CARD_NUM = "card_num"
EMAIL = "email"
WALLET_ONLY = "wallet_only"
ACTIVE = "active"

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
PROVIDER = "provider"
CURRENCY_CODE = "currency_code"
COUNTRY = "country"
TYPE = "type"
TOKEN_2 = "token_2"
TOKEN_PREFIX = "token_prefix"
PAYMENT_CARD_STATUS = "status"
INVALID_TOKEN = "invalid_token1"

EXPECTED_MEMBERSHIP_PLANS_PATH_STAGING = (
    "tests_resources/test_data/membership_plan" "/membership_plan_journey_field_staging"
)

JSON_DIFF_EXPECTED_JSON = (
    "tests_resources/test_data/membership_plan/journey_type_diff_comparator" "/expected_membership_plan.json"
)
JSON_DIFF_ACTUAL_JSON = (
    "tests_resources/test_data/membership_plan/journey_type_diff_comparator" "/actual_membership_plan.json"
)

# PAYMENT_CARD_STATUS = "status"
# ACTIVE_LINK = "active_link"
# PAYMENT_PROVIDER = "payment_provider"
# PAYMENT_URL = "payment_url"
# PAYMENT_ENCODING = "payment_encoding"
# PAYMENT_DISCRIPTION = "payment_discription"
# PAYMENT_VERIFICATION = "payment_verification"
