import bottle

from typing import List

from .modules import BaseModule


class Gallery(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

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
        root = self.root / 'model' / 'content' / 'gallery'

        patterns = [root.glob(ext) for ext in extensions]
        self.data = [file.name for pattern in patterns for file in pattern]

    def render(self, contact_email: str) -> None:
        self.template = bottle.template('gallery/index', data=self.data, contact_email=contact_email)
