import os

# Gost doesn't seem to work.

NONFIPS_DIGESTS = (
    "blake2b512",
    "blake2s256",
    # "gost",
    "md4",
    "md5",
    "mdc2",
    "rmd160",
    "sm3",
)

FIPS_DIGESTS = (
    "sha1",
    "sha224",
    "sha256",
    "sha3-224",
    "sha3-256",
    "sha3-384",
    "sha3-512",
    "sha384",
    "sha512",
    "sha512-224",
    "sha512-256",
    "shake128",
    "shake256",
)

ALL_DIGESTS = NONFIPS_DIGESTS + FIPS_DIGESTS


def host_fips_supported(fipsfile: str = "/proc/sys/crypto/fips_enabled"):
    return os.path.exists(fipsfile)


def host_fips_enabled(fipsfile: str = "/proc/sys/crypto/fips_enabled"):
    if not host_fips_supported(fipsfile):
        return False

    with open(fipsfile) as f:
        return f.read().strip() == "1"
