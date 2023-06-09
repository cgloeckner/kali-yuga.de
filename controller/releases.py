import bottle

from .modules import BaseModule, BaseWebServer
from .merch import Merch


class Releases(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)
        self.data = dict()

    def load_from_merch(self, merch: Merch) -> None:
        self.data = merch.get_cds()

    def render(self) -> None:
        self.template = bottle.template('releases/index', module_title='Releases', data=self.data,
                                        get_static_url=self.server.get_static_url)
