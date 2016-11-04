# -*- coding: utf-8 -*-
from getpass import getpass
from pogo.api import PokeAuthSession


class AccessTokenFetcher(object):
    def __init__(self, email):
        self.email = email

    def get_access_token(self):
        while True:
            password = getpass('Password: ')
            auth_session = PokeAuthSession(self.email, password, 'google')
            auth_session.authenticate()
            if auth_session.accessToken:
                return auth_session.accessToken

