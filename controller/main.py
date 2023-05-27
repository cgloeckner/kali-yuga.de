import bottle

from . import server, merch, gigs


from enum import auto
from strenum import LowercaseStrEnum


class Recipient(LowercaseStrEnum):
    CONTACT = auto()
    BOOKING = auto()
    MERCH = auto()
    WEBMASTER = auto()


def get_email_address(recipient: Recipient, domain: str) -> str:
    return f'{recipient.value}@{domain}'


def run():
    args = {
        'host': '0.0.0.0',
        'domain': 'localhost',
        'port': 8001,
        'debug': True,
        'reloader': True,
        'quiet': False,
        'server': 'gevent'
    }

    s = server.WebServer(args)

    # load merchandise
    m = merch.Merch(root=s.local_root, email=get_email_address(Recipient.MERCH, args['domain']))
    m.load_from_file(merch.MerchCategory.CDS)
    m.load_from_file(merch.MerchCategory.CLOTHS)
    m.render()

    # load live shows
    g = gigs.Gigs(root=s.local_root, email=get_email_address(Recipient.BOOKING, args['domain']))
    g.load_from_file()
    g.render()

    contact_email = get_email_address(Recipient.CONTACT, args['domain'])

    if args['debug']:
        @s.app.get('/static/<filename>')
        def static_files(filename: str):
            root = s.get_statics_path()
            return bottle.static_file(filename, root=root)

        @s.app.get('/content/<path:path>')
        def static_content(path: str):
            root = s.local_root / 'model' / 'images'
            return bottle.static_file(path, root=root)

    @s.app.get('/')
    def home_page():
        return bottle.template('home')

    @s.app.get('/merchandise')
    def merch_page():
        return m.template

    @s.app.get('/live-shows')
    def gigs_page():
        return g.template

    @s.app.get('/impressum')
    @bottle.view('impressum')
    def impressum_page():
        return dict(email=contact_email)

    s.run()
