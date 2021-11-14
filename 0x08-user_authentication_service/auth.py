#!/usr/bin/env python3
"""In this task you will define a
_hash_password method that takes
in a password string arguments and
returns bytes.

The returned bytes is a salted
hash of the input password, hashed
with bcrypt.hashpw."""
import bcrypt


def _hash_password(password: str) -> str:
    """
    Returns the hash of the password (str).
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
