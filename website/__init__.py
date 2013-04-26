from flask import Flask

app = Flask('website')


@app.route('/')
def index():
    return "Hello %s!" % app.config.get('ADMIN')
