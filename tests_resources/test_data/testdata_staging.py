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
    "provider": "VisaCard",
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
    "provider": "AmexCard",
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
    "last_four_digits": "4444",
    "first_six_digits": "555555",
    "fingerprint": "pytest2002",
    "provider": "MasterCard",
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
    "barcode": "6332040000300000003",
    "last_name": "hundred",
    "postcode": "rg2 2aa",
    "points": 205.02,
    "currency": "GBP",
    "description": "Placeholder Balance Description",
    "transactions": "3",
    "transaction_status": "active",
    "transaction_currency": "GBP",
}

harvey_nichols_membership_card = {
    "id": "andyjameshill@gmail.com",
    "password": "BinkTest",
    "card_num": "1000000962497",
    "barcode": "1000000962497",
    "points": 64,
    "currency": "Points",
    "description": "Placeholder Balance Description",
    "transactions": "5",
    "transaction_status": "active",
    "transaction_currency": "Points",
}

harvey_nichols_invalid_data = {"id": "fail@unknown.com"}

wasabi_membership_card = {
    "card_num": "1048175295",
    "email": "binktestuser19@wasabi.com",
    "points": 5,
    "currency": "stamps",
    "description": "",
    "transactions": "",
    "transaction_status": "active",
    "transaction_currency": "stamps",
}

# ----------------------------------------MEMBERSHIP PLAN IDs   ----------------------------------------------- #

membership_plan_id = {
    "fat_face": 246,
    "harvey_nichols": 124,
    "iceland": 105,
    "whsmith": 280,
    "wasabi": 281,
    "merchant_not_exists": 0000,
}

scheme_status = {
    "wallet_only": 10,
}

# ------------------------------------------ DB DETAILS ---------------------------------------------------- #

db_details = {
    "user": "common@bink-uksouth-staging-common",
    "password": "",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "hermes",
}

# ---------------------------------------------USER ACCOUNTS ---------------------------------------------------- #

bink_user_accounts = {
    "uid": "pytest_2.0_staging_auto@bink.com",
    "pwd": "Password1",
    "user_detail": "27925",
    "user_detail2": "1168",
}
