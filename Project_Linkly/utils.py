import db, random, string, requests
from urllib.parse import urlparse
import gen_code_helper

# Base58 alphabet (excluding confusing chars like 0, O, l, I)
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


# ------------------------------
# Main short-code generator
# ------------------------------
def generate_next_code():
    """Return next short code as 6-char Base58 string using seed & cipher."""
    last_code = db.my_db.get_last_short_code()
    if not last_code:
        # --- No previous URL, use base key ---
        base = db.my_db.get_base_key()
    else:
        last_code = last_code[-6:]
        print(last_code)
        # --- Decode last code ---
        last_indices = gen_code_helper.string_to_indices(last_code)
        # reverse cipher first to get numeric sequence
        decoded = gen_code_helper.remove_cipher(last_indices)
        # increment
        base = gen_code_helper.prime_increment_base58(decoded)

    # Apply cipher again and convert to string
    ciphered = gen_code_helper.apply_cipher(base)
    short_code = gen_code_helper.indices_to_string(ciphered)
    return short_code


def generate_short_code(length=6):
    # use base 58 encoding to create a random short_code
    return "".join(random.choices(BASE58_ALPHABET, k=length))


def validate_url(link):
    # check if url exists or is up
    parsed = urlparse(link)
    if not (parsed.scheme and parsed.netloc):
        return False
    try:
        requests.head(link, timeout=5)
        return True
    except requests.RequestException:
        return False
