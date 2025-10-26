import db


# Base58 alphabet (excluding confusing chars like 0, O, l, I)
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
BASE58_ALPHABET = ALPHABET
BASE_KEY, CIPHER_MAP, REVERSE_MAP = (
    db.my_db.get_base_key(),
    db.my_db.get_cipher_map(),
    db.my_db.get_reverse_map(),
)
INDEX_TO_CHAR = dict(enumerate(ALPHABET))
CHAR_TO_INDEX = {ch: i for i, ch in INDEX_TO_CHAR.items()}
PRIME_INCREMENT = [3, 15, 44, 24, 4, 7]

# ------------------------------
# Helper: encode / decode utils
# ------------------------------


def indices_to_string(indices):
    """Convert list of base58 indices -> string"""
    return "".join(INDEX_TO_CHAR[i] for i in indices)


def string_to_indices(code_str):
    """Convert base58 string -> list of indices"""
    return [CHAR_TO_INDEX[ch] for ch in code_str]


def apply_cipher(indices):
    """Apply mono-substitution cipher"""
    return [CIPHER_MAP[i] for i in indices]


def remove_cipher(indices):
    """Reverse the cipher"""
    return [REVERSE_MAP[i] for i in indices]


def increment_base58(indices):
    """Increment a base-58 array by 1 (like an odometer)."""
    arr, i, carry = indices[:], len(indices) - 1, 1
    while i >= 0 and carry:
        arr[i], carry = (arr[i] + carry) % 58, int(arr[i] + carry >= 58)
        i -= 1
    return arr


def prime_increment_base58(indices):
    """Increment using predefined prime increments."""
    arr, carry = indices[:], 0
    for i in range(len(arr) - 1, -1, -1):
        arr[i] = arr[i] + PRIME_INCREMENT[i] + carry
        carry, arr[i] = divmod(arr[i], 58)
    return arr
