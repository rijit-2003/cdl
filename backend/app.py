from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

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

# ✅ Correct Answer Check Route
@app.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()

    user_id = data.get("user_id")
    scientist_id = data.get("scientist_id")  # expecting a string like "eratosthenes"
    answer = data.get("answer")

    # Map string IDs to correct answers
    correct_answers = {
    "eratosthenes": 40000,        # Earth's circumference in km
    "aristarchus": 19,            # Distance to Sun / Distance to Moon ratio
    "hipparchus": 850, # Distance to nearest stars in km (~3 ly)
    "ptolemy": 80,                 # Orbital period of Mars in Earth years (approx)
    "copernicus": 6,         # Earth's orbital period in days
    "kepler": 1,                  # Orbital period for 1 AU in Earth years
    "newton": 6.674,                # Acceleration due to gravity (m/s²)
    "galileo": 4,              # Time for object to fall 1 meter (sec)
    "bessel": .314,               # Light years in one parsec
    "herschel": 1781,           # Estimated stars in Milky Way
    "bradley": 20.5,              # Aberration angle in arcseconds
    "hubble": 70,                 # Hubble constant (km/s/Mpc)
    "friendmann": 3,           # Age of the universe (billion years)
    "leavitt": 10,                # Period-luminosity distance: ~10 kpc
    "reiss": 68                 # Redshift z of distant supernova
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
