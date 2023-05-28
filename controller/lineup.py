import tomli
import bottle

from typing import Dict, List

from .modules import BaseModule


class Lineup(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.data = dict()

    def load_from_file(self) -> None:
        filename = f'{self.root}/model/data/lineup.toml'
        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('lineup/index', data=self.data)
