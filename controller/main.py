import pathlib

import bottle

from . import server, modules, feed, releases, lineup, gigs, gallery, merch, presskit


class Homepage:
    def __init__(self, api: modules.ServerApi) -> None:
        # load feed
        self.feed = feed.Feed(api=api)
        self.feed.load_from_file()
        self.feed.render()

        # load lineup
        self.lineup = lineup.Lineup(api=api)
        self.lineup.load_from_file()
        self.lineup.render()

        # load live shows
        self.gigs = gigs.Gigs(api=api)
        self.gigs.load_from_file()
        self.gigs.render()

        # load gallery
        self.gallery = gallery.Gallery(api=api)
        self.gallery.load_from_disc()
        self.gallery.render()

        # load merchandise
        self.merch = merch.Merch(api=api)
        for category_str in merch.MerchCategory:
            self.merch.load_from_file(merch.MerchCategory(category_str))
        self.merch.render()

        # load releases
        self.releases = releases.Releases(api=api)
        self.releases.load_from_merch(self.merch)
        self.releases.render()

        # build presskit (as static file)
        self.presskit = presskit.Presskit(api=api)
        self.presskit.build()

    @staticmethod
    def export_html(html: str, filename: pathlib.Path) -> None:
        with open(filename, 'w') as file:
            file.write(html)


def main(server_kwargs, render_only: bool):
    # setup webserver
    api = server.WebServer(server_kwargs)

    # load homepage
    homepage = Homepage(api)

    # export html
    root = pathlib.Path('./.build')
    root.mkdir(exist_ok=True)

    homepage.export_html(homepage.feed.template, root / 'index.html')
    homepage.export_html(homepage.lineup.template, root / 'lineup.html')
    homepage.export_html(homepage.gigs.template, root / 'shows.html')
    homepage.export_html(homepage.gallery.template, root / 'gallery.html')
    homepage.export_html(homepage.merch.template, root / 'merch.html')
    homepage.export_html(homepage.releases.template, root / 'releases.html')

    # render presskit redirect page
    epk = bottle.template('epk_redirect', url=api.get_static_url('/presskit.zip'))
    homepage.export_html(epk, root / 'presskit.html')

    # render impressum
    i = bottle.template('impressum', contact_email=api.get_contact_email(), get_static_url=api.get_static_url)
    homepage.export_html(i, root / 'imprint.html')

    if render_only:
        return

    if not server_kwargs['reverse_proxy']:
        @api.app.get('/static/<path:path>')
        def static_files(path: str):
            static_root = api.get_static_path()
            return bottle.static_file(path, root=static_root)

    @api.app.get('/')
    def feed_page():
        return homepage.feed.template

    @api.app.get('/releases')
    def releases_page():
        return homepage.releases.template

    @api.app.get('/lineup')
    def lineup_page():
        return homepage.lineup.template

    @api.app.get('/shows')
    def gigs_page():
        return homepage.gigs.template

    @api.app.get('/gallery')
    def gallery_page():
        return homepage.gallery.template

    @api.app.get('/merch')
    def merch_page():
        return homepage.merch.template

    @api.app.get('/imprint')
    @bottle.view('impressum')
    def impressum_page():
        return dict(contact_email=api.get_contact_email(), get_static_url=api.get_static_url)

    @api.app.get('/presskit')
    def static_presskit():
        path = pathlib.Path(homepage.presskit.zip_file)
        return bottle.static_file(path.name, root=path.parent, download='Kali Yuga EPK', mimetype='application/zip')

    api.run()
