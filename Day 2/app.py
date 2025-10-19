from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Temporary in-memory database (list of dicts)
notes = [
    {"id": 1, "title": "Learn Flask"},
    {"id": 2, "title": "Build CRUD API"}
]

@app.route('/')
def home():
    # render index.html from templates folder
    return render_template('index.html')

# GET: return all notes
@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

# POST: create a new note
@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Missing note title"}), 400

    new_note = {
        "id": len(notes) + 1,
        "title": data["title"]
    }
    notes.append(new_note)
    return jsonify(new_note), 201

# PUT: update an existing note
@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = data.get("title", note["title"])
            return jsonify(note), 200
    return jsonify({"error": "Note not found"}), 404

# DELETE: delete a note
@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
