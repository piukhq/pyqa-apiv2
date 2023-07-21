class IcelandResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
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
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 374,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                    "description": "Iceland Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 373,
                    "type": 4,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                    "description": "Iceland Asset",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1070,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1071,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1072,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1303,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                    "description": "Iceland Offer - Greggs",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/frozen-pies/greggs",
                },
                {
                    "id": 1302,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                    "description": "Iceland Offer - Pizza",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/pizza-and-garlic-bread/wood-fired-pizzas",
                },
                {
                    "id": 1398,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "PromotionsIcelandBonusCard1968x732.png",
                    "description": "Promo_Text_1",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_info

    @staticmethod
    def lc2_wallet_response():
        lc2_wallet_info = {
            # "id": 261658,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1675695071,
                # "current_display_value": "£20.10",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                # "current_value": "20.10",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "575342",
                    "timestamp": 1639505216,
                    "description": "CREDIT",
                    "display_value": "£1",
                },
                {
                    # "id": "575343",
                    "timestamp": 1626767059,
                    "description": "CREDIT",
                    "display_value": "£1.15",
                },
                {
                    # "id": "575344",
                    "timestamp": 1626605058,
                    "description": "CREDIT",
                    "display_value": "£5",
                },
                {
                    # "id": "575346",
                    "timestamp": 1623030929,
                    "description": "DEBIT",
                    "display_value": "-£5.50",
                },
                {
                    # "id": "575345",
                    "timestamp": 1622685329,
                    "description": "DEBIT",
                    "display_value": "-£2",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": "63320400123123543210080",
                "barcode_type": 0,
                "card_number": "6332040012312354321",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 374,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                    "description": "Iceland Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 373,
                    "type": 4,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                    "description": "Iceland Asset",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1070,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1071,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1072,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1303,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                    "description": "Iceland Offer - Greggs",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/frozen-pies/greggs",
                },
                {
                    "id": 1302,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                    "description": "Iceland Offer - Pizza",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/pizza-and-garlic-bread/wood-fired-pizzas",
                },
                {
                    "id": 1398,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "PromotionsIcelandBonusCard1968x732.png",
                    "description": "Promo_Text_1",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return lc2_wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
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
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return wallet_overview_info

    @staticmethod
    def lc2_wallet_overview_response():
        lc2_wallet_overview_info = {
            # "id": 261658,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1675695071,
                # "current_display_value": "£20.10",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                # "current_value": "20.10",
                "target_value": None,
            },
            "card": {
                "barcode": "63320400123123543210080",
                "barcode_type": 0,
                "card_number": "6332040012312354321",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return lc2_wallet_overview_info

    @staticmethod
    def wallet_unauth_response():
        unauth_wallet_info = {
            # "id": 210732,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
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
                # "barcode": None,
                "barcode_type": 0,
                # "card_number": "6332040000000000007",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 374,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                    "description": "Iceland Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 373,
                    "type": 4,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                    "description": "Iceland Asset",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1070,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1071,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1072,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1303,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                    "description": "Iceland Offer - Greggs",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/frozen-pies/greggs",
                },
                {
                    "id": 1302,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                    "description": "Iceland Offer - Pizza",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/pizza-and-garlic-bread/wood-fired-pizzas",
                },
                {
                    "id": 1398,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "PromotionsIcelandBonusCard1968x732.png",
                    "description": "Promo_Text_1",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return unauth_wallet_info

    @staticmethod
    def wallet_overview_unauth_response():
        unauth_wallet_overview_info = {
            # "id": 210732,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
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
            "card": {
                # "barcode": None,
                "barcode_type": 0,
                # "card_number": "6332040000000000007",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return unauth_wallet_overview_info

    @staticmethod
    def register_success_wallet_response():
        register_success_wallet_info = {
            # "id": 204521,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1662999593,
                "current_display_value": "£0",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "0",
                "target_value": None,
            },
            "transactions": [],
            "vouchers": [],
            "card": {
                "barcode": "66332040065432100000080",
                "barcode_type": 0,
                "card_number": "6633204006543210000",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
        }
        return register_success_wallet_info

    @staticmethod
    def register_failed_wallet_response():
        register_failed_wallet_info = {
            # "id": 204517,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "failed",
                "slug": "ACCOUNT_NOT_REGISTERED",
                "description": "The Loyalty Card has not yet been registered. "
                "Please register the card with the retailer.",
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
                # "barcode": None,
                "barcode_type": 0,
                "card_number": "6633204006543210000",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
        }
        return register_failed_wallet_info

    @staticmethod
    def register_pending_wallet_response():
        register_pending_wallet_info = {
            # "id": 204521,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {"state": "pending", "slug": "REGISTRATION_IN_PROGRESS", "description": None},
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
                "barcode_type": 0,
                "card_number": "6333333365432156789",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
        }
        return register_pending_wallet_info

    @staticmethod
    def join_success_wallet_response():
        join_success_wallet_info = {
            # "id": 205106,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1663165070,
                "current_display_value": "£0",
                "loyalty_currency_name": "GBP",
                "prefix": "£",
                "suffix": None,
                "current_value": "0",
                "target_value": None,
            },
            "transactions": [],
            "vouchers": [],
            "card": {
                # "barcode": "63320400569935736110080",
                "barcode_type": 0,
                # "card_number": "6332040056993573611",
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 374,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Logo.png",
                    "description": "Iceland Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 373,
                    "type": 4,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland-asset.png",
                    "description": "Iceland Asset",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1070,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_ref1.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1071,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref2.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1072,
                    "type": 5,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/iceland_ref3.jpg",
                    "description": "Iceland Reference",
                    "encoding": "jpg",
                    "cta_url": None,
                },
                {
                    "id": 1234,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Card.png",
                    "description": "Iceland Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1303,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Greggs.jpg",
                    "description": "Iceland Offer - Greggs",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/frozen-pies/greggs",
                },
                {
                    "id": 1302,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/Iceland_Offer_Pizza.jpg",
                    "description": "Iceland Offer - Pizza",
                    "encoding": "jpg",
                    "cta_url": "https://www.iceland.co.uk/frozen/pizza-and-garlic-bread/wood-fired-pizzas",
                },
                {
                    "id": 1398,
                    "type": 7,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/"
                    "PromotionsIcelandBonusCard1968x732.png",
                    "description": "Promo_Text_1",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return join_success_wallet_info

    @staticmethod
    def join_failed_wallet_response():
        join_failed_wallet_info = {
            # "loyalty_card_id": 193492,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "status": {
                "state": "failed",
                "slug": "JOIN_FAILED",
                "description": "The retailer has not been able to accept your request at this time. "
                "Please remove the request and try again.",
            },
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": None,
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
        }
        return join_failed_wallet_info

    @staticmethod
    def join_pending_wallet_response():
        join_pending_wallet_info = {
            # "loyalty_card_id": 193506,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "status": {"state": "pending", "slug": "JOIN_IN_PROGRESS", "description": None},
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": None,
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
        }
        return join_pending_wallet_info

    @staticmethod
    def join_account_already_exist_wallet_response():
        join_account_already_exist_wallet_info = {
            # "id": 200357,
            "loyalty_plan_id": 105,
            "loyalty_plan_name": "Iceland Bonus Card",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
            "status": {
                "state": "failed",
                "slug": "ACCOUNT_ALREADY_EXISTS",
                "description": "A Loyalty Card matching the entered credentials already exists. "
                "Please add this Loyalty Card to your wallet.",
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
                "barcode_type": 0,
                "card_number": None,
                "colour": "#d50724",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
        }
        return join_account_already_exist_wallet_info
