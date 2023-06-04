import tomli
import bottle

from .modules import BaseModule, ServerApi


class Lineup(BaseModule):
    def __init__(self, api: ServerApi) -> None:
        super().__init__(api)

        self.data = dict()

    def load_from_file(self) -> None:
        filename = f'{self.server.get_local_root()}/model/data/lineup.toml'
        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('lineup/index', data=self.data, get_static_url=self.server.get_static_url)
