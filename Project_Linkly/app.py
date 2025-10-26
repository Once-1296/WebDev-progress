# app.py
from flask import Flask, request, jsonify, render_template, redirect
import db
import utils

app = Flask(__name__)


# Initialize DB at startup
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not data or "link" not in data:
        return jsonify({"error": "Missing link"}), 400

    long_url = data["link"].strip()

    if not utils.validate_url(long_url):
        return jsonify({"error": "Invalid or unreachable URL"}), 400

    # Check if URL already exists
    existing_code = db.my_db.get_short_code(long_url)
    if existing_code:
        return (
            jsonify(
                {
                    "long_url": long_url,
                    "short_code": existing_code,
                    "message": "Existing short code found",
                }
            ),
            200,
        )
    if "suggestion" in data:
        if data["suggestion"] is not None:
            prefix = data["suggestion"]
        else:
            prefix = ""
    else:
        prefix = ""
    # Generate a unique short code
    while True:
        suffix = utils.generate_next_code()
        # print(prefix)
        short_code = prefix + suffix
        if not db.my_db.get_long_url(short_code):
            break

    db.my_db.insert_url(long_url, short_code)

    return (
        jsonify(
            {
                "long_url": long_url,
                "short_code": short_code,
                "short_url": f"/api/shorten/{short_code}",
            }
        ),
        200,
    )


@app.route("/api/shorten/<short_code>", methods=["GET"])
def redirect_to_long(short_code):
    long_url = db.my_db.get_long_url(short_code)
    if long_url:
        db.my_db.increment_click_count(short_code)
        return redirect(long_url)
    return jsonify({"error": "Short code not found"}), 404


@app.route("/api/stats/<short_code>", methods=["GET"])
def get_clicks(short_code):
    clicks = db.my_db.get_click_count(short_code)
    long_url = db.my_db.get_long_url(short_code)
    if clicks is not None and long_url is not None:
        return (
            jsonify(
                {
                    "clicks": clicks,
                    "long_url": long_url,
                    "short_code": short_code,
                }
            ),
            200,
        )
    return jsonify({"error": "Short code not valid"}), 404


@app.route("/api/show", methods=["GET"])
def show_all():
    # Optional: Debug endpoint to show all stored URLs
    url_db = db.my_db.get_all_urls()
    if url_db is None:
        return jsonify({"warning": "no links"}), 404
    map_dict = {}
    for long_url, short_code in url_db:
        map_dict.update(
            {
                long_url: short_code,
            }
        )
    return jsonify(map_dict), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)
