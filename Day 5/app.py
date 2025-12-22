from flask import Flask, jsonify, request, render_template
import requests
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
print(app.config["SQLALCHEMY_DATABASE_URI"])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), unique = True, nullable = False)
    rating = db.Column(db.Integer, unique = False, nullable = False)

header = {"User-Agent": "Web Agent", "Content-Type": "application/json"}

def fetch_leetcode_rating(username):
    api_url = "https://leetcode.com/graphql"
    payload = {
        "query": """
        query userContestRankingInfo($username: String!) {
          userContestRanking(username: $username) {
            rating
          }
        }
        """,
        "variables": {"username": username},
        "operationName": "userContestRankingInfo",
    }

    response = requests.post(api_url, headers=header, json=payload).json()
    data = response.get("data", {})

    if not data or not data.get("userContestRanking"):
        return None

    return data["userContestRanking"]["rating"]


def update_all_ratings():
    print("🔄 Updating ratings on startup...")

    entries = Entry.query.all()

    for entry in entries:
        new_rating = fetch_leetcode_rating(entry.username)

        if new_rating is not None:
            entry.rating = new_rating
            print(f"✔ {entry.username}: {new_rating}")
        else:
            print(f"⚠ Failed to fetch rating for {entry.username}")

    db.session.commit()
    print("✅ Ratings updated")

with app.app_context():
    db.create_all()
    update_all_ratings()




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
    api_url = "https://leetcode.com/graphql"
    upload = {
        "query": "\n  query userContestRankingInfo($username: String!) {\n  userContestRanking(username: $username) {\n    attendedContestsCount\n    rating\n    globalRanking\n    totalParticipants\n    topPercentage\n    badge {\n      name\n    }\n  }\n  userContestRankingHistory(username: $username) {\n    attended\n    trendDirection\n    problemsSolved\n    totalProblems\n    finishTimeInSeconds\n    rating\n    ranking\n    contest {\n      title\n      startTime\n    }\n  }\n}\n    ",
        "variables": {"username": username},
        "operationName": "userContestRankingInfo",
    }
    response = requests.post(api_url, headers=header, json=upload).json()
    dat1 = response["data"]
    if not "userContestRanking" in dat1:
        return jsonify({"error": "Wrong username"}), 404
    rating = dat1["userContestRanking"]["rating"]
    new_entry = Entry(username = username, rating = rating)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"rating":rating}),200

@app.route('/api/all_users',methods=['GET'])
def get_users():
    entries = Entry.query.all()
    return jsonify([
        {
            "id": e.id,
            "username": e.username,
            "rating": e.rating
        }
        for e in entries
    ]), 200

@app.route('/api/delete/<int:id>',methods=['DELETE'])
def delete_user(id):
    entry = Entry.query.get(id)
    if entry is None:
        return jsonify({"error": "Invalid username"}), 400
    
    db.session.delete(entry)
    db.session.commit()
    return "", 204


app.run(debug=True)