'''help command'''

import sys
import os
import getopt

import commands

def get_commands():
    '''get a list of bot command python scripts'''
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(file_path)
    prefix = 'sbc_'
    ext = '.py'
    scripts = []
    for i in os.listdir(path):
        if i.startswith(prefix) and i.endswith(ext):
            name = i[len(prefix):-len(ext)]
            script = os.path.join(path, i)
            scripts.append((name, script))
    return scripts

def main(argv):
    '''main function'''
    # get opts and args
    opts, args = getopt.getopt(argv, '', ['info'])
    for opt, _ in opts:
        if opt == '--info':
            print('displays the help message')
    # print the help message
    print('command usage:')
    print('`sb <command> [opts] [args]`')
    print('')
    # print list of commands
    print('commands:')
    for name, path in get_commands():
        info_str = commands.run_subprocess([sys.executable, path, '--info'])
        print(name + ': ' + info_str)
    print('')
    # print some extra info
    print('for more info about a command, run `sb help <command>` or `sb <command> --help`')

if __name__ == '__main__':
    main(sys.argv[1:])
