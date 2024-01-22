import json
import logging
import os

from base64 import b32decode, b32encode
from datetime import datetime, timedelta
from typing import Optional

from Crypto.PublicKey import RSA
from jwcrypto import jwe as crypto_jwe
from jwcrypto import jwk


class JweException(Exception):
    pass


class JweServerError(Exception):
    pass


class JWE:
    """
    This class is for handling JWE token encryption and decryption using the jwcrypto library and azure vault for
    key storage.

    Encryption/Decryption require RSA keys that are stored in the vault. These keys are stored in "key objects"
    containing the public key, private key, and the datetime of their expiry as a unix timestamp e.g:

    {
        "public_key": ...,
        "private_key": ...,
        "expires_at": 1234234234.3423
    }

    The secret name under which they are stored have a standard format, containing information about the channel which
    the keys relate, and the thumbprint of the public key in base32. Generation of the secret name and key objects
    can be done using the utility functions in this module.

    All errors raised are subclasses of falcon.HTTPError to handle API responses.
    """

    # Available algorithms
    allowed_algs = [
        # Key Management Algorithms
        "RSA-OAEP",
        "RSA-OAEP-256",
        # Content Encryption Algorithms
        "A128CBC-HS256",
        "A192CBC-HS384",
        "A256CBC-HS512",
        "A128GCM",
        "A192GCM",
        "A256GCM",
    ]

    def __init__(self):
        self.public_key: Optional[jwk.JWK] = None
        self.private_key: Optional[jwk.JWK] = None
        self.token: crypto_jwe.JWE = crypto_jwe.JWE(algs=self.allowed_algs)

    @staticmethod
    def _get_key_from_pem(key_pem: str) -> jwk.JWK:
        key = jwk.JWK()
        try:
            key.import_from_pem(key_pem.encode())
        except ValueError:
            raise JweServerError
        return key

    def encrypt(
        self,
        payload: str,
        alg: str = "RSA-OAEP",
        enc: str = "A256CBC-HS512",
        public_key_pem: str = None,
        kid: str = None,
        compact: bool = True,
    ) -> str:
        if public_key_pem:
            self.public_key = self._get_key_from_pem(public_key_pem)

        protected_header = {
            "alg": alg,
            "enc": enc,
            "typ": "JWE",
            "kid": self.public_key.thumbprint(),
        }
        jwe_token = crypto_jwe.JWE(
            payload.encode("utf-8"),
            recipient=self.public_key,
            protected=protected_header,
        )
        return jwe_token.serialize(compact=compact)


# Utilities ####################################################################################


# Padding stripping versions of base32
# as described for base64 in RFC 7515 Appendix C
def base32_encode(payload):
    if not isinstance(payload, bytes):
        payload = payload.encode("utf-8")
    encode = b32encode(payload)
    return encode.decode("utf-8").rstrip("=")


def base32_decode(payload):
    last_block_width = len(payload) % 8
    if last_block_width != 0:
        payload += (8 - last_block_width) * "="
    return b32decode(payload.encode("utf-8"))


def gen_rsa_keypair(priv_path: str, pub_path: str):
    key = RSA.generate(2048)

    private_key = open(priv_path, "wb")
    private_key.write(key.export_key("PEM"))
    private_key.close()

    pub = key.public_key()
    pub_key = open(pub_path, "wb")
    pub_key.write(pub.export_key("PEM"))
    pub_key.close()


def gen_vault_key_obj(channel_slug, priv, pub, mins_to_expire=60 * 24, paths=True) -> tuple[str, dict]:
    pub_key = jwk.JWK()

    if paths:
        priv = os.path.abspath(priv)
        pub = os.path.abspath(pub)

        with open(pub, "rb") as f:
            pub_key_pem = f.read()
            pub_key.import_from_pem(pub_key_pem)
            pub_key_pem = pub_key_pem.decode()

        with open(priv, "rb") as f:
            priv_key_pem = f.read()
            priv_key_pem = priv_key_pem.decode()

    else:
        pub_key.import_from_pem(pub.encode())
        pub_key_pem = pub
        priv_key_pem = priv

    jwe_kid = pub_key.thumbprint()

    azure_kid = f"jwe-{channel_slug.removeprefix('com.').replace('.', '-')}-{base32_encode(jwe_kid)}"
    expiry = datetime.now() + timedelta(minutes=mins_to_expire)
    value = {
        "public_key": pub_key_pem,
        "private_key": priv_key_pem,
        "expires_at": expiry.timestamp(),
    }

    print(
        "FOR TESTING PURPOSES OR LOCAL USE ONLY\nAzure secret name:"
        f"\n{azure_kid}\n\nValue:\n{json.dumps(value, indent=4)}\n\n"
    )
    return azure_kid, value


def manual_encrypt(data: dict, pub_key_path: str = None, kid: str = None):
    """
    A simplified, more user-friendly encryption function that allows providing a filepath to a public key.

    Can be used as a helper tool for manual testing with encryption.
    """
    if not (pub_key_path or kid):
        raise ValueError("pub_key_path or kid required")

    jwe = JWE()

    if pub_key_path:
        with open(pub_key_path, "r") as f:
            pub_key_pem = f.read()
        token = jwe.encrypt(json.dumps(data), public_key_pem=pub_key_pem)
    else:
        token = jwe.encrypt(json.dumps(data), kid=kid)

    return json.dumps(token)


def encrypted_payload_token(payload):
    token = manual_encrypt(payload, pub_key_path="rsa.pub")
    logging.info("The encrypted request for the journey is :\n" + token)
    return token
