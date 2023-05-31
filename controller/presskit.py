import tempfile
import zipfile

from .modules import ServerApi


class Presskit:
    def __init__(self, api: ServerApi) -> None:
        self.server = api
        self.root = api.get_local_root() / 'model' / 'presskit'
        self.zip_file = tempfile.NamedTemporaryFile()

    def __del__(self):
        self.zip_file.close()

    def build(self) -> None:
        """Zips all files and folders."""
        with zipfile.ZipFile(self.zip_file, 'w') as handle:
            for file in self.root.glob('**/*'):
                handle.write(file, arcname=file.relative_to(self.root))
