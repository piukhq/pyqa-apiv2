from os import environ

from tests_resources.test_data import testdata_dev, testdata_sandbox, testdata_staging


class EnvironmentDetails:
    def __init__(self, base_url, test_data):
        self.base_url = base_url
        self.test_data = test_data


if "KUBERNETES_SERVICE_HOST" in environ:
    DEV = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_dev)
    STAGING = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_staging)
    TRUSTED = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_staging)
    SANDBOX = EnvironmentDetails(base_url="http://angelia-api", test_data=testdata_sandbox)
else:
    DEV = EnvironmentDetails(base_url="https://api.dev.gb.bink.com", test_data=testdata_dev)
    STAGING = EnvironmentDetails(base_url="https://api.staging.gb.bink.com", test_data=testdata_staging)
    TRUSTED = EnvironmentDetails(base_url="https://tc.staging.gb.bink.com", test_data=testdata_staging)
    SANDBOX = EnvironmentDetails(base_url="https://lloyds-sit.sandbox.gb.bink.com", test_data=testdata_sandbox)


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
    channel_name="Lloyds",
    bundle_id="com.lloydsqa.api2",
    client_id="LkVR4URcysf22a10Jpm3QXVmSGD8neUwgLo7JBSKtDxlV8zZJr",
    kid="lloydsqa-bink-regression",
    organisation_id="",
)

BARCLAYS = ChannelDetails(
    channel_name="barclays",
    bundle_id="com.barclays.bmb",
    client_id="lwhkGNn5FAXPCCcbIFrgZWk0i7Qolg5WBMFM4UYjZAbaOXQyq6",
    kid="barclays-bink-regression",
    organisation_id="",
)

HALIFAX = ChannelDetails(
    channel_name="halifax",
    bundle_id="com.halifax.api2",
    client_id="8eBiL5Vh7AKKkWOezW5Avv8olfhK3to9ToqiypzPbOiBj5XEIv",
    kid="halifax-bink-regression",
    organisation_id="",
)

BOS = ChannelDetails(
    channel_name="bos",
    bundle_id="com.bos.api2",
    client_id="8eBiL5Vh7AKKkWOezW5Avv8olfhK3to9ToqiypzPbOiBj5XEIv",
    kid="bos-bink-regression",
    organisation_id="",
)

SQUAREMEAL = ChannelDetails(
    channel_name="squaremeal",
    bundle_id="com.squaremeal.api2",
    client_id="Ngc7PzJM20zQMXhy8ZoTlAOrePGOkmLkqz0DCBSVcUJTcPkgNz",
    kid="squaremeal-bink-regression",
    organisation_id="",
)
