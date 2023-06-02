import pathlib

import bottle

from . import server, feed, releases, lineup, gigs, gallery, merch, presskit


def export_html(html: str, filename: pathlib.Path) -> None:
    with open(filename, 'w') as file:
        file.write(html)


def build(domain: str):
    args = {
        'host': '0.0.0.0',
        'domain': domain,
        'port': 8000,
        'debug': False,
        'reloader': False,
        'quiet': True,
        'server': 'gevent',
        'reverse_proxy': True
    }

    s = server.WebServer(args)

    root = pathlib.Path('./.build')
    root.mkdir(exist_ok=True)

    # load feed
    f = feed.Feed(api=s)
    f.load_from_file()
    f.render()
    export_html(f.template, root / 'index.html')

    # load lineup
    l = lineup.Lineup(api=s)
    l.load_from_file()
    l.render()
    export_html(l.template, root / 'lineup.html')

    # load live shows
    g = gigs.Gigs(api=s)
    g.load_from_file()
    g.render()
    export_html(g.template, root / 'shows.html')

    # load gallery
    gal = gallery.Gallery(api=s)
    gal.load_from_disc()
    gal.render()
    export_html(gal.template, root / 'gallery.html')

    # load merchandise
    m = merch.Merch(api=s)
    for category_str in merch.MerchCategory:
        m.load_from_file(merch.MerchCategory(category_str))
    m.render()
    export_html(m.template, root / 'merch.html')

    # load releases
    r = releases.Releases(api=s)
    r.load_from_merch(m)
    r.render()
    export_html(r.template, root / 'releases.html')

    # build presskit (as static file)
    p = presskit.Presskit(api=s)
    p.build()

    # render presskit redirect page
    epk = bottle.template('epk_redirect', url=s.get_static_url('/presskit.zip'))
    export_html(epk, root / 'presskit.html')

    # render impressum
    i = bottle.template('impressum', contact_email=s.get_contact_email(), get_static_url=s.get_static_url)
    export_html(i, root / 'impressum.html')

    print('Rendered HTML to files')


def run(domain: str, port: int, reverse_proxy: bool):
    args = {
        'host': '0.0.0.0',
        'domain': domain,
        'port': port,
        'debug': not reverse_proxy,
        'reloader': False,
        'quiet': reverse_proxy,
        'server': 'gevent',
        'reverse_proxy': reverse_proxy
    }

    s = server.WebServer(args)

    # load feed
    f = feed.Feed(api=s)
    f.load_from_file()
    f.render()

    # load lineup
    l = lineup.Lineup(api=s)
    l.load_from_file()
    l.render()

    # load live shows
    g = gigs.Gigs(api=s)
    g.load_from_file()
    g.render()

    # load gallery
    gal = gallery.Gallery(api=s)
    gal.load_from_disc()
    gal.render()

    # load merchandise
    m = merch.Merch(api=s)
    for category_str in merch.MerchCategory:
        m.load_from_file(merch.MerchCategory(category_str))
    m.render()

    # load releases
    r = releases.Releases(api=s)
    r.load_from_merch(m)
    r.render()

    # build presskit (as static file)
    p = presskit.Presskit(api=s)
    p.build()

    if not reverse_proxy:
        @s.app.get('/static/<path:path>')
        def static_files(path: str):
            root = s.get_static_path()
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
        return dict(contact_email=s.get_contact_email(), get_static_url=s.get_static_url)

    @s.app.get('/presskit')
    def static_presskit():
        path = pathlib.Path(p.zip_file.name)
        return bottle.static_file(path.name, root=path.parent, download='Kali Yuga EPK', mimetype='application/zip')

    s.run()
