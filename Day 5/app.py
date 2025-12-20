from flask import Flask, jsonify, request, render_template
import requests
app = Flask(__name__)

LEETCODE_URL = "http://127.0.0.1:8000/"
PROFILE_PAGE = "leetcode_profile/"
STATS_PAGE = "leetcode_contest_stats/"

users = {}

@app.route('/')
def home():
    # render index.html from templates folder
    return render_template('index.html')

@app.route('/api/add', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "user" not in data or data["user"] is None:
        return jsonify({"error": "Missing username"}), 400
    username = data["user"]
    dat1 = requests.get(LEETCODE_URL+STATS_PAGE+username).json()
    dat1 = dat1["data"]
    if not "userContestRanking" in dat1:
        return jsonify({"error": "Wrong username"}), 404
    rating = dat1["userContestRanking"]["rating"]
    
    users.update({username : rating})
    return jsonify({"rating":rating}),200

if __name__ == '__main__':
    app.run(debug=True)