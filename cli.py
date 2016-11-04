#!/usr/bin/python
import logging

from plumbum.cli import Application
import pogo.util as util
from pogo.api import PokeAuthSession

from access_token import AccessTokenFetcher
from analyze_xp import analyze_xp
from collect_reward import collect_reward
from rename_party import rename_party


class PokeHelperCLI(Application):
    def main(self, email, command):
        util.setupLogger()
        method = {
            'rename': rename_party,
            'collect': collect_reward,
            'analyze_xp': analyze_xp,
        }.get(command)
        if not method:
            print 'Unknown command {}'.format(command)
            return
        session = self.get_session_for_email(email)
        logging.info("Printing Profile:")
        profile = session.getProfile()
        logging.info(profile)
        method(session)

    def get_session_for_email(self, email):
        access_token = AccessTokenFetcher(email).get_access_token()
        auth_session = PokeAuthSession(username=None, password=None, provider='google')
        auth_session.accessToken = access_token
        return auth_session.createPogoSession(provider='google', noop=True)


if __name__ == '__main__':
    PokeHelperCLI.run()
