import tomli
import bottle

from .modules import BaseModule


class Feed(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.data = dict()

    def load_from_file(self) -> None:
        filename = f'{self.root}/model/data/feed.toml'
        with open(filename, 'rb') as file:
            self.data = tomli.load(file)

    def render(self, contact_email: str) -> None:
        self.template = bottle.template('feed/index', data=self.data, contact_email=contact_email)
