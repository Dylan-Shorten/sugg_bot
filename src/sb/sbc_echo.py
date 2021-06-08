'''echo command'''

import sys
import getopt

def main(argv):
    '''main function'''
    opts, args = getopt.getopt(argv, '', ['help', 'info'])
    help_opt = False
    info_opt = False
    for opt, _ in opts:
        if opt == '--help':
            help_opt = True
        if opt == '--info':
            info_opt = True
    if help_opt:
        print('usage: `sb echo [opts] [args]`')
    if info_opt:
        print('prints messages')
    if len(args):
        print(*args)

if __name__ == '__main__':
    main(sys.argv[1:])
