# ------------------------------------ ---PAYMENT  CARDS ------------------------------------------------------- #

visa_payment_card = {
    "expiry_month": "01",
    "expiry_year": "11",
    "name_on_card": "visa_sandbox_test",
    "card_nickname": "visa_sandbox_test_nick",
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
    "name_on_card": "amex_sandbox_test",
    "card_nickname": "amex_sandbox_test_nick",
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
    "name_on_card": "master_sandbox_test",
    "card_nickname": "master_sandbox_test_nick",
    "card_nickname": "master_sandbox_test_nick",
    "issuer": "HSBC",
    "issuer_updated": "LLOYDS",
    "token": "pytest24011",
    "last_four_digits": "4444",
    "first_six_digits": "555555",
    "fingerprint": "pytest2002",
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
    "register_card": "6332040031231230002",
    "transactions_card": "6332040000300000003",
    "barcode": "6332040000300000003",
    "transactions_card_last_name": "perfuser03",
    "transactions_postcode": "mp6 0bb",
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

harvey_nichols_invalid_data = {
    "id": "fail@unknown.com",
    "slow_join_id": "slowjoin@testbink.com",
    "success_email": "pytest+success@bink.com",
}

wasabi_membership_card = {
    "card_num": "1048175295",
    # "transactions_card": "1048171268",
    # "transactions_email": "binktestuser10@wasabi.com",
    "transactions_card": "1048172852",
    "transactions_email": "binktestuser14@wasabi.com",
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
    "card_num": "100500000",
    "transactions_card": "100500000",
    "transactions_email": "pytest+auto1@testbink.com",
    "email": "pytest+auto1@testbink.com",
    "password": "passauto01",
    "invalid_password": "pass01",
    "invalid_email": "fail@unknown.com",
    "unauthorised_email": "invalidemail@testbink.com",
    "points": 800,
    "currency": "points",
    "description": "",
    "transactions": "3",
    "transaction_status": "active",
    "transaction_currency": "points",
}

# Wallet_info can have card details of different merchants and each merchant can have multiple loyalty cards.
# Here Wasabi dictionary has a list stored in it. So more than 1 card can be added in future.
wallet_info = {
    "Wasabi": [
        {
            # "id": 149652,
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1649424631,
                "current_display_value": "6 stamps",
                "loyalty_currency_name": "stamps",
                "prefix": None,
                "suffix": "stamps",
                "current_value": "6",
                "target_value": "7",
            },
            "transactions": [
                {
                    # "id": "318120",
                    "timestamp": 1638356401,
                    "description": "Ascot 1 Petty Cury £8.00",
                    "display_value": "1 stamps",
                },
                {
                    # "id": "318121",
                    "timestamp": 1635854462,
                    "description": "Ascot 2 Petty Cury £15.60",
                    "display_value": "1 stamps",
                },
            ],
            "vouchers": [
                {
                    "state": "inprogress",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Spend £7.00 or more to get a stamp. "
                    "Collect 7 stamps to get a Meal Voucher of up to £7 off your next meal.",
                    "voucher_code": None,
                    "barcode_type": 0,
                    "progress_display_text": "6/7 stamps",
                    "current_value": "6",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Spend £7.00 or more to get a stamp. "
                    "Collect 7 stamps to get a Meal Voucher of up to £7 off your next meal.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": None,
                    "expiry_date": None,
                    "redeemed_date": None,
                },
                {
                    "state": "issued",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Earned",
                    "voucher_code": "12DQ696S",
                    "barcode_type": 0,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Show your Wasabi Club reward code in store to redeem £7 off your next meal.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1704844800",
                    "redeemed_date": None,
                },
                {
                    "state": "expired",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Expired",
                    "voucher_code": "12DQ696S",
                    "barcode_type": 0,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Your FREE meal voucher has expired.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1640822400",
                    "redeemed_date": None,
                },
                {
                    "state": "redeemed",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Redeemed",
                    "voucher_code": "12DQ696S",
                    "barcode_type": 0,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Your FREE meal voucher was redeemed.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1673481600",
                    "redeemed_date": "1643241600",
                },
                {
                    "state": "cancelled",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": None,
                    "voucher_code": "12DQ696S",
                    "barcode_type": 0,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": None,
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1673308800",
                    "redeemed_date": None,
                },
            ],
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "1048172852",
                "colour": "#ccd400",
                "text_colour": "#7289da",
            },
            "images": [
                {
                    "id": 1297,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Logo.png",
                    "description": "Wasabi Icon",
                    "encoding": "png",
                },
                {
                    "id": 1324,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Promo_1968x732.png",
                    "description": "Wasabi Promotion 1",
                    "encoding": "png",
                },
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                },
                {
                    "id": 1298,
                    "type": 9,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Alternate_Hero.png",
                    "description": "Wasabi Alternative Hero",
                    "encoding": "png",
                },
                {
                    "id": 1319,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Offer_tile_5_CVAeqUv_naFzo9T.png",
                    "description": "Wasabi Test Offer",
                    "encoding": "png",
                },
            ],
        }
    ],
    "Iceland": [
        {
            # "id": 143755,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1647611859,
                "current_display_value": "£380.01",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "380.01",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "304833",
                    "timestamp": 1643809826,
                    "description": "CREDIT",
                    "display_value": "£12.50",
                },
                {
                    # "id": "304834",
                    "timestamp": 1639591616,
                    "description": "CREDIT",
                    "display_value": "£1",
                },
                {
                    # "id": "304836",
                    "timestamp": 1631961858,
                    "description": "CREDIT",
                    "display_value": "£5",
                },
                {
                    # "id": "304835",
                    "timestamp": 1626767059,
                    "description": "CREDIT",
                    "display_value": "£21.15",
                },
                {
                    # "id": "304837",
                    "timestamp": 1623549329,
                    "description": "DEBIT",
                    "display_value": "-£23",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": "63320400000000000070080",
                "barcode_type": 0,
                "card_number": "6332040000000000007",
                "colour": "#d50724",
                "text_colour": "#00FF00",
            },
            "images": [
                {
                    "id": 1289,
                    "type": 9,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_MiyMk96.png",
                    "description": "Iceland Alternative Hero Image",
                    "encoding": "png",
                },
                {
                    "id": 374,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                    "description": "Iceland Icon",
                    "encoding": "png",
                },
                {
                    "id": 373,
                    "type": 4,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                    "description": "Iceland Asset",
                    "encoding": "png",
                },
                {
                    "id": 1070,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                },
                {
                    "id": 1071,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                },
                {
                    "id": 1072,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                },
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                },
                {
                    "id": 1303,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                    "description": "Iceland Offer - Greggs",
                    "encoding": "jpg",
                },
                {
                    "id": 1302,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                    "description": "Iceland Offer - Pizza",
                    "encoding": "jpg",
                },
                {
                    "id": 1398,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "PromotionsIcelandBonusCard1968x732.png",
                    "description": "Promo_Text_1",
                    "encoding": "png",
                },
            ],
        }
    ],
    "HarveyNichols": [
        {
            # "id": 143753,
            "loyalty_plan_id": 124,
            "loyalty_plan_name": "Rewards by Harvey Nichols",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1647610241,
                "current_display_value": "123456 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "123456",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "304829",
                    "timestamp": 1536080100,
                    "description": "Test transaction: 2 items",
                    "display_value": "-50 pts",
                },
                {
                    # "id": "304830",
                    "timestamp": 1536046510,
                    "description": "Test transaction: 1 item",
                    "display_value": "10 pts",
                },
                {
                    # "id": "304828",
                    "timestamp": 1536012345,
                    "description": "Test transaction: 5 items",
                    "display_value": "200 pts",
                },
                {
                    # "id": "304827",
                    "timestamp": 1533211890,
                    "description": "Test transaction: 3 items",
                    "display_value": "-100 pts",
                },
                {
                    # "id": "304826",
                    "timestamp": 1530455055,
                    "description": "Test transaction: 1 item",
                    "display_value": "20 pts",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": "9000000000003",
                "barcode_type": 7,
                "card_number": "9000000000003",
                "colour": "#000000",
                "text_colour": "#bfc68c",
            },
            "images": [
                {
                    "id": 1293,
                    "type": 9,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_ESHACSv.png",
                    "description": "Harvey Nichols Alternative Hero",
                    "encoding": "png",
                },
                {
                    "id": 660,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_Logo.png",
                    "description": "Harvey Nichols Icon",
                    "encoding": "png",
                },
                {
                    "id": 1187,
                    "type": 8,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_4_Black.png",
                    "description": "Black Tier",
                    "encoding": "png",
                },
                {
                    "id": 1184,
                    "type": 8,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_1_Silver.png",
                    "description": "Silver Tier",
                    "encoding": "png",
                },
                {
                    "id": 1185,
                    "type": 8,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_2_Gold.png",
                    "description": "Gold Tier",
                    "encoding": "png",
                },
                {
                    "id": 1186,
                    "type": 8,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_3_Platinum.png",
                    "description": "Platinum Tier",
                    "encoding": "png",
                },
                {
                    "id": 1304,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Rewards_square_oct_02.jpg",
                    "description": "Harvey Nichols Rewards",
                    "encoding": "jpg",
                },
                {
                    "id": 575,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_0_TIER_UNKNOWN.png",
                    "description": "Harvey Nichols Hero",
                    "encoding": "png",
                },
            ],
        }
    ],
    "payment_accounts": [
        {
            "provider": "Mastercard",
            "issuer": "HSBC",
            "status": "active",
            "type": "debit",
            "currency_code": "GBP",
            "country": "GB",
            "last_four_digits": "4444",
            "images": [
                {
                    "id": 2,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard-Payment_1goHQYv.png",
                    "description": "Mastercard Hero",
                    "encoding": "png",
                },
                {
                    "id": 32,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard_pricelesscities_heathrow.png",
                    "description": "MasterCard Offer Stay - Heathrow",
                    "encoding": "png",
                },
                {
                    "id": 35,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Mastercard_qkr_app.png",
                    "description": "Master Offer 7 - Qkr",
                    "encoding": "png",
                },
                {
                    "id": 28,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard_pricelesscities_moreoffers.png",
                    "description": "MasterCard Offer 6 - More Offers",
                    "encoding": "png",
                },
                {
                    "id": 40,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard_pricelesscities_loungepass.png",
                    "description": "MasterCard Offer Stay - Lounge",
                    "encoding": "png",
                },
                {
                    "id": 27,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard_pricelesscities_liberty.png",
                    "description": "MasterCard Offer Shop - Liberty",
                    "encoding": "png",
                },
                {
                    "id": 39,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard_pricelesscities_market.png",
                    "description": "MasterCard Offer Play - Markets",
                    "encoding": "png",
                },
                {
                    "id": 53,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "10773378_MDemand_WFP_BINK_Tile.png",
                    "description": "World Food Programme",
                    "encoding": "png",
                },
            ],
        }
    ],
}

