'''echo command'''

import sys
import getopt

def print_info():
    '''print the info message'''
    print('prints messages')

def print_help():
    '''print the help message'''
    print('usage: `sb echo [opts] [args]`')
    print('options:')
    print('`--help`: print command usage information')
    print('`--info`: print a short description of the command')

def main(argv):
    '''main function'''
    # get optss and args
    opts, args = getopt.getopt(argv, '', ['info', 'help'])
    info_opt = False
    help_opt = False
    for opt, _ in opts:
        if opt == '--info':
            info_opt = True
        elif opt == '--help':
            help_opt = True
    # print info message
    if info_opt:
        print_info()
    # print help message
    if help_opt:
        print_help()
    # print message args
    if len(args) > 0:
        print(*args)
    elif not info_opt and not help_opt:
        print('error: no args')
        print_help()

if __name__ == '__main__':
    main(sys.argv[1:])
