class ViatorResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
            # "id": 276875,
            "loyalty_plan_id": 292,
            "loyalty_plan_name": "Viator Discounts",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1679504220,
                "current_display_value": "£0.11",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "0.11",
                "target_value": "200",
            },
            "transactions": [
                {
                    # "id": "605095",
                    "timestamp": 1678199304,
                    "description": "N/A £200.11",
                    "display_value": "£200.11",
                }
            ],
            "vouchers": [
                {
                    "state": "inprogress",
                    "earn_type": "accumulator",
                    "reward_text": "10% off discount",
                    "headline": "Spend £200 to get a 10% off Viator voucher code",
                    "voucher_code": None,
                    "barcode_type": None,
                    "progress_display_text": "£0.11/£200",
                    "current_value": "0.11",
                    "target_value": "200",
                    "prefix": "£",
                    "suffix": None,
                    "body_text": "Spend £200 to get a 10% off Viator voucher code.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/Viator/rewardtc.html",
                    "issued_date": None,
                    "expiry_date": None,
                    "redeemed_date": None,
                    "conversion_date": None,
                },
                {
                    "state": "pending",
                    "earn_type": "accumulator",
                    "reward_text": "10% off discount",
                    "headline": "Pending",
                    "voucher_code": "pending",
                    "barcode_type": None,
                    "progress_display_text": "£200/£200",
                    "current_value": "200",
                    "target_value": "200",
                    "prefix": "£",
                    "suffix": None,
                    "body_text": "You've earned a Viator reward. "
                    "All you need to do now is wait for your code to show "
                    "here after 10 days (just to allow for any returns to register "
                    "in our system). Use your Viator discount reward at checkout on your next purchase.",
                    "terms_and_conditions": "https://policies.staging.gb.bink.com/Viator/rewardtc.html",
                    "issued_date": "1678147200",
                    "expiry_date": None,
                    "redeemed_date": None,
                    "conversion_date": "1807369200",
                },
            ],
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "VIAT0522355816",
                "colour": "#246b6c",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1411,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Logo1-280x280.png",
                    "description": "Viator Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1409,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Loyalty_Card_V2_1312x800.png",
                    "description": "Viator Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1412,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Viator_Barclays_Promotional_Image.png",
                    "description": "Viator Promotion",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
            # "id": 276875,
            "loyalty_plan_id": 292,
            "loyalty_plan_name": "Viator Discounts",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1679506295,
                "current_display_value": "£0.11",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "0.11",
                "target_value": "200",
            },
            "card": {
                "barcode": None,
                "barcode_type": None,
                "card_number": "VIAT0522355816",
                "colour": "#246b6c",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1409,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Loyalty_Card_V2_1312x800.png",
                    "description": "Viator Loyalty Card",
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
                    "id": 1319,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "Offer_tile_5_CVAeqUv_naFzo9T.png",
                    "description": "Wasabi Test Offer",
                    "encoding": "png",
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
