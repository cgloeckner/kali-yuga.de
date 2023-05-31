import pathlib
import requests

from typing import Dict

from gevent import monkey; monkey.patch_all()
import bottle

from enum import auto
from strenum import LowercaseStrEnum

from .modules import ServerApi


class Recipient(LowercaseStrEnum):
    CONTACT = auto()
    BOOKING = auto()
    MERCH = auto()
    WEBMASTER = auto()


def get_email_address(recipient: Recipient, domain: str) -> str:
    return f'{recipient.value}@{domain}'


class WebServer(ServerApi):

    def __init__(self, args: Dict) -> None:
        self.local_root = pathlib.Path('./')
        self.args = args

        self.app = bottle.default_app()
        self.app.catchall = self.args['debug']

    def get_contact_email(self) -> str:
        return get_email_address(Recipient.CONTACT, self.args['domain'])

    def get_merch_email(self) -> str:
        return get_email_address(Recipient.MERCH, self.args['domain'])

    def get_booking_email(self) -> str:
        return get_email_address(Recipient.BOOKING, self.args['domain'])

    def get_local_root(self) -> pathlib.Path:
        return self.local_root

    def run(self) -> None:
        bottle.run(
            host=self.args['host'],
            port=self.args['port'],
            debug=self.args['debug'],
            reloader=self.args['reloader'],
            quiet=self.args['quiet'],
            server=self.args['server']
        )

    def get_statics_path(self) -> pathlib.Path:
        """Returns local path to static files (css sheets etc.)"""
        return self.local_root / 'static'

    def get_public_url(self, route: str = '') -> str:
        """Returns the public uri with or without a route. HTTPS is assumed in production mode.
        e.g. https://example.com/foo/bar
        """
        base = 'http'
        if not self.args['debug']:
            base += 's'

        base += '://' + self.args['domain']

        if route != '':
            base += '/' + route
        return base

    def get_client_ip(self, request: bottle.Request) -> str:
        """Returns client's ip address based on the given request."""
        if self.args['debug']:
            return request.environ.get('REMOTE_ADDR')

        # default: app runs behind reverse proxy
        return request.environ.get('HTTP_X_FORWARDED_FOR')

    @staticmethod
    def get_client_agent(request: bottle.Request) -> str:
        """Returns the client's browser agent based on the given request."""
        return request.environ.get('HTTP_USER_AGENT')

    @staticmethod
    def get_public_ip():
        try:
            return requests.get('https://api.ipify.org').text
        except requests.exceptions.ReadTimeout as e:
            return 'localhost'
