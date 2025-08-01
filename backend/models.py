from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scientist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    period = db.Column(db.String(100), nullable=False)
    problem = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.Float, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    badges = db.relationship('Badge', backref='user', lazy=True)

class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
