from os import environ


class EnvironmentDetails:
    def __init__(self, transaction_matching_base_url, transaction_matching_base_url_zephyrus):
        self.transaction_matching_base_url = transaction_matching_base_url
        self.transaction_matching_base_url_zephyrus = transaction_matching_base_url_zephyrus


if "KUBERNETES_SERVICE_HOST" in environ:

    STAGING = EnvironmentDetails(
        transaction_matching_base_url="http://skiron-api",
        transaction_matching_base_url_zephyrus="http://zephyrus-api"
    )

    SANDBOX = EnvironmentDetails(
        transaction_matching_base_url="http://skiron-api",
        transaction_matching_base_url_zephyrus="http://zephyrus-api"
    )

    PROD = EnvironmentDetails(
        transaction_matching_base_url="http://skiron-api",
        transaction_matching_base_url_zephyrus="http://zephyrus-api"
    )
else:

    STAGING = EnvironmentDetails(
        transaction_matching_base_url="https://api.staging.gb.bink.com",
        transaction_matching_base_url_zephyrus="https://api.staging.gb.bink.com"
    )
