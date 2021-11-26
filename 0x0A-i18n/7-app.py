#!/usr/bin/env python3
"""First you will setup a basic
Flask app in 0-app.py. Create a single / route"""
from flask import Flask, render_template
from flask_babel import Babel
from flask import request, g
from typing import Union
import pytz


app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config(object):
    """Configure the app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    """Returns a user dictionary."""

    try:
        login_as = request.args.get("login_as")
        user = users[int(login_as)]
    except Exception:
        return None
    return user


@app.before_request
def before_request():
    """Set the user in the global scope."""
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'], strict_slashes=False)
def route_index():
    """Renders a Basic Template"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale() -> str:
    """Select a language """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            return locale

    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    1 Find timezone
    2 Find time zone
    3 Default to UTC
    """
    try:
        if request.args.get("timezone"):
            timezone = request.args.get("timezone")
            tz = pytz.timezone(timezone)

        elif g.user and g.user.get("timezone"):
            timezone = g.user.get("timezone")
            tz = pytz.timezone(timezone)
        else:
            timezone = app.config["BABEL_DEFAULT_TIMEZONE"]
            tz = pytz.timezone(timezone)

    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone

if __name__ == '__main__':
    app.run()
