#!/usr/bin/env python
"""Create a class SessionAuth
that inherits from Auth. For
the moment this class will be
empty. It’s the first step for
creating a new authentication mechanism:

validate if everything inherits
correctly without any overloading
validate the “switch” by using
environment variables"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class
    """
    pass
