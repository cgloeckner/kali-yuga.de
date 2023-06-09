import tomli
import bottle

from typing import Dict, List

from .modules import BaseModule, BaseWebServer


class Gigs(BaseModule):
    def __init__(self, api: BaseWebServer) -> None:
        super().__init__(api)

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
        filename = f'{self.server.local_root}/model/data/gigs.toml'
        with open(filename, 'rb') as file:
            gigs = tomli.load(file)

        self.data = self.process_gigs(gigs)

    def render(self) -> None:
        self.template = bottle.template('gigs/index', module_title='Live Shows', data=self.data,
                                        booking_email=self.server.get_booking_email(),
                                        get_static_url=self.server.get_static_url)
