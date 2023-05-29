import sys

import controller


def main():
    port = 8080
    if '-p' in sys.argv:
        index = sys.argv.index('-p')
        port = int(sys.argv[index + 1])

    if '-h' in sys.argv:
        print('Usage: -p <portnumber>')
        return

    controller.run(port)


if __name__ == '__main__':
    main()
