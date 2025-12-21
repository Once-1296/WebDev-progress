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


LEETCODE_URL = "http://127.0.0.1:8000/"
PROFILE_PAGE = "leetcode_profile/"
STATS_PAGE = "leetcode_contest_stats/"

with app.app_context():
    db.create_all()

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

app.run(debug=True)