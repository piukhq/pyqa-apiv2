# ------------------------------------ ---PAYMENT  CARDS ------------------------------------------------------- #

visa_payment_card = {
    "expiry_month": "01",
    "expiry_year": "11",
    "name_on_card": "visa_staging_test",
    "card_nickname": "visa_staging_test_nick",
    "issuer": "HSBC",
    "issuer_updated": "LLOYDS",
    "token": "pytest24021",
    "last_four_digits": "4242",
    "first_six_digits": "424242",
    "fingerprint": "pytest2002",
    # "provider": "VisaCard",
    "type": "debit",
    "country": "GB",
    "currency_code": "GBP",
    "status": "active",
    "token_2": "eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
    "token_prefix": "bearer eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
}

amex_payment_card = {
    "expiry_month": "03",
    "expiry_year": "11",
    "name_on_card": "amex_staging_test",
    "card_nickname": "amex_staging_test_nick",
    "issuer": "HSBC",
    "issuer_updated": "LLOYDS",
    "token": "pytest24021",
    "last_four_digits": "0005",
    "first_six_digits": "378282",
    "fingerprint": "pytest2002",
    # "provider": "AmexCard",
    "type": "debit",
    "country": "GB",
    "currency_code": "GBP",
    "status": "active",
    "token_2": "eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
    "token_prefix": "bearer eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
}

master_payment_card = {
    "expiry_month": "02",
    "expiry_year": "12",
    "name_on_card": "master_staging_test",
    "card_nickname": "master_staging_test_nick",
    "issuer": "HSBC",
    "issuer_updated": "LLOYDS",
    "token": "pytest24011",
    "last_four_digits": "5844",
    "first_six_digits": "528673",
    "fingerprint": "pytestversion2test",
    # "provider": "MasterCard",
    "type": "debit",
    "country": "GB",
    "currency_code": "GBP",
    "status": "active",
    "token_2": "eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
    "token_prefix": "bearer eyJhbGciOiJIU.eyJ1c2VyX2lkIjoyMzg3NywiY2hhbm.FCqWWGbD3jOTJfEe2tQHt-PlwTGqQg8YuS7V5fPo23Yz",
}

invalid_token = {
    "invalid_token1": "bearer invalid_token",
    "expired_token": "bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImFjY2Vzcy1zZWNyZXQtMSJ9.eyJ1c2VyX2lkIjoy"
    "Mzg3NywiY2hhbm5lbCI6ImNvbS5iYXJjbGF5cy5ibWIiLCJzdWIiOjIzODc3LCJleHAiOjE2MzEyOTE3MjYsImlhdCI6M"
    "TYzMTI5MDgyNX0.2LfB5dNuweArdz5j-ecXds4mepaeG65h3JA0vC-Mfeilv6C0IWVnfEK_K9_xrJDUhLD7f094rC1L7th"
    "5g4vJoQ",
}
# ----------------------------------------LOYALTY CARDs    --------------------------------------------------- #
iceland_membership_card = {
    "card_num": "6332040000300000003",
    # "register_card": "6332040000400000011",
    "unauthorised_last_name": "invalidlastname",
    "register_card": "6633204006543210000",
    "register_lastname": "ghostcard_success",
    "register_failed_card": "6332040065432156789",
    "register_failed_email": "generalerror@testbink.com",
    "transactions_card": "6332040000000000007",
    "barcode": "6332040000300000003",
    "transactions_card_last_name": "perfuser07",
    "transactions_postcode": "rg5 5aa",
    "transactions2_card": "6332040012312354321",
    "transactions2_lastname": "testuser",
    "transactions2_unauth_lastname": "error",
    "last_name": "perfuser03",
    "postcode": "mp6 0bb",
    "points": 123456,
    "currency": "GBP",
    "description": "Placeholder Balance Description",
    "transactions": "3",
    "transaction_status": "active",
    "transaction_currency": "GBP",
}

harvey_nichols_membership_card = {
    # "id": "andyjameshill@gmail.com",
    # "password": "BinkTest",
    # "card_num": "1000000962497",
    # "barcode": "1000000962497",
    # "points": 64,
    # "currency": "Points",
    # "description": "Placeholder Balance Description",
    # "transactions": "5",
    # "transaction_status": "active",
    # "transaction_currency": "Points",
    "id": "perfuser03@testbink.com",
    "password": "Password03",
    "card_num": "9000000000003",
    "barcode": "9000000000003",
    "points": 123456,
    "currency": "Points",
    "description": None,
    "transactions": "5",
    "transaction_status": "active",
    "transaction_currency": "Points",
}

join_emails = {
    "id": "joininprogress@testbink.com",
    "slow_join_id": "slowjoin@testbink.com",
    "success_email": "pytest+success@bink.com",
    "identical_join": "identicaljoin@bink.com",
}

wasabi_membership_card = {
    "card_num": "1048175295",
    # "transactions_card": "1048171268",
    # "transactions_email": "binktestuser10@wasabi.com",
    "transactions_card": "1048172996",
    "transactions_email": "binktestauto01@wasabi.com",
    "email": "binktestuser19@wasabi.com",
    "invalid_email": "fail@unknown.com",
    "unauthorised_email": "invalidemail@testbink.com",
    "points": 5,
    "currency": "stamps",
    "description": "",
    "transactions": "5",
    "transaction_status": "active",
    "transaction_currency": "stamps",
}

