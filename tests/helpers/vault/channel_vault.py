import datetime
import json
import logging
import time

from enum import Enum

import jwt
import requests

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError, ServiceRequestError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from settings import ACCESS_SECRET_NAME, CHANNEL_SECRET_NAME, LOCAL_CHANNELS, LOCAL_SECRETS_PATH, VAULT_URL

logger = logging.getLogger(__name__)
loaded = False
_bundle_secrets = {}
_access_secrets = {}

logging.basicConfig(level=logging.INFO)
logging.getLogger("azure").setLevel(logging.ERROR)


class KeyType(str, Enum):
    PRIVATE_KEY = "private_key"
    PUBLIC_KEY = "public_key"


class KeyVaultError(Exception):
    pass


def retry_get_secrets_from_vault():
    retries = 3
    exception = RuntimeError("Failed to get secrets from Vault")
    for _ in range(retries):
        try:
            client = SecretClient(vault_url=VAULT_URL, credential=DefaultAzureCredential())
            secret = client.get_secret(CHANNEL_SECRET_NAME)
            try:
                return json.loads(secret.value)
            except json.decoder.JSONDecodeError:
                return secret.value
        except (ServiceRequestError, ResourceNotFoundError, HttpResponseError) as e:
            exception = e
            time.sleep(3)

    raise exception


def retry_get_access_secrets_from_vault():
    retries = 3
    exception = RuntimeError("Failed to get access secrets from Vault")
    for _ in range(retries):
        try:
            client = SecretClient(vault_url=VAULT_URL, credential=DefaultAzureCredential())
            secret = client.get_secret(ACCESS_SECRET_NAME)
            try:
                return json.loads(secret.value)
            except json.decoder.JSONDecodeError:
                return secret.value
        except (ServiceRequestError, ResourceNotFoundError, HttpResponseError) as e:
            exception = e
            time.sleep(3)

    raise exception


def load_secrets():
    """
    Retrieves security credential values from channel storage vault and stores them
    in _bundle_secrets which are used as a cache.
    Secrets contained in _bundle_secrets are bundle specific.

    Example:

    _bundle_secrets = {
        "com.bink.wallet": {"key": "value"}
    }

    """
    global loaded
    global _bundle_secrets
    global _access_secrets

    if loaded:
        logger.info("Tried to load the vault secrets more than once, ignoring the request.")

    elif LOCAL_CHANNELS:
        with open(LOCAL_SECRETS_PATH) as fp:
            all_secrets = json.load(fp)

        _bundle_secrets = all_secrets
        loaded = True

    else:
        try:
            bundle_secrets = retry_get_secrets_from_vault()
        except requests.RequestException as e:
            err_msg = f"JWT bundle secrets - Vault Exception {e}"
            logger.exception(err_msg)
            raise KeyVaultError(err_msg) from e

        _bundle_secrets = bundle_secrets
        try:
            _access_secrets = retry_get_access_secrets_from_vault()
        except requests.RequestException as e:
            err_msg = f"Access secret - Vault Exception {e}"
            logger.exception(err_msg)
            raise KeyVaultError(err_msg) from e

        loaded = True


def get_access_secret():
    if not _access_secrets:
        load_secrets()
    try:
        kid = _access_secrets["current_key"]
        secret = _access_secrets[kid]
        return kid, secret
    except KeyError as e:
        raise KeyVaultError(f"Invalid Access secret for bundle: {e}") from e


def check_and_load_vault():
    if not _bundle_secrets:
        load_secrets()


def get_jwt_secret(bundle_id):
    check_and_load_vault()
    try:
        return _bundle_secrets[bundle_id]["jwt_secret"]
    except KeyError as e:
        raise KeyVaultError(f"No JWT secret found for bundle: {bundle_id}") from e


def get_key(bundle_id, key_type: str):
    check_and_load_vault()
    try:
        return _bundle_secrets[bundle_id][key_type]
    except KeyError as e:
        raise KeyVaultError(f"Unable to locate {key_type} in vault for bundle {bundle_id}") from e


def create_bearer_token(sub=None, channel=None, utc_now=None, expire_in=60, prefix="bearer", algorithm="HS512"):
    kid, secret = get_access_secret()
    if utc_now is None:
        iat = datetime.datetime.utcnow()
    else:
        iat = utc_now
    exp = iat + datetime.timedelta(seconds=expire_in)
    payload = {"exp": exp, "iat": iat}
    if channel is not None:
        payload["channel"] = channel
    if sub is not None:
        payload["sub"] = str(sub)
    token = jwt.encode(payload, secret, headers={"kid": kid}, algorithm=algorithm)
    return f"{prefix} {token}"
