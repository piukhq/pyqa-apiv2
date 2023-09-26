class PaymentAccountResponse:
    @staticmethod
    def wallet_payment_account():
        wallet_payment_account = {
            "provider": "Mastercard",
            "issuer": "HSBC",
            "status": "active",
            "type": "debit",
            "currency_code": "GBP",
            "country": "GB",
            "last_four_digits": "5844",
            "images": [
                {
                    "id": 2,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/" "Mastercard-Payment_1goHQYv.png",
                    "description": "Mastercard Hero",
                    "encoding": "png",
                },
                {
                    "id": 32,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "Mastercard_pricelesscities_heathrow.png",
                    "description": "MasterCard Offer Stay - Heathrow",
                    "encoding": "png",
                },
                {
                    "id": 35,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/Mastercard_qkr_app.png",
                    "description": "Master Offer 7 - Qkr",
                    "encoding": "png",
                },
                {
                    "id": 28,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "Mastercard_pricelesscities_moreoffers.png",
                    "description": "MasterCard Offer 6 - More Offers",
                    "encoding": "png",
                },
                {
                    "id": 40,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "Mastercard_pricelesscities_loungepass.png",
                    "description": "MasterCard Offer Stay - Lounge",
                    "encoding": "png",
                },
                {
                    "id": 27,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "Mastercard_pricelesscities_liberty.png",
                    "description": "MasterCard Offer Shop - Liberty",
                    "encoding": "png",
                },
                {
                    "id": 39,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "Mastercard_pricelesscities_market.png",
                    "description": "MasterCard Offer Play - Markets",
                    "encoding": "png",
                },
                {
                    "id": 53,
                    "type": 2,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/"
                    "10773378_MDemand_WFP_BINK_Tile.png",
                    "description": "World Food Programme",
                    "encoding": "png",
                },
            ],
        }
        return wallet_payment_account

    @staticmethod
    def wallet_overview_payment_account():
        wallet_overview_payment_account = {
            # "id": 78816,
            "provider": "Mastercard",
            "issuer": "HSBC",
            "status": "active",
            "type": "debit",
            "currency_code": "GBP",
            "country": "GB",
            "last_four_digits": "5844",
            "images": [
                {
                    "id": 2,
                    "type": 0,
                    "url": "https://api.staging.gb.bink.com/content/hermes/schemes/" "Mastercard-Payment_1goHQYv.png",
                    "description": "Mastercard Hero",
                    "encoding": "png",
                }
            ],
        }
        return wallet_overview_payment_account
