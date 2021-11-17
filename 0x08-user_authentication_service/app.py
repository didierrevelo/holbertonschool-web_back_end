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
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """ If the user exist, respond with a 200 HTTP status and a JSON Payload
    Otherwise respond with a 403 HTTP status.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    msg = {"email": user.email}

    return jsonify(msg), 200


@app.route('/reset_password', methods=['POST'])
def reset_password() -> str:
    """Create a Flask app that has a single
    POST route ("/reset_password") and use flask.jsonify
    to return a JSON"""
    try:
        email = request.form['email']
    except KeyError:
        abort(403)

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    msg = {"email": email, "reset_token": reset_token}

    return jsonify(msg), 200

"""In this task, you will implement the Auth.update_password method. It takes reset_token string argument and a password string argument and returns None.

Use the reset_token to find the corresponding user. If it does not exist, raise a ValueError exception.

Otherwise, hash the password and update the user’s hashed_password field with the new hashed password and the reset_token field to None."""

@app.route('/update_password', methods=['POST'])
def update_password() -> str:
    """Create a Flask app that has a single
    POST route ("/update_password") and use flask.jsonify
    to return a JSON"""
    try:
        email = request.form['email']
        reset_token = request.form['reset_token']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        AUTH.update_password(reset_token, password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
