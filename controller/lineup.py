import tomli
import bottle

from .modules import BaseModule, BaseWebServer


class Lineup(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

        self.data = dict()

    def load_from_file(self) -> None:
        filename = f'{self.server.local_root}/model/data/lineup.toml'
        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('lineup/index', module_title='Lineup & Biografie', data=self.data,
                                        get_static_url=self.server.get_static_url)
