#!/usr/bin/env python3
"""First you will setup a basic
Flask app in 0-app.py. Create a single / route"""
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'], strict_slashes=False)
def route_index():
    """Renders a Basic Template"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
