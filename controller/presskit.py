import pathlib
import tempfile
import zipfile


class Presskit:
    def __init__(self, root: pathlib.Path) -> None:
        self.root = root / 'model' / 'presskit'
        self.zip_file = tempfile.NamedTemporaryFile()

    def __del__(self):
        self.zip_file.close()

    def build(self) -> None:
        """Zips all files and folders."""
        with zipfile.ZipFile(self.zip_file, 'w') as zip:
            for file in self.root.glob('**/*'):
                zip.write(file, arcname=file.relative_to(self.root))
