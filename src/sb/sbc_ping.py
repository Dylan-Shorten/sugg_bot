"""ping command"""

import sys
import getopt


def print_info():
    """print the info message"""
    print('prints "pong"')


def print_help():
    """print the help message"""
    print("usage: `sb ping [opts]`")
    print("options:")
    print("`--help`: print command usage information")
    print("`--info`: print a short description of the command")


def main(args):
    """main function"""
    info_opt = False
    help_opt = False
    opts, _ = getopt.getopt(args, "", ["info", "help"])
    for opt, _ in opts:
        if opt == "--info":
            info_opt = True
        elif opt == "--help":
            help_opt = True
    if info_opt:
        print_info()
    if help_opt:
        print_help()
    if not info_opt and not help_opt:
        print("pong")


if __name__ == "__main__":
    main(sys.argv[1:])
