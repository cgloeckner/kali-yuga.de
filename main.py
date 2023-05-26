import pathlib

import server


def main():
    root = pathlib.Path('./')
    args = {
        'host': '0.0.0.0',
        'domain': 'localhost',
        'port': 8080,
        'debug': True,
        'reloader': True,
        'quiet': False,
        'server': 'gevent'
    }

    s = server.WebServer(root, args)

    @s.app.get('/')
    def index():
        return 'hallo'

    s.run()


if __name__ == '__main__':
    main()
