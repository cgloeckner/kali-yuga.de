from gevent import monkey; monkey.patch_all()

import requests
import bottle

from typing import Dict

from .modules import BaseWebServer


class WebServer(BaseWebServer):

    def __init__(self, args: Dict) -> None:
        super().__init__()
        self.args = args

        self.debug = args['debug']
        self.reverse_proxy = args['reverse_proxy']
        self.domain = args['domain']

        self.app = bottle.default_app()
        self.app.catchall = self.debug

    def get_client_ip(self, request: bottle.Request) -> str:
        """Returns client's ip address based on the given request."""
        if self.debug:
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

    def run(self) -> None:
        bottle.run(
            host=self.args['host'],
            port=self.args['port'],
            debug=self.args['debug'],
            reloader=self.args['reloader'],
            quiet=self.args['quiet'],
            server=self.args['server']
        )
