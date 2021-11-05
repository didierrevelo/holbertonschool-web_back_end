#!/usr/bin/env python3
"""Create a folder api/v1/auth
Create an empty file api/v1/auth/__init__.py
Create the class Auth:
in the file api/v1/auth/auth.py
import request from flask
class name Auth
public method def require_auth(self,
path: str, excluded_paths: List[str]) -> bool:
that returns False - path and excluded_paths
will be used later, now, you don’t need to
take care of them
public method def authorization_header(self,
request=None) -> str: that returns None - request
will be the Flask request object
public method def current_user(self, request=None) ->
TypeVar('User'): that returns None - request will be
the Flask request object
This class is the template for all authentication
system you will implement."""
from flask import request
from typing import TypeVar, List


class Auth:
    """Class Auth"""

    def __init__(self):
        """__init__ method"""
        self.request = request

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> str:
        """current_user method"""
        return None
