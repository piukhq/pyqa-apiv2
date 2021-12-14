from os import environ

from tests_resources.test_data import testdata_dev, testdata_staging


class EnvironmentDetails:
    def __init__(self, base_url, test_data):
        self.base_url = base_url
        self.test_data = test_data


if "KUBERNETES_SERVICE_HOST" in environ:
    DEV = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_dev)
    STAGING = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_staging)
else:
    DEV = EnvironmentDetails(base_url="https://api.dev.gb.bink.com", test_data=testdata_dev)
    STAGING = EnvironmentDetails(base_url="https://api.staging.gb.bink.com", test_data=testdata_staging)


class ChannelDetails:
    def __init__(self, channel_name, bundle_id, client_id, organisation_id, kid):
        self.channel_name = channel_name
        self.bundle_id = bundle_id
        self.client_id = client_id
        self.organisation_id = organisation_id
        self.kid = kid


BINK = ChannelDetails(
    channel_name="bink",
    bundle_id="com.bink.wallet",
    client_id="MKd3FfDGBi1CIUQwtahmPap64lneCa2R6GvVWKg6dNg4w9Jnpd",
    kid="bink-bink-regression",
    organisation_id="",
)

LLOYDS = ChannelDetails(
    channel_name="lloyds",
    bundle_id="com.lloyds.api2",
    client_id="8eBiL5Vh7AKKkWOezW5Avv8olfhK3to9ToqiypzPbOiBj5XEIv",
    kid="lloyds-bink-regression",
    organisation_id="",
)
