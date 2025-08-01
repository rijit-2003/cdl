from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app, origins="*")

# SQLite config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cdl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Badge model
class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    scientist = db.Column(db.String(50), nullable=False)
    badge_name = db.Column(db.String(100), nullable=False)

# Create DB
if not os.path.exists('cdl.db'):
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    return 'CDL Flask Backend Running!'

@app.route('/api/badge', methods=['POST'])
def add_badge():
    data = request.json
    badge = Badge(
        username=data['username'],
        scientist=data['scientist'],
        badge_name=data['badge_name']
    )
    db.session.add(badge)
    db.session.commit()
    return jsonify({'message': 'Badge added successfully'}), 201

@app.route('/api/badges/<username>', methods=['GET'])
def get_badges(username):
    badges = Badge.query.filter_by(username=username).all()
    return jsonify([
        {'scientist': b.scientist, 'badge_name': b.badge_name}
        for b in badges
    ])

# ✅ Route to serve scientist details by ID
@app.route('/api/scientist/<string:scientist_id>', methods=['GET'])
def get_scientist(scientist_id):
    try:
        with open('scientists.json') as f:
            data = json.load(f)
            for scientist in data:
                if scientist['id'] == scientist_id:
                    return jsonify(scientist)
        return jsonify({'error': 'Scientist not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ Correct Answer Check Route
@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()

    user_id = data.get("user_id")
    scientist_id = data.get("scientist_id")
    answer = data.get("answer")

    correct_answers = {
        "eratosthenes": 40000,
        "aristarchus": 19,
        "hipparchus": 850,
        "ptolemy": 80,
        "copernicus": 6,
        "kepler": 1,
        "newton": 6.674,
        "galileo": 4,
        "bessel": .314,
        "herschel": 1781,
        "bradley": 20.5,
        "hubble": 70,
        "friendmann": 3,
        "leavitt": 10,
        "reiss": 68
    }

    correct = correct_answers.get(scientist_id)
    if correct is None:
        return jsonify({'message': 'Scientist answer not available'}), 404

    if abs(float(answer) - correct) < 0.05 * correct:
        return jsonify({'message': '✅ Correct! Well done.'})
    else:
        return jsonify({'message': '❌ Incorrect. Try again!'})

if __name__ == '__main__':
    app.run(debug=True)
