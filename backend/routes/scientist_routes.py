from flask import Blueprint, request, jsonify
from models import db, Scientist, User, Badge
from utils.badge_logic import check_answer_and_award_badge

scientist_bp = Blueprint('scientist', __name__)

@scientist_bp.route('/api/scientist/<int:id>', methods=['GET'])
def get_scientist(id):
    scientist = Scientist.query.get(id)
    if not scientist:
        return jsonify({'error': 'Scientist not found'}), 404
    return jsonify({
        'id': scientist.id,
        'name': scientist.name,
        'period': scientist.period,
        'problem': scientist.problem
    })

@scientist_bp.route('/api/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    user_id = data['user_id']
    scientist_id = data['scientist_id']
    answer = float(data['answer'])

    result = check_answer_and_award_badge(user_id, scientist_id, answer)
    return jsonify(result)
