import shlex
import subprocess
import sys
import os

COMMAND_PREFIX = 'sb'

def parse_input(string, scripts_path):
    '''parse user input and run a command if necessary'''
    split = shlex.split(string)
    if len(split) > 0 and split[0] == COMMAND_PREFIX:
        name = split[1] if len(split) > 1 else ''
        args = split[2:] if len(split) > 2 else []
        return run_command(name, args, scripts_path)
    return None

def run_command(name, args, scripts_path):
    '''run a command with args'''
    script = 'sbc-' + name + '.py'
    script_path = os.path.join(scripts_path, script)
    if os.path.isfile(script_path):
        command = [sys.executable]
        command.append(script_path)
        command.extend(args)
        return run_subprocess(command)
    return '"' + name + '" is not a command'

def run_subprocess(command):
    '''run a terminal command and return it's stdout as a string'''
    result = subprocess.run(command, stdout=subprocess.PIPE, check=False)
    return result.stdout.decode('utf-8')[:-1]
