from flask import Flask
# from flask_cors import CORS
from flask_migrate import Migrate
from app.models import db
import os

app = Flask(__name__)
app.config.from_mapping({
  'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
  'SQLALCHEMY_TRACK_MODIFICATIONS': False,
})

db.init_app(app)
Migrate(app, db)

# Application Security
# CORS(app)


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')
