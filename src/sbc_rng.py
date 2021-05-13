'''sugg bot rng command'''

import sys
import getopt
import random

def mode_help():
    print('generate a random number')
    print('usage: `sb rng [options] [min] max`')
    print('min and max are inclusive')
    print('if min is omitted, it is assumed to be 0')
    print('options:')
    print('    --help    display usage info')

def main():
    opts, args = getopt.getopt(sys.argv[1:], '', ['help'])
    for opt in opts:
        if opt[0] == '--help':
            mode_help()
            return
    print('not implemented')

if __name__ == '__main__':
    main()
