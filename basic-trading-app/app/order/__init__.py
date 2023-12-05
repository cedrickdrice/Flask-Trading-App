from flask import Blueprint
from app.authenticate import authenticate

bp = Blueprint('order', __name__)

bp.before_request(authenticate)

from app.order import routes
