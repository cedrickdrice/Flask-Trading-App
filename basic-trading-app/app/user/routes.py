# app/auth/routes.py

from flask import request, jsonify
from app.user import bp
from app.user.service import AuthService

@bp.route('/login', methods=['POST'])
def login():
    response = AuthService.login_user(request.json)
    return jsonify(response), response['code']

@bp.route('/signup', methods=['POST'])
def signup():
    response = AuthService.signup_user(request.json)
    return response, response['code']
