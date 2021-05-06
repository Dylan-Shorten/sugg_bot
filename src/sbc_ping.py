'''sugg bot ping command'''

import sys

def main():
    '''main func'''
    if len(sys.argv) != 1:
        print('invalid argc')
        return
    print('pong')

if __name__ == '__main__':
    main()
