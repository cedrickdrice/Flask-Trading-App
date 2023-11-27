from flask import Blueprint
from app.authenticate import authenticate

bp = Blueprint('stock', __name__)

bp.before_request(authenticate)

from app.stock import routes
