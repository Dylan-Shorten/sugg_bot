'''sugg bot ping command'''

import sys
import getopt

def mode_help():
    print('prompts a responce of "pong"')
    print('usage: `sb ping [options]`')
    print('options:')
    print('    --help    displays usage info')

def main():
    '''main func'''
    opts, args = getopt.getopt(sys.argv[1:], '', ['help'])
    if len(args) != 0:
        print('invalid argc')
        return
    for opt in opts:
        if opt[0] == '--help':
            mode_help()
            return
    print('pong')

if __name__ == '__main__':
    main()