wallet_overview_info = {
    "Wasabi": [
        {
            # "id": 154316,
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1651055796,
                "current_display_value": "6 stamps",
                "loyalty_currency_name": "stamps",
                "prefix": None,
                "suffix": "stamps",
                "current_value": "6",
                "target_value": "7",
            },
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "1048172852",
                "colour": "#ccd400",
                "text_colour": "#7289da",
            },
            "reward_available": True,
            "images": [
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                }
            ],
        }
    ],
    "Iceland": [
        {
            # "id": 154317,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1651055977,
                "current_display_value": "£380.01",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "380.01",
                "target_value": None,
            },
            "card": {
                "barcode": "63320400000000000070080",
                "barcode_type": 0,
                "card_number": "6332040000000000007",
                "colour": "#d50724",
                "text_colour": "#00FF00",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                }
            ],
        }
    ],
    "HarveyNichols": [
        {
            # "id": 154318,
            "loyalty_plan_id": 124,
            "loyalty_plan_name": "Rewards by Harvey Nichols",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1651056068,
                "current_display_value": "123456 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "123456",
                "target_value": None,
            },
            "card": {
                "barcode": "9000000000003",
                "barcode_type": 7,
                "card_number": "9000000000003",
                "colour": "#000000",
                "text_colour": "#bfc68c",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 575,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Harvey_Nichols_Card_0_TIER_UNKNOWN.png",
                    "description": "Harvey Nichols Hero",
                    "encoding": "png",
                }
            ],
        }
    ],
    "payment_accounts": [
        {
            # "id": 78816,
            "provider": "Mastercard",
            "issuer": "HSBC",
            "status": "active",
            "type": "debit",
            "currency_code": "GBP",
            "country": "GB",
            "last_four_digits": "4444",
            "images": [
                {
                    "id": 2,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Mastercard-Payment_1goHQYv.png",
                    "description": "Mastercard Hero",
                    "encoding": "png",
                }
            ],
        }
    ],
}

