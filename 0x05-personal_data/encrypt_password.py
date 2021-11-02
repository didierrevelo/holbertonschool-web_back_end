#!/usr/bin/env python3
"""User passwords should NEVER be
stored in plain text in a database.

Implement a hash_password function
that expects one string argument name
password and returns a salted, hashed
password, which is a byte string.

Use the bcrypt package to perform the
hashing (with hashpw)."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return True if the password is valid, False otherwise."""
    return bcrypt.checkpw(password.encode(), hashed_password)
