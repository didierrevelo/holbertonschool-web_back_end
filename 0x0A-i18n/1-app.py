#!/usr/bin/env python3
"""First you will setup a basic
Flask app in 0-app.py. Create a single / route"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config(object):
    """Configure the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def route_index():
    """Renders a Basic Template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
