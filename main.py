#!/bin/python3

import sys

import controller


def main():
    server_kwargs = {
        'host': '0.0.0.0',
        'server': 'gevent',
        'domain': 'kali-yuga.de',
        'port': 8000,
        'debug': '--debug' in sys.argv,
        'reloader': '--debug' in sys.argv,
        'quiet': '--debug' not in sys.argv,
        'reverse_proxy': '--debug' not in sys.argv
    }

    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        server_kwargs['port'] = int(sys.argv[index + 1])

    if '-h' in sys.argv:
        print('Usage: -p <portnumber>')
        return

    controller.main(server_kwargs, '--render' in sys.argv)


if __name__ == '__main__':
    main()
