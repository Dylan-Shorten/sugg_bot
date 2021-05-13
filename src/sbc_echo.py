'''sugg bot echo command'''

import sys
import getopt

def mode_help():
    print('print something')
    print('usage: `sb echo [options] message...`')
    print('options:')
    print('    --help    display usage info')

def main():
    '''main func'''
    opts, args = getopt.getopt(sys.argv[1:], '', ['help'])
    for opt in opts:
        if opt[0] == '--help':
            mode_help()
            return
    if len(args) == 0:
        print('invalid argc')
        return
    for arg in args:
        print(arg)

if __name__ == '__main__':
    main()