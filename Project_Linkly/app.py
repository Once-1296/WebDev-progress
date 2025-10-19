from flask import Flask, jsonify, request, render_template
from urllib.parse import urlparse
import numpy as np
import requests
app = Flask(__name__)

map_dict ={

}
def make_short(link):
    short_link = "abc"
    parsed = urlparse(link)
    if not (parsed.scheme and parsed.netloc):
        return False, ""
    try:
        response = requests.head(link, timeout=5)
        return True,link
    except requests.RequestException:
        return False, ""

    #complete logic

    return True,short_link
@app.route('/')
def home():
    # Renders the frontend HTML
    return render_template('index.html')

# POST route: user submits a guess
@app.route('/api/shorten', methods=["POST"])
def get_link():
    global map_dict
    data = request.get_json()
    # Validation checks
    if not data or "link" not in data:
        return jsonify({"error": "Missing link"}), 400
    flag,short_link = make_short(data["link"])
    if not flag:
        return jsonify({"error": "Invalid link"}), 400

    map_dict.update({data["link"]:short_link})
     

    return jsonify({
        "long_link": data["link"],
        "result": short_link
    }), 200

# Optional GET route (if you want to view the current guess result)
@app.route('/api/show', methods=["GET"])
def status():
    print("Hello world")
    return jsonify(map_dict),200


if __name__ == '__main__':
    app.run(debug=True, port=5001)
