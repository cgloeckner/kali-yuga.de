import pathlib

import tomli
import bottle

from enum import auto
from strenum import LowercaseStrEnum


class MerchCategory(LowercaseStrEnum):
    CDS = auto()
    CLOTHS = auto()


class Merch:
    def __init__(self, root: pathlib.Path) -> None:
        self.root = root

        self.data = dict()
        self.template = None

    def load_from_file(self, category: MerchCategory) -> None:
        filename = f'{self.root}/model/data/{category.value}.toml'
        with open(filename, 'rb') as file:
            self.data[category] = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('merch/index', data=self.data)

    def get_template(self) -> str:
        return self.template
