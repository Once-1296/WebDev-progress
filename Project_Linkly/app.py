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
        short_code = generate_short_code()
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
