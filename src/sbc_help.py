'''sugg bot help command'''

import sys
import os

def main():
    '''main func'''
    if len(sys.argv) != 1:
        print('invalid argc')
        return
    print('commands:```')
    for i in os.listdir():
        prefix = 'sbc_'
        suffix = '.py'
        if i.startswith(prefix) and i.endswith(suffix):
            name = i[len(prefix):-len(suffix)]
            print(name)
    print('```for usage information about a specific command, run it with the --help option')

if __name__ == '__main__':
    main()
