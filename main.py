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
    m = controller.Merch(s)
    m.load_from_file(controller.MerchCategory.CDS)
    m.load_from_file(controller.MerchCategory.CLOTHS)
    m.render()

    if args['debug']:
        @s.app.get('/static/<filename>')
        def static_files(filename: str):
            root = s.get_statics_path()
            return bottle.static_file(filename, root=root)

        @s.app.get('/static/merch/<category>/<filename>')
        def static_merch(category: str, filename: str):
            root = s.get_statics_path() / 'merch' / category
            return bottle.static_file(filename, root=root)

    @s.app.get('/')
    def index():
        return m.template

    s.run()


if __name__ == '__main__':
    main()
