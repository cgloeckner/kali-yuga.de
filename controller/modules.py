import pathlib

from abc import abstractmethod, ABC
from typing import Dict


def get_email_address(recipient: str, domain: str) -> str:
    return f'{recipient}@{domain}'


class BaseWebServer(ABC):
    def __init__(self):
        self.domain = 'localhost'
        self.debug = True
        self.reverse_proxy = False
        self.local_root = pathlib.Path('./')

    def get_contact_email(self) -> str:
        return get_email_address('kontakt', self.domain)

    def get_merch_email(self) -> str:
        return get_email_address('merch', self.domain)

    def get_booking_email(self) -> str:
        return get_email_address('booking', self.domain)

    def get_webmaster_email(self) -> str:
        return get_email_address('webmaster', self.domain)

    def get_all_emails(self) -> Dict[str, str]:
        return {
            'contact': self.get_contact_email(),
            'merch': self.get_merch_email(),
            'booking': self.get_booking_email(),
            'webmaster': self.get_webmaster_email()
        }

    def get_build_path(self) -> pathlib.Path:
        return self.local_root / '.build'

    def get_static_url(self, relative_url: str) -> str:
        if self.reverse_proxy:
            return f'https://static.{self.domain}{relative_url}'

        return f'/static{relative_url}'

    def get_static_path(self) -> pathlib.Path:
        """Returns local path to static files (css sheets etc.)"""
        return self.local_root / 'views' / 'static'

    def get_public_url(self, route: str = '') -> str:
        """Returns the public uri with or without a route. HTTPS is assumed in production mode.
        e.g. https://example.com/foo/bar
        """
        base = 'http'
        if not self.debug:
            base += 's'

        base += '://' + self.domain

        if route != '':
            base += '/' + route
        return base


class BaseModule(ABC):
    def __init__(self, server: BaseWebServer) -> None:
        self.server = server
        self.template = None

    @abstractmethod
    def render(self) -> None: ...
