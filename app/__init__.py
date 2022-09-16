from flask import Flask
from config import Config
from flask_cors import CORS
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)
CORS(app)

app.config.from_object(Config)

from .models import db

db.init_app(app)
migrate = Migrate(app, db)

from . import routes