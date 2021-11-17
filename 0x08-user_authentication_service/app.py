#!/usr/bin/env python3
"""app.py file"""

from flask import Flask, jsonify, request, abort, request, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def single() -> str:
    """Create a Flask app that
has a single GET route ("/") and
use flask.jsonify to return a JSON
payload of the form:"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user() -> str:
    """Create a Flask app that has a single
    POST route ("/users") and use flask.jsonify
    to return a JSON"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
    except KeyError:
        abort(400)
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"email": email, "message": "user created"})

    return jsonify({"email": "<registered email>", "message": "user created"})


@app.route("/sessions", methods=["POST"])
def login() -> str:
    """Create a Flask app that has a single
    POST route ("/sessions") and use flask.jsonify
    to return a JSON"""
    try:
        email = request.form.get("email")
        password = request.form.get("password")
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    msg = {"email": email, "message": "logged in"}
    response = jsonify(msg)

    response.set_cookie("session_id", session_id)

    return response

@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """Create a Flask app that has a single
    DELETE route ("/sessions") and use flask.jsonify
    to return a JSON"""
    try:
        session_id = request.cookies.get("session_id", None)
    except KeyError:
        abort(403)

    if not AUTH.get_user_from_session_id(session_id):
        abort(403)

    AUTH.destroy_session(session_id)

    response = redirect("/")
    response.set_cookie("session_id", "", expires=0)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
