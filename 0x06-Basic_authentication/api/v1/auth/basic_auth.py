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
