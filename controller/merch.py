import pathlib

import tomli
import bottle

from enum import auto
from strenum import LowercaseStrEnum

from .modules import BaseModule


class MerchCategory(LowercaseStrEnum):
    CDS = auto()
    CLOTHS = auto()


class Merch(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.data = dict()

    def load_from_file(self, category: MerchCategory) -> None:
        filename = f'{self.root}/model/data/{category.value}.toml'
        with open(filename, 'rb') as file:
            self.data[category] = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('merch/index', data=self.data, email=self.email)
