import tomli
import bottle

from typing import Dict

from .modules import BaseModule


class Gigs(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.data = list()

    def update_lists(self, gigs: Dict) -> None:
        # group by years
        years_found = [gigs[key]['date'].year for key in gigs]
        self.data = dict()
        for year in years_found:
            gigs_that_year = [gigs[key] for key in gigs if gigs[key]['date'].year == year]
            self.data[year] = gigs_that_year

        # sort gigs with year
        for year in self.data:
            self.data[year].sort(key=lambda gig: gig['date'])

    def load_from_file(self) -> None:
        filename = f'{self.root}/model/data/gigs.toml'
        with open(filename, 'rb') as file:
            gigs = tomli.load(file)

        self.update_lists(gigs)

    def render(self) -> None:
        self.template = bottle.template('gigs/index', data=self.data, email=self.email)
