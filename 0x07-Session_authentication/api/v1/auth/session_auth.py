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
from models.user import User


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ user id for session id """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """ Returns a User instance based on a cookie value """
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)

        return User.get(user_id)

    def destroy_session(self, request=None):
        """ that deletes the user session / logout:"""
        if request is None:
            return False

        id_session = self.session_cookie(request)
        if id_session is None:
            return False

        id_user = self.user_id_for_session_id(id_session)
        if not id_user:
            return False

        try:
            del self.user_id_by_session_id[id_session]
        except Exception:
            pass

        return True
