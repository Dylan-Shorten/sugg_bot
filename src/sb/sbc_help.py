'''help command'''

import sys
import os
import getopt

import commands

INFO_STR = 'prints help messages and info'

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

def print_info():
    '''print the info message'''
    print(INFO_STR)

def print_help():
    '''print the help message'''
    print('usage: `sb help [opts] [args]`')
    print('options:')
    print('`--help`: print command usage information')
    print('`--info`: print a short description of the command')

def print_generic_help():
    '''print the generic help message'''
    # print the help message
    print('command usage:')
    print('`sb <command> [opts] [args]`')
    # print list of commands
    print('commands:')
    for name, path in get_commands():
        info_str = INFO_STR
        if name != 'help':
            info_str = commands.run_subprocess([sys.executable, path, '--info'])
        print('`' + name + '`: ' + info_str)
    # print some extra info
    print('for more info about a command, run `sb help <command>`')

def main(argv):
    '''main function'''
    # get opts and args
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
    # print args command info
    count = 0
    for i in args:
        script = commands.find_command_script(i)
        if script is None:
            print('`' + i + '` is not a command')
            continue
        command = [sys.executable, script, '--info', '--help']
        result = commands.run_subprocess(command)
        if len(args) > 1:
            print('`' + i + '`:')
        print(result)
        count += 1
        if count < len(args):
            print('')
    # print generic help
    if not info_opt and not help_opt and len(args) == 0:
        print_generic_help()

if __name__ == '__main__':
    main(sys.argv[1:])
