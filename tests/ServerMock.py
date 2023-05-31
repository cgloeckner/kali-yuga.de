import pathlib

from controller.modules import ServerApi


class ServerMock(ServerApi):
    def __init__(self) -> None:
        self.root = pathlib.Path('./')

    def get_contact_email(self) -> str:
        return f'contact@example.com'

    def get_merch_email(self) -> str:
        return f'merch@example.com'

    def get_booking_email(self) -> str:
        return f'booking@example.com'

    def get_local_root(self) -> pathlib.Path:
        return self.root

    def get_static_url(self, relative_url: str) -> str:
        return f'/static{relative_url}'
