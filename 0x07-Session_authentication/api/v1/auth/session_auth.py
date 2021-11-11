#!/usr/bin/env python3
"""Create a class SessionAuth
that inherits from Auth. For
the moment this class will be
empty. It’s the first step for
creating a new authentication mechanism:

validate if everything inherits
correctly without any overloading
validate the “switch” by using
environment variables

"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create session """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
