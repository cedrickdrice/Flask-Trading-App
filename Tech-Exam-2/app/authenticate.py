import jwt
from flask import request, jsonify
from config import Config
from app.models.user import User

def authenticate():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'code': 401, 'message': 'Authorization header is missing'}), 401

    auth_content = auth_header.split()
    
    if len(auth_content) != 2 or auth_content[0] != 'Bearer':
        return jsonify({'code': 401, 'message': 'Invalid authorization header format'}), 401

    access_token = auth_content[1]
    try:
        decoded = jwt.decode(access_token, Config.SECRET_KEY, algorithms=["HS256"])
        user = User.query.filter_by(id=decoded['id']).first()
        if not user:
            return jsonify({'code': 401, 'message': 'User not found'}), 401
    except jwt.ExpiredSignatureError:
        return jsonify({'code': 401, 'message': 'Expired access token'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'code': 401, 'message': 'Invalid access token'}), 401