wallet_info_by_card_id = {
    "Wasabi": {
        # "id": 149653,
        "loyalty_plan_id": 281,
        "loyalty_plan_name": "Wasabi Club",
        "is_fully_pll_linked": True,
        "pll_linked_payment_accounts": 1,
        "total_payment_accounts": 1,
        "status": {"state": "authorised", "slug": None, "description": None},
        "balance": {
            # "updated_at": 1649425854,
            "current_display_value": "6 stamps",
            "loyalty_currency_name": "stamps",
            "prefix": None,
            "suffix": "stamps",
            "current_value": "6",
            "target_value": "7",
        },
        "transactions": [
            {
                # "id": "318122",
                "timestamp": 1638356401,
                "description": "Ascot 1 Petty Cury £8.00",
                "display_value": "1 stamps",
            },
            {
                # "id": "318123",
                "timestamp": 1635854462,
                "description": "Ascot 2 Petty Cury £15.60",
                "display_value": "1 stamps",
            },
        ],
        "vouchers": [
            {
                "state": "inprogress",
                "earn_type": "stamps",
                "reward_text": "Free Meal",
                "headline": "Spend £7.00 or more to get a stamp. Collect 7 stamps to get a Meal "
                "Voucher of up to £7 off your next meal.",
                "voucher_code": None,
                "barcode_type": 0,
                "progress_display_text": "6/7 stamps",
                "current_value": "6",
                "target_value": "7",
                "prefix": None,
                "suffix": "stamps",
                "body_text": "In progress body text",
                "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                "issued_date": None,
                "expiry_date": None,
                "redeemed_date": None,
            },
            {
                "state": "issued",
                "earn_type": "stamps",
                "reward_text": "Free Meal",
                "headline": "Earned",
                "voucher_code": "12DQ696S",
                "barcode_type": 0,
                "progress_display_text": "7/7 stamps",
                "current_value": "7",
                "target_value": "7",
                "prefix": None,
                "suffix": "stamps",
                "body_text": "Issued body text",
                "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                "issued_date": "1591787076",
                "expiry_date": "1673308800",
                "redeemed_date": None,
            },
        ],
        "card": {
            "barcode": None,
            "barcode_type": None,
            "card_number": "1048172852",
            "colour": "#ccd400",
            "text_colour": "#7289da",
        },
        "images": [
            {
                "id": 1297,
                "type": 3,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Logo.png",
                "description": "Wasabi Icon",
                "encoding": "png",
            },
            {
                "id": 1324,
                "type": 7,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Promo_1968x732.png",
                "description": "Wasabi Promotion 1",
                "encoding": "png",
            },
            {
                "id": 1296,
                "type": 0,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Card.png",
                "description": "Wasabi Hero",
                "encoding": "png",
            },
            {
                "id": 1298,
                "type": 9,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Wasabi_Alternate_Hero.png",
                "description": "Wasabi Alternative Hero",
                "encoding": "png",
            },
            {
                "id": 1319,
                "type": 2,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Offer_tile_5_CVAeqUv_naFzo9T.png",
                "description": "Wasabi Test Offer",
                "encoding": "png",
            },
        ],
    },
    "Iceland": {
        # "id": 143755,
        "loyalty_plan_id": 105,
        "loyalty_plan_name": "Iceland Bonus Card",
        "is_fully_pll_linked": True,
        "pll_linked_payment_accounts": 1,
        "total_payment_accounts": 1,
        "status": {"state": "authorised", "slug": None, "description": None},
        "balance": {
            # "updated_at": 1647611859,
            "current_display_value": "£380.01",
            "loyalty_currency_name": "GBP",
            "prefix": "£",
            "suffix": None,
            "current_value": "380.01",
            "target_value": None,
        },
        "transactions": [
            {
                # "id": "304833",
                "timestamp": 1643809826,
                "description": "CREDIT",
                "display_value": "£12.50",
            },
            {
                # "id": "304834",
                "timestamp": 1639591616,
                "description": "CREDIT",
                "display_value": "£1",
            },
            {
                # "id": "304836",
                "timestamp": 1631961858,
                "description": "CREDIT",
                "display_value": "£5",
            },
            {
                # "id": "304835",
                "timestamp": 1626767059,
                "description": "CREDIT",
                "display_value": "£21.15",
            },
            {
                # "id": "304837",
                "timestamp": 1623549329,
                "description": "DEBIT",
                "display_value": "-£23",
            },
        ],
        "vouchers": [],
        "card": {
            "barcode": "63320400000000000070080",
            "barcode_type": 0,
            "card_number": "6332040000000000007",
            "colour": "#d50724",
            "text_colour": "#00FF00",
        },
        "images": [
            {
                "id": 1289,
                "type": 9,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_MiyMk96.png",
                "description": "Iceland Alternative Hero Image",
                "encoding": "png",
            },
            {
                "id": 374,
                "type": 3,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                "description": "Iceland Icon",
                "encoding": "png",
            },
            {
                "id": 373,
                "type": 4,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                "description": "Iceland Asset",
                "encoding": "png",
            },
            {
                "id": 1070,
                "type": 5,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                "description": "Iceland Reference",
                "encoding": "jpg",
            },
            {
                "id": 1071,
                "type": 5,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                "description": "Iceland Reference",
                "encoding": "jpg",
            },
            {
                "id": 1072,
                "type": 5,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                "description": "Iceland Reference",
                "encoding": "jpg",
            },
            {
                "id": 1234,
                "type": 0,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                "description": "Iceland Loyalty Card",
                "encoding": "png",
            },
            {
                "id": 1303,
                "type": 2,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                "description": "Iceland Offer - Greggs",
                "encoding": "jpg",
            },
            {
                "id": 1302,
                "type": 2,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                "description": "Iceland Offer - Pizza",
                "encoding": "jpg",
            },
            {
                "id": 1398,
                "type": 7,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                "PromotionsIcelandBonusCard1968x732.png",
                "description": "Promo_Text_1",
                "encoding": "png",
            },
        ],
    },
    "HarveyNichols": {
        # "id": 143753,
        "loyalty_plan_id": 124,
        "loyalty_plan_name": "Rewards by Harvey Nichols",
        "is_fully_pll_linked": True,
        "pll_linked_payment_accounts": 1,
        "total_payment_accounts": 1,
        "status": {"state": "authorised", "slug": None, "description": None},
        "balance": {
            # "updated_at": 1647610241,
            "current_display_value": "123456 pts",
            "loyalty_currency_name": "points",
            "prefix": None,
            "suffix": "pts",
            "current_value": "123456",
            "target_value": None,
        },
        "transactions": [
            {
                # "id": "304829",
                "timestamp": 1536080100,
                "description": "Test transaction: 2 items",
                "display_value": "-50 pts",
            },
            {
                # "id": "304830",
                "timestamp": 1536046510,
                "description": "Test transaction: 1 item",
                "display_value": "10 pts",
            },
            {
                # "id": "304828",
                "timestamp": 1536012345,
                "description": "Test transaction: 5 items",
                "display_value": "200 pts",
            },
            {
                # "id": "304827",
                "timestamp": 1533211890,
                "description": "Test transaction: 3 items",
                "display_value": "-100 pts",
            },
            {
                # "id": "304826",
                "timestamp": 1530455055,
                "description": "Test transaction: 1 item",
                "display_value": "20 pts",
            },
        ],
        "vouchers": [],
        "card": {
            "barcode": "9000000000003",
            "barcode_type": 7,
            "card_number": "9000000000003",
            "colour": "#000000",
            "text_colour": "#bfc68c",
        },
        "images": [
            {
                "id": 1293,
                "type": 9,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_ESHACSv.png",
                "description": "Harvey Nichols Alternative Hero",
                "encoding": "png",
            },
            {
                "id": 660,
                "type": 3,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_Logo.png",
                "description": "Harvey Nichols Icon",
                "encoding": "png",
            },
            {
                "id": 1187,
                "type": 8,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_Card_4_Black.png",
                "description": "Black Tier",
                "encoding": "png",
            },
            {
                "id": 1184,
                "type": 8,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_Card_1_Silver.png",
                "description": "Silver Tier",
                "encoding": "png",
            },
            {
                "id": 1185,
                "type": 8,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Harvey_Nichols_Card_2_Gold.png",
                "description": "Gold Tier",
                "encoding": "png",
            },
            {
                "id": 1186,
                "type": 8,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                "Harvey_Nichols_Card_3_Platinum.png",
                "description": "Platinum Tier",
                "encoding": "png",
            },
            {
                "id": 1304,
                "type": 2,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                "Harvey_Nichols_Rewards_square_oct_02.jpg",
                "description": "Harvey Nichols Rewards",
                "encoding": "jpg",
            },
            {
                "id": 575,
                "type": 0,
                "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                "Harvey_Nichols_Card_0_TIER_UNKNOWN.png",
                "description": "Harvey Nichols Hero",
                "encoding": "png",
            },
        ],
    },
}

