import pathlib

import bottle

from enum import auto
from strenum import LowercaseStrEnum

from . import server, feed, releases, lineup, gigs, gallery, merch, presskit


class Recipient(LowercaseStrEnum):
    CONTACT = auto()
    BOOKING = auto()
    MERCH = auto()
    WEBMASTER = auto()


def get_email_address(recipient: Recipient, domain: str) -> str:
    return f'{recipient.value}@{domain}'


def run(port: int):
    args = {
        'host': '0.0.0.0',
        'domain': 'kali-yuga.de',
        'port': port,
        'debug': True,
        'reloader': False,
        'quiet': False,
        'server': 'gevent'
    }

    s = server.WebServer(args)

    contact_email = get_email_address(Recipient.CONTACT, args['domain'])

    # load feed
    f = feed.Feed(root=s.local_root, email=contact_email)
    f.load_from_file()
    f.render(contact_email=contact_email)

    # load lineup
    l = lineup.Lineup(root=s.local_root, email=contact_email)
    l.load_from_file()
    l.render(contact_email=contact_email)

    # load live shows
    g = gigs.Gigs(root=s.local_root, email=get_email_address(Recipient.BOOKING, args['domain']))
    g.load_from_file()
    g.render(contact_email=contact_email)

    # load gallery
    gal = gallery.Gallery(root=s.local_root, email=contact_email)
    gal.load_from_disc()
    gal.render(contact_email=contact_email)

    # load merchandise
    m = merch.Merch(root=s.local_root, email=get_email_address(Recipient.MERCH, args['domain']))
    for category in merch.MerchCategory:
        m.load_from_file(category)
    m.render(contact_email=contact_email)

    # load releases
    r = releases.Releases(root=s.local_root, email=contact_email)
    r.load_from_merch(m)
    r.render(contact_email=contact_email)

    # load presskit
    p = presskit.Presskit(root=s.local_root)
    p.build()

    if args['debug']:
        @s.app.get('/static/<filename>')
        def static_files(filename: str):
            root = s.get_statics_path()
            return bottle.static_file(filename, root=root)

        @s.app.get('/content/<path:path>')
        def static_content(path: str):
            root = s.local_root / 'model' / 'content'
            return bottle.static_file(path, root=root)

    @s.app.get('/')
    def feed_page():
        return f.template

    @s.app.get('/releases')
    def releases_page():
        return r.template

    @s.app.get('/lineup')
    def lineup_page():
        return l.template

    @s.app.get('/shows')
    def gigs_page():
        return g.template

    @s.app.get('/gallery')
    def gallery_page():
        return gal.template

    @s.app.get('/merch')
    def merch_page():
        return m.template

    @s.app.get('/imprint')
    @bottle.view('impressum')
    def impressum_page():
        return dict(email=contact_email, contact_email=contact_email)

    @s.app.get('/presskit')
    def static_presskit():
        path = pathlib.Path(p.zip_file.name)
        return bottle.static_file(path.name, root=path.parent, download='Kali Yuga EPK', mimetype='application/zip')

    s.run()
