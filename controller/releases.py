import tomli
import bottle

from typing import Dict, List

from .modules import BaseModule, ServerApi
from .merch import Merch


class Releases(BaseModule):
    def __init__(self, api: ServerApi) -> None:
        super().__init__(api)
        self.data = dict()

    def load_from_merch(self, merch: Merch) -> None:
        self.data = merch.get_cds()

    def render(self) -> None:
        self.template = bottle.template('releases/index', data=self.data, contact_email=self.server.get_contact_email(),
                                        get_static_url=self.server.get_static_url)
