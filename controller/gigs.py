import tomli
import bottle

from typing import Dict, List

from .modules import BaseModule


class Gigs(BaseModule):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.data = dict()

    @staticmethod
    def process_gigs(gigs: Dict[str, Dict]) -> Dict[int, List]:
        """Groups the given dictionary of gigs by year and returns a dictionary."""
        # group by years
        years_found = [gigs[key]['date'].year for key in gigs]
        data = dict()
        for year in years_found:
            gigs_that_year = [gigs[key] for key in gigs if gigs[key]['date'].year == year]
            data[year] = gigs_that_year

        # sort gigs with date (starting with most recent)
        for year in data:
            data[year].sort(key=lambda gig: gig['date'], reverse=True)

        return data

    def load_from_file(self) -> None:
        filename = f'{self.root}/model/data/gigs.toml'
        with open(filename, 'rb') as file:
            gigs = tomli.load(file)

        self.data = self.process_gigs(gigs)

    def render(self, contact_email: str) -> None:
        self.template = bottle.template('gigs/index', data=self.data, email=self.email, contact_email=contact_email)
