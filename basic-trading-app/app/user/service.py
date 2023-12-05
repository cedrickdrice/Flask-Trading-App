import jwt
import datetime

from config import Config

from app import db
from app.models.user import User
from app.user.schema.signup_user_schema import SignupUserSchema
from app.user.schema.login_user_schema import LoginUserSchema

from werkzeug.security import generate_password_hash, check_password_hash

class AuthService:
    def login_user(request):
        login_user_schema = LoginUserSchema()
        errors = login_user_schema.validate(request)
        
        if errors:
            return {'message' : errors, 'code' : 400}

        param = login_user_schema.load(request)
        
        auth_user = User.query.filter_by(username = param['username']).first()

        if auth_user is None:
            return {'message' : 'User not found', 'code' : 400}
        
        if check_password_hash(auth_user.password, param['password']):
            # generate token
            access_token = jwt.encode({
                        'id': auth_user.id,
                        'email': auth_user.email,
                        'username': auth_user.username,
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
                    }, Config.SECRET_KEY)
            
            param['access_token'] = access_token

            return {'code' : 200, 'message' : 'Login Successfully', 'data' : param}
        else:            
            return {'code' : 400, 'message' : 'Wrong Password'}


    def signup_user(request):
        signup_user_schema = SignupUserSchema()
        errors = signup_user_schema.validate(request)
        
        if errors:
            return {'message' : errors}

        param = signup_user_schema.load(request)

        get_existing_username = User.query.filter_by(username = param['username']).first()        
        get_existing_email = User.query.filter_by(email = param['email']).first()

        if get_existing_username:
            return {
                'code'      : 400, 
                'message'   : 'Username already exist'
            }
        
        if get_existing_email:
            return {
                'code'      : 400,
                'message'   : 'Email already exist'
            }
        
        hashed_password = generate_password_hash(param['password'])
        
        db.session.add(User(
            username=param['username'],
            email=param['email'],
            password=hashed_password
        ))

        try:
            db.session.commit()
            return {
                'code'      : 201, 
                'message'   : 'User created successfully'
            }
        except Exception as e:
            return {
                'code'      : 500,
                'message'   : str(e)
            }

    def get_auth_user(request):
        auth_header = request.headers.get('Authorization')

        auth_content = auth_header.split() if auth_header else []
        access_token = auth_content[1]            
        try:
            decode_auth = jwt.decode(
                access_token,
                Config.SECRET_KEY,
                algorithms="HS256",
                options={"require": ["exp"]}
            )

            return {
                'status'    : True,
                'message'   : 'Valid access token',
                'user'      :  decode_auth
            }
        except:
            return {
                'status'    : False,
                'message'   : 'Failed to decode token'
            }
            
        