# ----------------------------------------MEMBERSHIP PLAN IDs   ----------------------------------------------- #

membership_plan_id = {
    "fat_face": 246,
    "harvey_nichols": 194,
    "iceland": 105,
    "whsmith": 280,
    "wasabi": 316,
    "asos": 328,
    "square_meal": 326,
    "merchant_not_exists": 0000,
    "Bink Test Scheme": 132,  # suspended loyalty plan
    "Wallis": 131,  # inactive loyalty plan
}

scheme_status = {
    "wallet_only": 10,
    "active": 1,
    "enrol_failed": 901,
    "account_already_exist": 445,
}

# ------------------------------------------ DB DETAILS ---------------------------------------------------- #

db_details = {
    "user": "common@bink-uksouth-lloyds-sit",
    "password": "",
    "host": "127.0.0.1",
    "port": "5432",
    "database": "hermes",
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

Join_Scheme_status = {
    "join_success": {
        "state": "authorised",
        "slug": None,
        "description": None,
    },
    "enrol_failed": {
        "state": "failed",
        "slug": "JOIN_FAILED",
        "description": "The retailer has not been able to accept your request at this time. "
        "Please remove the request and try again.",
    },
    "asynchronous_join_in_progress": {
        "state": "pending",
        "slug": "JOIN_IN_PROGRESS",
        "description": None,
    },
}
