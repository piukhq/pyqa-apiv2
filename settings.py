import logging
import os

from environment import env_var, read_env

os.chdir(os.path.dirname(__file__))
read_env()

logging.basicConfig(format="%(process)s %(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("automation_tests_logger")
logger.setLevel(logging.DEBUG)

LOCAL_CHANNELS = env_var("LOCAL_CHANNELS", False)
LOCAL_SECRETS_PATH = env_var("LOCAL_SECRETS_PATH", "tests/helpers/vault/local_channels.json")
VAULT_URL_STAGING = env_var("VAULT_URL", "https://uksouth-staging-232w.vault.azure.net")
VAULT_URL_SANDBOX = env_var("VAULT_URL", "https://bink-uksouth-lloyds-sit.vault.azure.net")
CHANNEL_SECRET_NAME = env_var("CHANNEL_SECRET_NAME", "channels")
ACCESS_SECRET_NAME = env_var("ACCESS_SECRET_NAME", "api2-access-secrets")
B2B_BINK_PRIVATE_KEY = env_var("B2B_BINK_PRIVATE_KEY", "api2-b2b-private-key-bink-regression")
B2B_LLOYDS_PRIVATE_KEY = env_var("B2B_LLOYDS_PRIVATE_KEY", "api2-b2b-private-key-lloydsqa-regression")
B2B_HALIFAX_PRIVATE_KEY = env_var("B2B_HALIFAX_PRIVATE_KEY", "api2-b2b-private-key-halifax-regression")
B2B_BOS_PRIVATE_KEY = env_var("B2B_BOS_PRIVATE_KEY", "api2-b2b-private-key-bos-regression")
B2B_SQUAREMEAL_PRIVATE_KEY = env_var("B2B_SQUAREMEAL_PRIVATE_KEY", "api2-b2b-private-key-sqrmeal-regression")
BLOB_STORAGE_DSN = env_var("BLOB_STORAGE_DSN")
HERMES_DATABASE_URI = env_var("HERMES_DATABASE_URI","postgresql://warthog:elsJ1XgVizFhQmX5mIl8dz52@uksouth-staging-2o6h.postgres.database.azure.com/hermes?sslmode=require")
HARMONIA_DATABASE_URI = env_var("HARMONIA_DATABASE_URI")
SNOWSTORM_DATABASE_URI = env_var("SNOWSTORM_DATABASE_URI","postgresql://warthog:elsJ1XgVizFhQmX5mIl8dz52@127.0.0.1/snowstorm?sslmode=require")
                                #  "postgresql://warthog:elsJ1XgVizFhQmX5mIl8dz52@uksouth-staging-2o6h.postgres.database.azure.com/snowstorm?sslmode=require")
