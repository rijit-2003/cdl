from models import db, Scientist, User, Badge

def check_answer_and_award_badge(user_id, scientist_id, user_answer):
    scientist = Scientist.query.get(scientist_id)
    user = User.query.get(user_id)
    if not scientist or not user:
        return {'status': 'error', 'message': 'Invalid user or scientist'}

    margin = 0.05 * scientist.correct_answer
    if abs(scientist.correct_answer - user_answer) <= margin:
        badge_name = f"{scientist.name} Conqueror"
        existing = Badge.query.filter_by(name=badge_name, user_id=user_id).first()
        if not existing:
            badge = Badge(name=badge_name, user_id=user_id)
            db.session.add(badge)
            db.session.commit()
        return {'status': 'success', 'message': 'Correct! Badge awarded.'}
    else:
        return {'status': 'fail', 'message': 'Incorrect answer'}
