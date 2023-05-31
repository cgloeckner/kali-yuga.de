import sys

import controller


def main():
    port = 8080
    reverse_proxy = False
    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        port = int(sys.argv[index + 1])

    if '--reverse-proxy' in sys.argv:
        reverse_proxy = True

    if '-h' in sys.argv:
        print('Usage: -p <portnumber>')
        return

    controller.run(port, reverse_proxy)


if __name__ == '__main__':
    main()
