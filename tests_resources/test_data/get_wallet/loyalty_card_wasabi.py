class WasabiResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
            # "id": 205105,
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1663164498,
                "current_display_value": "6 stamps",
                "loyalty_currency_name": "stamps",
                "prefix": None,
                "suffix": "stamps",
                "current_value": "6",
                "target_value": "7",
            },
            "transactions": [
                {
                    # "id": "446780",
                    "timestamp": 1638356401,
                    "description": "Ascot 1 Petty Cury £8.00",
                    "display_value": "1 stamps",
                },
                {
                    # "id": "446781",
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
                    "barcode_type": None,
                    "progress_display_text": "6/7 stamps",
                    "current_value": "6",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Spend £7.00 or more to get a stamp. Collect 7 stamps to get a Meal "
                    "Voucher of up to £7 off your next meal.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": None,
                    "expiry_date": None,
                    "redeemed_date": None,
                    "conversion_date": None,
                },
                {
                    "state": "issued",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Earned",
                    "voucher_code": "12DQ696S",
                    "barcode_type": None,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Show your Wasabi Club reward code in store to redeem £7 off your next meal.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1924819200",
                    "redeemed_date": None,
                    "conversion_date": None,
                },
                {
                    "state": "cancelled",
                    "earn_type": "stamps",
                    "reward_text": "Free Meal",
                    "headline": "Cancelled",
                    "voucher_code": "12DQ696S",
                    "barcode_type": None,
                    "progress_display_text": "7/7 stamps",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "stamps",
                    "body_text": "Your voucher has been cancelled. "
                    "If you believe we have made a mistake please contact enquiries@wasabi.uk.com.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/wasabi/tc.html",
                    "issued_date": "1591787076",
                    "expiry_date": "1644491076",
                    "redeemed_date": None,
                    "conversion_date": None,
                },
            ],
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "1048172996",
                "colour": "#ccd400",
                "text_colour": "#000000",
            },
            "reward_available": True,
            "images": [
                {
                    "id": 1324,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Promo_1968x732.png",
                    "description": "Wasabi Promotion 1",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1319,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/" "Offer_tile_5_CVAeqUv_naFzo9T.png",
                    "description": "Wasabi Test Offer",
                    "encoding": "png",
                    "cta_url": "https://www.wasabi.uk.com/find-a-wasabi",
                },
                {
                    "id": 1297,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Logo.png",
                    "description": "Wasabi Icon",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
            # "id": 205105,
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1663164498,
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
                "card_number": "1048172996",
                "colour": "#ccd400",
                "text_colour": "#000000",
            },
            "reward_available": True,
            "images": [
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return wallet_overview_info

    @staticmethod
    def wallet_unauth_response():
        unauth_wallet_info = {
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "unauthorised",
                "slug": "AUTHORISATION_FAILED",
                "description": "We're unable to verify the Loyalty Card details provided. "
                "Please re-enter your details and try again.",
            },
            "balance": {
                "updated_at": None,
                "current_display_value": None,
                "loyalty_currency_name": None,
                "prefix": None,
                "suffix": None,
                "current_value": None,
                "target_value": None,
            },
            "transactions": [],
            "vouchers": [],
            "card": {
                "barcode": None,
                "barcode_type": None,
                # "card_number": "1048172996",
                "colour": "#ccd400",
                "text_colour": "#000000",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1324,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Promo_1968x732.png",
                    "description": "Wasabi Promotion 1",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1319,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/" "schemes/Offer_tile_5_CVAeqUv_naFzo9T.png",
                    "description": "Wasabi Test Offer",
                    "encoding": "png",
                    "cta_url": "https://www.wasabi.uk.com/find-a-wasabi",
                },
                {
                    "id": 1297,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Logo.png",
                    "description": "Wasabi Icon",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
            # "pll_links": [
            # 	{
            # 		"payment_account_id": 113304,
            # 		"payment_scheme": "Mastercard",
            # 		"status": {
            # 			"state": "inactive",
            # 			"slug": "LOYALTY_CARD_NOT_AUTHORISED",
            # 			"description": "The Loyalty Card is not authorised so no PLL link can be created."
            # 		}
            # 	}
            # ]
        }
        return unauth_wallet_info

    @staticmethod
    def wallet_overview_unauth_response():
        unauth_wallet_overview_info = {
            "loyalty_plan_id": 281,
            "loyalty_plan_name": "Wasabi Club",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "unauthorised",
                "slug": "AUTHORISATION_FAILED",
                "description": "We're unable to verify the Loyalty Card details provided."
                " Please re-enter your details and try again.",
            },
            "balance": {
                "updated_at": None,
                "current_display_value": None,
                "loyalty_currency_name": None,
                "prefix": None,
                "suffix": None,
                "current_value": None,
                "target_value": None,
            },
            "card": {
                "barcode": None,
                "barcode_type": None,
                # "card_number": "1048172996",
                "colour": "#ccd400",
                "text_colour": "#000000",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1296,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Wasabi_Card.png",
                    "description": "Wasabi Hero",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return unauth_wallet_overview_info
