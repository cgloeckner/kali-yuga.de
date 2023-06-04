import tomli
import bottle

from typing import Dict, List

from enum import auto
from strenum import LowercaseStrEnum

from .modules import BaseModule, ServerApi


class MerchCategory(LowercaseStrEnum):
    CDS = auto()
    CLOTHS = auto()
    MISC = auto()

    @property
    def caption(self) -> str:
        if self.value == MerchCategory.CDS:
            return 'CDs'
        if self.value == MerchCategory.CLOTHS:
            return 'Kleidung'
        if self.value == MerchCategory.MISC:
            return 'Sonstiges'
        raise NotImplemented


class Merch(BaseModule):
    def __init__(self, api: ServerApi) -> None:
        super().__init__(api)
        self.data = dict()

    @staticmethod
    def process_merch(merch: Dict[str, Dict]) -> List[dict]:
        return [merch[key] for key in merch]

    def get_cds(self) -> List[dict]:
        return self.data[MerchCategory.CDS]

    def load_from_file(self, category: MerchCategory) -> None:
        filename = f'{self.server.get_local_root()}/model/data/{category.value}.toml'
        with open(filename, 'rb') as file:
            merch = tomli.load(file)

        self.data[category] = self.process_merch(merch)

        # sort CDs by year (most recent first)
        if category == MerchCategory.CDS:
            self.data[category].sort(key=lambda cd: cd['year'], reverse=True)

    def render(self) -> None:
        self.template = bottle.template('merch/index', module_title='Merchandise', data=self.data,
                                        merch_email=self.server.get_merch_email(), get_static_url=self.server.get_static_url)
