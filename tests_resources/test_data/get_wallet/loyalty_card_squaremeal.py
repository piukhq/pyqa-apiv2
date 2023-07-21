class SquareMealResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
            # "id": 230144,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1668095818,
                "current_display_value": "800 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "800",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "506864",
                    "timestamp": 1640772734,
                    "description": "First Card Added",
                    "display_value": "100 pts",
                },
                {
                    # "id": "506866",
                    "timestamp": 1639769134,
                    "description": "Dining at Camino Bankside",
                    "display_value": "500 pts",
                },
                {
                    # "id": "506865",
                    "timestamp": 1639592114,
                    "description": "Registration",
                    "display_value": "100 pts",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": "10050000",
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1328,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Icon.png",
                    "description": "SquareMeal Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1331,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Bronze_Tier_1.png",
                    "description": "SquareMeal Bronze Tier Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_info

    @staticmethod
    def lc2_wallet_response():
        lc2_wallet_info = {
            # "id": 232313,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1668599502,
                "current_display_value": "900 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "900",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "512307",
                    "timestamp": 1640772734,
                    "description": "First Card Added",
                    "display_value": "100 pts",
                },
                {
                    # "id": "512309",
                    "timestamp": 1639769134,
                    "description": "Dining at Camino Bankside",
                    "display_value": "500 pts",
                },
                {
                    # "id": "512308",
                    "timestamp": 1639592114,
                    "description": "Registration",
                    "display_value": "100 pts",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": "10010012",
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1328,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Icon.png",
                    "description": "SquareMeal Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1331,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Bronze_Tier_1.png",
                    "description": "SquareMeal Bronze Tier Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return lc2_wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
            # "id": 230144,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1668095818,
                "current_display_value": "800 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "800",
                "target_value": None,
            },
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": "10050000",
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1331,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Bronze_Tier_1.png",
                    "description": "SquareMeal Bronze Tier Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return wallet_overview_info

    @staticmethod
    def lc2_wallet_overview_response():
        lc2_wallet_overview_info = {
            # "id": 243832,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1671445885,
                "current_display_value": "900 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "900",
                "target_value": None,
            },
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": "10010012",
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1331,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Bronze_Tier_1.png",
                    "description": "SquareMeal Bronze Tier Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return lc2_wallet_overview_info

    @staticmethod
    def wallet_lc2_only_in_tc():
        wallet_lc2_only_in_tc = {
            # "id": 324657,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
            "status": {"state": "authorised", "slug": None, "description": None},
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
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1328,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Icon.png",
                    "description": "SquareMeal Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1330,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Hero.png",
                    "description": "SquareMeal Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_lc2_only_in_tc

    @staticmethod
    def wallet_overview_lc2_only_in_tc():
        wallet_overview_lc2_only_in_tc = {
            # "id": 324657,
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
            "status": {"state": "authorised", "slug": None, "description": None},
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
                "barcode_type": 0,
                "card_number": None,
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1330,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Hero.png",
                    "description": "SquareMeal Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return wallet_overview_lc2_only_in_tc

    @staticmethod
    def wallet_unauth_response():
        unauth_wallet_info = {
            "loyalty_plan_id": 286,
            "loyalty_plan_name": "SquareMeal Restaurant Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 0,
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
            "transactions": [],
            "vouchers": [],
            "card": {
                "barcode": None,
                "barcode_type": 0,
                "card_number": None,
                "colour": "#465560",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1328,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Icon.png",
                    "description": "SquareMeal Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1330,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/media/hermes/schemes/SquareMeal_Hero.png",
                    "description": "SquareMeal Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return unauth_wallet_info