square_meal_membership_card = {
    "card_num": "10050000",
    "email": "pytest+auto1@testbink.com",
    "email2": "pytest+auto2@testbink.com",
    "password": "passauto01",
    "transactions_card": "10010012",
    "transactions_email": "pytest+smauto02@bink.com",
    "transactions_password": "password01",
    "transactions_merchant_id": "qa_testauto_02",
    "invalid_password": "incorrectpassword",
    "invalid_email": "fail@unknown.com",
    "unauthorised_email": "invalidemail@testbink.com",
    "points": 800,
    "currency": "points",
    "description": "",
    "merchant_id": "qa_test_01",
    "merchant_id2": "qa_test_02",
    "transactions": "3",
    "transaction_status": "active",
    "transaction_currency": "points",
}

viator_membership_card = {
    "card_num": "VIAT0522355816",
    "email": "qatest+voucher1@bink.com",
    "email2": "pytest+auto2@testbink.com",
    "password": "passauto01",
    "transactions_card": "VIAT0522355816",
    "transactions_email": "qatest+voucher1@bink.com",
    "transactions_password": "password01",
    "transactions_merchant_id": "qa_testauto_02",
    "invalid_password": "incorrectpassword",
    "invalid_email": "fail@unknown.com",
    "unauthorised_email": "invalidemail@testbink.com",
    "points": 800,
    "currency": "points",
    "description": "",
    "transactions": "3",
    "transaction_status": "active",
    "transaction_currency": "points",
}

trenette_membership_card = {
    "card_num": "TRNT4659789654",
    "transactions_card": "TRNT4659789654",
    "transactions_email": "JLcard3@bink.com",
    "email": "JLcard3@bink.com",
    "invalid_email": "fail@unknown.com",
    "unauthorised_email": "invalidemail@testbink.com",
    "points": 3,
    "currency": "stamps",
    "description": "",
    "transactions": "4",
    "transaction_status": "active",
    "transaction_currency": "stamps",
}

the_works_membership_card = {
    "card_num": "6338849749210000002622",
    "points": 3,
    "currency": "stamps",
    "description": "",
    "transactions": "4",
    "transaction_status": "active",
    "transaction_currency": "stamps",
    "register_card": "6338844992910000029726",
    "jon_register_account_already_exists_email": "emailexists",
    "register_account_already_exists_cardnum": "cardnumberexists",
    "join_register_non_retryable_error": "opnotpermitted",
    "join_register_non_retryable_http_error": "failhttperror",
    "invalid_card_number": "633884102938475600011",
    "unknown_card_number": "633884564738291000022",
}


# ----------------------------------------MEMBERSHIP PLAN IDs   ----------------------------------------------- #

membership_plan_id = {
    "fat_face": 246,
    "harvey_nichols": 124,
    "iceland": 105,
    "square_meal": 286,
    "whsmith": 280,
    "asos": 288,
    "wasabi": 281,
    "trenette": 284,
    "viator": 292,
    "merchant_not_exists": 9999,
    "Bink Test Scheme": 132,  # suspended loyalty plan
    "Wallis": 131,  # inactive loyalty plan
    "the_works": 294,
}

scheme_status = {
    "wallet_only": 10,
    "failed_validation": 401,
    "active": 1,
    "enrol_failed": 901,
    "account_already_exist": 445,
    "invalid_credentials": 403,
    "ghost_card_registration_failed": 902,
}

# -------------------------------------------EVENTS---------------------------------------------------------- #

event_info = {
    "origin": "channel",
    "channel_bink": "com.bink.wallet",
    "channel_lloyds": "com.lloydsqa.api2",
    "channel_halifax": "com.halifax.api2",
    "channel_bos": "com.bos.api2",
    "status": 1,
}

event_type = {
    "user_created": "user.created",
    "user_deleted": "user.deleted",
    "lc_join_request": "lc.join.request",
    "lc_status_change": "lc.statuschange",
    "lc_join_success": "lc.join.success",
    "lc_join_failed": "lc.join.failed",
    "lc_auth_request": "lc.auth.request",
    "lc_auth_success": "lc.auth.success",
    "lc_add_auth_request": "lc.addandauth.request",
    "lc_add_auth_success": "lc.addandauth.success",
    "lc_add_auth_failed": "lc.addandauth.failed",
}

consent_slug = {
    "Wasabi": "EmailOptin",
    "Iceland": "marketing_opt_in",
    "SquareMeal": "Subscription",
}

# ------------------------------------------ DB DETAILS ---------------------------------------------------- #

db_details = {
    "user": "common@bink-uksouth-staging-common",
    "password": "",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "hermes",
}

harmonia_db_details = {
    "user": "common@bink-uksouth-staging-common",
    "password": "",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "harmonia",
}
# ---------------------------------------------USER ACCOUNTS ---------------------------------------------------- #

bink_user_accounts = {
    "uid": "pytest+api2.0_staging_auto@bink.com",
    "pwd": "Password1",
    "user_detail": "38766",
    "user_detail2": "38627",
    "b2b_email": "pytest+b2b_staging_email@bink.com",
    "b2b_email2": "pytest+b2b_staging_email2@bink.com",
    "lloyds_email": "pytest+lloydsb2b_staging_email@bink.com",
    "lloyds_external_id": "12345",
    "b2b_external_id": "Autob2b",
    "b2b_external_id2": "Autob2b2",
}
