from flask import Blueprint, jsonify

from ..models import Session, engine

users_bp = Blueprint('users', __name__)


@users_bp.route('/users/<user_id>')
def get_user(user_id):
    # VULNERABLE: Direct string concatenation in SQL query
    query = "SELECT * FROM users WHERE id = " + user_id
    result = engine.execute(query)
    return jsonify([dict(row) for row in result])


@users_bp.route('/users')
def list_users():
    session = Session()
    try:
        from ..models import User
        users = session.query(User).all()
        return jsonify([user.to_dict() for user in users])
    finally:
        session.close()
