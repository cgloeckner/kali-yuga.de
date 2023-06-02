import zipfile

from .modules import ServerApi


class Presskit:
    def __init__(self, api: ServerApi) -> None:
        self.server = api
        self.root = api.get_local_root() / 'model' / 'presskit'
        self.zip_file = api.get_static_path() / 'presskit.zip'

    def build(self) -> None:
        """Zips all files and folders."""
        with zipfile.ZipFile(self.zip_file, 'w') as handle:
            for file in self.root.glob('**/*'):
                handle.write(file, arcname=file.relative_to(self.root))
