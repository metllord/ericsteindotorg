from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('website')
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "Hello %s!" % app.config.get('ADMIN')
