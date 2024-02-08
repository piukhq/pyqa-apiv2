class TheWorksResponse:
    @staticmethod
    def wallet_response():
        wallet_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1688658362,
                "current_display_value": "60 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "60",
                "target_value": None,
            },
            "transactions": [
                {
                    # "id": "750316",
                    "timestamp": 1687190168,
                    "description": "Available balance: £0.00",
                    "display_value": "5 pts",
                },
                {
                    # "id": "750317",
                    "timestamp": 1687188672,
                    "description": "Available balance: £0.00",
                    "display_value": "25 pts",
                },
                {
                    # "id": "750318",
                    "timestamp": 1687182362,
                    "description": "Available balance: £0.00",
                    "display_value": "15 pts",
                },
                {
                    # "id": "750319",
                    "timestamp": 1687176061,
                    "description": "Available balance: £0.00",
                    "display_value": "10 pts",
                },
                {
                    # "id": "750320",
                    "timestamp": 1687171741,
                    "description": "Available balance: £0.00",
                    "display_value": "5 pts",
                },
            ],
            "vouchers": [],
            "card": {
                "barcode": "6338849749210000002622",
                "barcode_type": 0,
                "card_number": "6338849749210000002622",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1414,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Icon.png",
                    "description": "The Works Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return wallet_info

    @staticmethod
    def wallet_overview_response():
        wallet_overview_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1688658362,
                "current_display_value": "60 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "60",
                "target_value": None,
            },
            "card": {
                "barcode": "6338849749210000002622",
                "barcode_type": 0,
                "card_number": "6338849749210000002622",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return wallet_overview_info

    @staticmethod
    def wallet_unauth_response():
        unauth_wallet_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
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
                "barcode": "633884102938475600011",
                "barcode_type": 0,
                "card_number": "633884102938475600011",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1414,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Icon.png",
                    "description": "The Works Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return unauth_wallet_info

    @staticmethod
    def wallet_overview_unauth_response():
        unauth_wallet_overview_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
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
                "barcode": "633884102938475600011",
                "barcode_type": 0,
                "card_number": "633884102938475600011",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                }
            ],
        }
        return unauth_wallet_overview_info

    @staticmethod
    def register_success_wallet_response():
        register_success_wallet_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1687772129,
                "current_display_value": "0 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "0",
                "target_value": None,
            },
            "transactions": [],
            "vouchers": [],
            "card": {
                "barcode": "6338844992910000029726",
                "barcode_type": 0,
                "card_number": "6338844992910000029726",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1414,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Icon.png",
                    "description": "The Works Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return register_success_wallet_info

    """This response is same for ghost_card_registration_failed_non_retryable_http_error
    and other non_retryable_error."""

    @staticmethod
    def register_failed_wallet_response():
        register_failed_wallet_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
            "is_fully_pll_linked": False,
            "pll_linked_payment_accounts": 0,
            "total_payment_accounts": 1,
            "status": {
                "state": "failed",
                "slug": "REGISTRATION_FAILED",
                "description": "The retailer couldn't process your request, so we can't "
                               "register your details. To help fix this, check the card "
                                "number, select 'Remove loyalty card', then start again. If it "
                                "still doesn't work, please speak to the retailer.",
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
                "barcode": "6338844992910000029726",
                "barcode_type": 0,
                "card_number": "6338844992910000029726",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1414,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Icon.png",
                    "description": "The Works Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return register_failed_wallet_info

    @staticmethod
    def join_success_wallet_response():
        join_success_wallet_info = {
            "loyalty_plan_id": 294,
            "loyalty_plan_name": "Together Rewards",
            "is_fully_pll_linked": True,
            "pll_linked_payment_accounts": 1,
            "total_payment_accounts": 1,
            "status": {"state": "authorised", "slug": None, "description": None},
            "balance": {
                # "updated_at": 1687536746,
                "current_display_value": "0 pts",
                "loyalty_currency_name": "points",
                "prefix": None,
                "suffix": "pts",
                "current_value": "0",
                "target_value": None,
            },
            "transactions": [],
            "vouchers": [],
            "card": {
                # "barcode": "6338847707382846345717",
                "barcode_type": 0,
                # "card_number": "6338847707382846345717",
                "colour": "#fff200",
                "text_colour": "#FFFFFF",
            },
            "reward_available": False,
            "images": [
                {
                    "id": 1414,
                    "type": 3,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Icon.png",
                    "description": "The Works Logo",
                    "encoding": "png",
                    "cta_url": None,
                },
                {
                    "id": 1415,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/The_Works_Hero_jel2vZz.png",
                    "description": "The Works Loyalty Card",
                    "encoding": "png",
                    "cta_url": None,
                },
            ],
        }
        return join_success_wallet_info

    # @staticmethod
    # def join_failed_wallet_response():
    #     join_failed_wallet_info = {}
    #     return join_failed_wallet_info
    #
    #
    # @staticmethod
    # def join_account_already_exist_wallet_response():
    #     join_account_already_exist_wallet_info = {}
    #     return join_account_already_exist_wallet_info
