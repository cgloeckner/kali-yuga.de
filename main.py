import bottle

import controller


def main():
    args = {
        'host': '0.0.0.0',
        'domain': 'localhost',
        'port': 8080,
        'debug': True,
        'reloader': True,
        'quiet': False,
        'server': 'gevent'
    }

    s = controller.WebServer(args)

    m = controller.Merch(s.local_root)
    m.load_from_file(controller.MerchCategory.CDS)
    m.load_from_file(controller.MerchCategory.CLOTHS)
    m.render()

    g = controller.Gigs(s.local_root)
    g.load_from_file()
    g.render()

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
    def index():
        return bottle.template('home')

    @s.app.get('/merch')
    def merch():
        return m.template

    @s.app.get('/gigs')
    def gigs():
        return g.template

    s.run()


if __name__ == '__main__':
    main()
