'''ping command'''

import sys
import getopt

def main(args):
    '''main function'''
    info_opt = False
    opts, _ = getopt.getopt(args, '', ['help', 'info'])
    for opt, _ in opts:
        if opt in ['--help', '--info']:
            info_opt = True
    if info_opt:
        print('prints "pong"')
    else:
        print('pong')

if __name__ == '__main__':
    main(sys.argv[1:])
