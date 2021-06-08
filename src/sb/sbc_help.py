'''help command'''

import sys
import os
import getopt

import commands

INFO_STR = 'displays help messages'

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

def print_generic_help():
    # print the help message
    print('command usage:')
    print('`sb <command> [opts] [args]`')
    print('')
    # print list of commands
    print('commands:')
    for name, path in get_commands():
        if name == 'help':
            print(name + ': ' + INFO_STR)
            continue
        info_str = commands.run_subprocess([sys.executable, path, '--info'])
        print(name + ': ' + info_str)
    print('')
    # print some extra info
    print('for more info about a command, run `sb help <command>` or `sb <command> --help`')

def main(argv):
    '''main function'''
    # get opts and args
    opts, args = getopt.getopt(argv, '', ['help', 'info'])
    info_opt = False
    for opt, _ in opts:
        if opt == '--info':
            info_opt = True

    # print info
    if info_opt:
        print(INFO_STR)

    # print command info
    for i in args:
        script = commands.find_command_script(i)
        command = [sys.executable, script, '--info', '--help']
        result = commands.run_subprocess(command)
        print(result)

    # print generic help
    if not info_opt and len(args) == 0:
        print_generic_help()

if __name__ == '__main__':
    main(sys.argv[1:])
