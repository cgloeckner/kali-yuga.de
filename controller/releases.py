import tomli
import bottle

from typing import Dict, List

from .modules import BaseModule
from .merch import Merch


class Releases(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.data = dict()

    def load_from_merch(self, merch: Merch) -> None:
        self.data = merch.get_cds()

    def render(self, contact_email: str) -> None:
        self.template = bottle.template('releases/index', data=self.data, email=self.email, contact_email=contact_email)
