from flask import Flask
app = Flask(__name__)

from app import routes
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#

# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# from app import routes, models
