import tomli
import bottle

from enum import auto
from strenum import LowercaseStrEnum

from . import server


class MerchCategory(LowercaseStrEnum):
    CDS = auto()
    CLOTHS = auto()


class Merch:
    def __init__(self, engine: server.WebServer) -> None:
        self.engine = engine

        self.data = dict()
        self.template = None

    def load_from_file(self, category: MerchCategory) -> None:
        filename = f'{self.engine.local_root}/model/merch/{category.value}.toml'
        with open(filename, 'rb') as file:
            self.data[category] = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('merch/index', data=self.data)

    def get_template(self) -> str:
        return self.template
