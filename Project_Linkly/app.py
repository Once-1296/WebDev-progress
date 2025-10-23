# app.py
from flask import Flask, request, jsonify, render_template, redirect
from urllib.parse import urlparse
import string, random, requests
import db

app = Flask(__name__)

# Initialize DB at startup
db.init_db()

# Base58 alphabet (excluding confusing chars like 0, O, l, I)
BASE58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# --- Load constants ---
BASE_KEY     = db.get_base_key()
CIPHER_MAP   = db.get_cipher_map()
REVERSE_MAP  = db.get_reverse_map()
ALPHABET     = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
INDEX_TO_CHAR = {i: ch for i, ch in enumerate(ALPHABET)}
CHAR_TO_INDEX = {ch: i for i, ch in enumerate(ALPHABET)}

PRIME_INCREMENT = [3,15,44,24,4,7]

# ------------------------------
# Helper: encode / decode utils
# ------------------------------

def indices_to_string(indices):
    """Convert list of base58 indices -> string"""
    return ''.join(INDEX_TO_CHAR[i] for i in indices)

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
    arr = indices[:]
    i = len(arr) - 1
    carry = 1
    while i >= 0 and carry:
        arr[i] = (arr[i] + carry) % 58
        carry = 1 if arr[i] == 0 else 0
        i -= 1
    return arr

def prime_increment_base58(indices):
    # add prime (1<<31) - 1
    arr = indices[:]
    i = len(arr) - 1
    carry = 0
    while i >= 0:
        arr[i] = (arr[i] + PRIME_INCREMENT[i] + carry)
        carry = 1 if arr[i] >=58 else 0
        arr[i] =(arr[i])%58
        i -= 1
    return arr


# ------------------------------
# Main short-code generator
# ------------------------------
def generate_next_code():
    """Return next short code as 6-char Base58 string using seed & cipher."""
    last_code = db.get_last_short_code()

    if not last_code:
        # --- No previous URL, use base key ---
        base = BASE_KEY
    else:
        # --- Decode last code ---
        last_indices = string_to_indices(last_code)
        # reverse cipher first to get numeric sequence
        decoded = remove_cipher(last_indices)
        # increment
        base = prime_increment_base58(decoded)

    # Apply cipher again and convert to string
    ciphered = apply_cipher(base)
    short_code = indices_to_string(ciphered)
    return short_code

def generate_short_code(length=6):
    #use base 58 encoding to create a random short_code
    return ''.join(random.choices(BASE58_ALPHABET, k=length))

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    if not data or 'link' not in data:
        return jsonify({"error": "Missing link"}), 400

    long_url = data['link'].strip()
    
    if not validate_url(long_url):
        return jsonify({"error": "Invalid or unreachable URL"}), 400

    # Check if URL already exists
    existing_code = db.get_short_code(long_url)
    if existing_code:
        return jsonify({
            "long_url": long_url,
            "short_code": existing_code,
            "message": "Existing short code found"
        }), 200

    # Generate a unique short code
    while True:
        short_code = generate_next_code()
        if not db.get_long_url(short_code):
            break

    db.insert_url(long_url, short_code)

    return jsonify({
        "long_url": long_url,
        "short_code": short_code,
        "short_url": f"/api/shorten/{short_code}"
    }), 200

@app.route('/api/shorten/<short_code>', methods=['GET'])
def redirect_to_long(short_code):
    long_url = db.get_long_url(short_code)
    if long_url:
        return redirect(long_url)
    return jsonify({"error": "Short code not found"}), 404

@app.route('/api/show', methods=['GET'])
def show_all():
    # Optional: Debug endpoint to show all stored URLs
    url_db = db.get_all_urls()
    map_dict ={

    }
    for long_url,short_code in url_db:
        map_dict.update({long_url:short_code,})
    return jsonify(map_dict), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)
