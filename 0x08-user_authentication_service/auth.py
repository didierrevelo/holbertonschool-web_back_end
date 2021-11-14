#!/usr/bin/env python3
"""In this task you will define a
_hash_password method that takes
in a password string arguments and
returns bytes.

The returned bytes is a salted
hash of the input password, hashed
with bcrypt.hashpw."""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Returns the hash of the password (str).
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    """Auth.register_user should take mandatory email and password string arguments and return a User object.

    If a user already exist with the passed email, raise a ValueError with the message User <user's email> already exists.

    If not, hash the password with _hash_password, save the user to the database using self._db and return the User object."""

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user in the database.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
        else:
            raise ValueError(f'User {email} already exists')