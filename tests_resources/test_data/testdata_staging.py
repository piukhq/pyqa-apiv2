# ------------------------------------ ---PAYMENT  CARDS ------------------------------------------------------- #

visa_payment_card = {
    "expiry_month": "01",
    "expiry_year": "11",
    "name_on_card": "visa_staging_test",
    "card_nickname": "visa_staging_test_nick",
    "issuer": "HSBC",
    "issuer_updated": "LLOYDS",
    "token": "pytest24021",
    "last_four_digits": "4297",
    "first_six_digits": "424242",
    "fingerprint": "pytest2002",
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
    "last_four_digits": "5834",
    "first_six_digits": "518673",
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
# ----------------------------------------LOYALTY CARDs    ---------------------------------------------------
join_emails = {
    "id": "joininprogress@testbink.com",
    "join_fail_id": "emailexists@testbink.com",
    "slow_join_id": "slowjoin@testbink.com",
    "success_email": "pytest+success@bink.com",
    "identical_join": "identicaljoin@bink.com",
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
    "transactions_card": "6338849749210000002622",
}

itsu_membership_card = {
    "card_num": "1406495756",
    "invalid_card_number": "0099887766",
    "unknown_card_number": "0009998887",
}
# ----------------------------------------MEMBERSHIP PLAN IDs   ----------------------------------------------- #

membership_plan_id = {
    "square_meal": 286,
    "trenette": 284,
    "viator": 292,
    "merchant_not_exists": 9999,
    "Bink Test Scheme": 132,  # suspended loyalty plan
    "Wallis": 131,  # inactive loyalty plan
    "the_works": 294,
    "itsu": 295,
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
    "client_id_lloyds": "LkVR4URcysf22a10Jpm3QXVmSGD8neUwgLo7JBSKtDxlV8zZJr",
    "channel_halifax": "com.halifax.api2",
    "client_id_halifax": "MIwOHVa2qUAdxyXn5o4n7lA6ZM38N9NOXsXS0zSCYWPoDq4rw7",
    "channel_bos": "com.bos.api2",
    "client_id_bos": "NnZn3Tu2dpNF5sbgypk0RKNiwrVK68b7Aq2JyYcLvIwGYm5QoB",
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
    "lc_register_request": "lc.register.request",
    "lc_register_success": "lc.register.success",
    "lc_register_failed": "lc.register.failed",
    "pll_link_statuschange": "pll_link.statuschange",
}

consent_slug = {
    "The_Works": "email_marketing",
    "SquareMeal": "Subscription",
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
