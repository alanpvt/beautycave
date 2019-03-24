import os
from flask import Flask
import sassutils.builder
from flask_migrate import Migrate
from sassutils.wsgi import SassMiddleware
from .models import db, Inventory

# import logging
# logging.basicConfig()

app = Flask(__name__, instance_relative_config=True) # !important
app.config.from_mapping(
  SECRET_KEY = os.urandom(16),
  SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(app.root_path, '..', 'data', 'data.db')),
  SQLALCHEMY_TRACK_MODIFICATIONS = True
)
db.init_app(app)
migrate = Migrate(app, db)

app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'beetcave': ('static/sass', 'static/css', '/static/css', True)
})

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

from .import views

