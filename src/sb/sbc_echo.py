'''echo command'''

import sys

def main(argv):
    '''main function'''
    print(*argv)

if __name__ == '__main__':
    main(sys.argv[1:])
