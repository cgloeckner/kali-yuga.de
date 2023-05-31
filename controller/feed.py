import tomli
import bottle

from .modules import BaseModule, ServerApi


class Feed(BaseModule):
    def __init__(self, api: ServerApi) -> None:
        super().__init__(api)

        self.data = dict()

    def load_from_file(self) -> None:
        filename = f'{self.server.get_local_root()}/model/data/feed.toml'
        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self) -> None:
        self.template = bottle.template('feed/index', data=self.data, contact_email=self.server.get_contact_email())
