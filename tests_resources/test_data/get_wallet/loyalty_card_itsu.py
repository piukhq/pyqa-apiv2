class ItsuResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
            "loyalty_plan_id": 295,
            "loyalty_plan_name": "itsu loyalty",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1688658362,
                "current_display_value": "5 stamps",
                "loyalty_currency_name": "stamps",
                "prefix": None,
                "suffix": "stamps",
                "current_value": "5",
                "target_value": "7",
            },
            "transactions": [],
            "vouchers": [
                {
                    "state": "inprogress",
                    "earn_type": "stamps",
                    "reward_text": "Free dish, snack, or drink",
                    "headline": "Earn more butterflies for your free dish, snack or drink",
                    "voucher_code": None,
                    "barcode_type": None,
                    "progress_display_text": "5/7 butterflies",
                    "current_value": "5",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "butterflies",
                    "body_text": "Earn more butterflies for your free dish, snack or drink",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/itsu/tc.html",
                    "issued_date": None,
                    "expiry_date": None,
                    "redeemed_date": None,
                    "conversion_date": None
                },
                {
                    "state": "redeemed",
                    "earn_type": "stamps",
                    "reward_text": "Free dish, snack, or drink",
                    "headline": "Redeemed",
                    "voucher_code": "----------",
                    "barcode_type": None,
                    "progress_display_text": "7/7 butterflies",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "butterflies",
                    "body_text": "Your itsu voucher was redeemed.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/itsu/tc.html",
                    "issued_date": "1685009490",
                    "expiry_date": "1905983940",
                    "redeemed_date": "1687269540",
                    "conversion_date": None
                },
                {
                    "state": "expired",
                    "earn_type": "stamps",
                    "reward_text": "Free dish, snack, or drink",
                    "headline": "Expired",
                    "voucher_code": "----------",
                    "barcode_type": None,
                    "progress_display_text": "7/7 butterflies",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "butterflies",
                    "body_text": "Your itsu voucher has expired.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/itsu/tc.html",
                    "issued_date": "1685009490",
                    "expiry_date": "1687737540",
                    "redeemed_date": None,
                    "conversion_date": None
                },
                dict(state="issued", earn_type="stamps", reward_text="Free dish, snack, or drink", headline="Earned",
                     voucher_code="----------", barcode_type=None, progress_display_text="7/7 butterflies",
                     current_value="7", target_value="7", prefix=None, suffix="butterflies",
                     body_text="Congrats! You've earned a free itsu dish, snack or drink. Simply download the itsu "
                               "app from the Google Play Store or App Store to redeem.",
                     terms_and_conditions="https://policies.staging.gb.bink.com/itsu/tc.html", issued_date="1684750290",
                     expiry_date="1905638340", redeemed_date=None, conversion_date=None),
                {
                    "state": "issued",
                    "earn_type": "stamps",
                    "reward_text": "Free dish, snack, or drink",
                    "headline": "Earned",
                    "voucher_code": "----------",
                    "barcode_type": None,
                    "progress_display_text": "7/7 butterflies",
                    "current_value": "7",
                    "target_value": "7",
                    "prefix": None,
                    "suffix": "butterflies",
                    "body_text": "Congrats! You've earned a free itsu dish, snack or drink. Simply download the itsu "
                                 "app from the Google Play Store or App Store to redeem.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/itsu/tc.html",
                    "issued_date": "1683902926",
                    "expiry_date": "1916956800",
                    "redeemed_date": None,
                    "conversion_date": None
                }

            ],
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "9988776655",
                "colour": "#e70095",
                "text_colour": None,
            },
            "reward_available": True,
            "images": [
                {
                    "id": 1416,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Hero.png",
                    "description": "itsu Loyalty Card",
                    "encoding": "png",
                    "cta_url": None
                },
                {
                    "id": 1417,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Icon.png",
                    "description": "itsu Logo",
                    "encoding": "png",
                    "cta_url": None
                }
            ],
        }
        return wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
            "loyalty_plan_id": 295,
            "loyalty_plan_name": "itsu loyalty",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1688658362,
                "current_display_value": "5 stamps",
                "loyalty_currency_name": "stamps",
                "prefix": None,
                "suffix": "stamps",
                "current_value": "5",
                "target_value": "7",
            },
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "9988776655",
                "colour": "#e70095",
                "text_colour": None,
            },
            "reward_available": True,
            "images": [
                {
                    "id": 1416,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Hero.png",
                    "description": "itsu Loyalty Card",
                    "encoding": "png",
                    "cta_url": None
                }
            ],
        }
        return wallet_overview_info

    @staticmethod
    def wallet_unauth_response():
        unauth_wallet_info = {
            "loyalty_plan_id": 295,
            "loyalty_plan_name": "itsu loyalty",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "unauthorised",
                "slug": "VALIDATION_ERROR",
                "description": "We can’t link your card as some details don’t match what the retailer has."
                " Please check your details and enter them into the form again. If this doesn’t work, "
                "please speak to the retailer, or re-join their loyalty scheme in Loyalty Plus.",
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
                "card_number": "9988776655",
                "colour": "#e70095",
                "text_colour": None,
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1416,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Hero.png",
                    "description": "itsu Loyalty Card",
                    "encoding": "png",
                    "cta_url": None
                },
                {
                    "id": 1417,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Icon.png",
                    "description": "itsu Logo",
                    "encoding": "png",
                    "cta_url": None
                },
            ],
        }
        return unauth_wallet_info

    @staticmethod
    def wallet_overview_unauth_response():
        unauth_wallet_overview_info = {
            "loyalty_plan_id": 295,
            "loyalty_plan_name": "itsu loyalty",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "unauthorised",
                "slug": "VALIDATION_ERROR",
                "description": "We can’t link your card as some details don’t match what the retailer has. "
                "Please check your details and enter them into the form again. If this doesn’t work, "
                "please speak to the retailer, or re-join their loyalty scheme in Loyalty Plus.",
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
                "card_number": "9988776655",
                "colour": "#e70095",
                "text_colour": None,
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1416,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/itsu_Hero.png",
                    "description": "itsu Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return unauth_wallet_overview_info
