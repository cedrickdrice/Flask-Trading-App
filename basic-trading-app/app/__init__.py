from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.stock import bp as stock_bp
app.register_blueprint(stock_bp, url_prefix='/stock')

from app.order import bp as order_bp
app.register_blueprint(order_bp, url_prefix='/order')

from app.user import bp as user_bp
app.register_blueprint(user_bp, url_prefix='/')