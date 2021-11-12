#!/usr/bin/env python3
"""Create a class BasicAuth
that inherits from Auth.
For the moment this class will
be empty.

Update api/v1/app.py for using
BasicAuth class instead of Auth
depending of the value of the
environment variable AUTH_TYPE,
If AUTH_TYPE is equal to basic_auth:

import BasicAuth from api.v1.auth.basic_auth
create an instance of BasicAuth
and assign it to the variable auth
Otherwise, keep the previous mechanism
with auth an instance of Auth.
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Return the Base64 part of the
        Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """Return the decoded Base64 part of the
        Authorization header for a Basic Authentication"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decode = base64.b64decode(base64_authorization_header)
            return decode.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """Extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(":", 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            found_users = User.search({'email': user_email})
        except Exception:
            return None

        for user in found_users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the User instance for a request"""
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        coded = self.extract_base64_authorization_header(auth_header)

        if not coded:
            return None

        decoded = self.decode_base64_authorization_header(coded)

        if not decoded:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded)

        if not user_email or not user_pwd:
            return None

        user = self.user_object_from_credentials(user_email, user_pwd)
        return user
