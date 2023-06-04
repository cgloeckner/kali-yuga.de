import pathlib

from abc import abstractmethod, ABC
from typing import Dict


class ServerApi(ABC):
    @abstractmethod
    def get_contact_email(self) -> str: ...

    @abstractmethod
    def get_merch_email(self) -> str: ...

    @abstractmethod
    def get_booking_email(self) -> str: ...

    def get_all_emails(self) -> Dict[str, str]:
        return {
            'contact': self.get_contact_email(),
            'merch': self.get_merch_email(),
            'booking': self.get_booking_email(),
            'webmaster': self.get_webmaster_email()
        }

    @abstractmethod
    def get_webmaster_email(self) -> str: ...

    @abstractmethod
    def get_local_root(self) -> pathlib.Path: ...

    @abstractmethod
    def get_static_path(self) -> pathlib.Path: ...

    @abstractmethod
    def get_static_url(self, relative_url: str) -> str: ...


class BaseModule(ABC):
    def __init__(self, server: ServerApi) -> None:
        self.server = server
        self.template = None

    @abstractmethod
    def render(self) -> None: ...
