import pathlib

from abc import abstractmethod, ABC


class BaseModule(ABC):
    def __init__(self, root: pathlib.Path, email: str) -> None:
        self.root = root
        self.email = email
        self.template = None

    @abstractmethod
    def render(self) -> None: ...
