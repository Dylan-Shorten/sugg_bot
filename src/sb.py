'''sugg bot processing'''

import os
import shlex
import subprocess
import sys
import pathlib

'''command string prefix'''
PREFIX = 'sb '

'''path to command src files'''
COMMANDS_PATH = os.path.dirname(os.path.realpath(__file__)) + '/commands/'

'''path to data files'''
DATA_PATH = os.path.dirname(os.path.realpath(__file__)) + '/../data/'

def parse_input_str(string):
    '''read an input string and return a response'''
    if string.startswith(PREFIX):
        return run_command_str(string[len(PREFIX):])
    return ''

def run_command_str(string):
    '''run a command string'''
    words = shlex.split(string)
    return run_command_rec(COMMANDS_PATH, words)

def run_command_rec(path, words):
    '''recursively find and run the command script'''
    if len(words) == 0:
        return 'invalid command'
    name = words[0]
    args = words[1:]
    script_path = path + 'sb_' + name + '.py'
    if os.path.isfile(script_path):
        return run_command_subprocess(script_path, args)
    folder_path = path + name + '/'
    if os.path.isdir(folder_path):
        return run_command_rec(folder_path, args)
    else:
        return 'invalid command'

def run_command_subprocess(path, args):
    '''run a python script and return the output'''
    command = [
        sys.executable,
        path
        ]
    command.extend(args)
    result = subprocess.run(command, stdout=subprocess.PIPE, check=False)
    return result.stdout.decode('utf-8')[:-1]

# def run_command(path, command):
#     if len(command) == 0:
#         return False
#     name = command[0]
#     args = command[1:]
#     script_path = path + 'sbc_' + name + '.py'
#     if os.path.isfile(script_path):
#         print(script_path)
#     else:
#         folder_path = path + name + '/'
#         if os.path.isdir(folder_path):
#             run_command(folder_path, args)
#         else:
#             print('invalid command')

# def parse_input(string):
#     if string.startswith(PREFIX):
#         command = shlex.split(string[len(PREFIX):])
#         run_command('./', command)

def read_file(path):
    '''read the contents of a file into a string'''
    contents = pathlib.Path(path).read_text()
    if contents.endswith(contents):
        return contents[:-1]
    return contents
