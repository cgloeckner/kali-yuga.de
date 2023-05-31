import bottle

from typing import List

from .modules import BaseModule, ServerApi


class Gallery(BaseModule):
    def __init__(self, api: ServerApi) -> None:
        super().__init__(api)

        self.data = list()

    @staticmethod
    def get_extensions() -> List[str]:
        return ['jpg', 'jpeg', 'png']

    @staticmethod
    def get_extension_wildcards() -> List[str]:
        """Transform into *.<ext> using all extensions in lowercase and uppercase version."""
        ext_list = Gallery.get_extensions()
        out = [f'*.{ext}' for ext in ext_list]
        out.extend([f'*.{ext.upper()}' for ext in ext_list])

        return out

    def load_from_disc(self) -> None:
        extensions = Gallery.get_extension_wildcards()
        root = self.server.get_local_root() / 'model' / 'content' / 'gallery'

        patterns = [root.glob(ext) for ext in extensions]
        self.data = [file.name for pattern in patterns for file in pattern]

    def render(self) -> None:
        self.template = bottle.template('gallery/index', data=self.data, contact_email=self.server.get_contact_email(),
                                        get_static_url=self.server.get_static_url)
