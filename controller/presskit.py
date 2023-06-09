import zipfile

from .modules import BaseWebServer


class Presskit:
    def __init__(self, api: BaseWebServer) -> None:
        self.server = api
        self.root = api.local_root / 'model' / 'presskit'
        self.zip_file = api.get_static_path() / 'presskit.zip'

    def build(self) -> None:
        """Zips all files and folders."""
        with zipfile.ZipFile(self.zip_file, 'w') as handle:
            for file in self.root.glob('**/*'):
                handle.write(file, arcname=file.relative_to(self.root))
