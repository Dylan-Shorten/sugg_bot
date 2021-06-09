"""command parser/runner"""

import shlex
import subprocess
import sys
import os

COMMAND_PREFIX = "sb"


def parse_input(string):
    """parse user input and run a command if necessary"""
    split = shlex.split(string)
    if len(split) > 0 and split[0] == COMMAND_PREFIX:
        name = split[1] if len(split) > 1 else ""
        args = split[2:] if len(split) > 2 else []
        return run_command(name, args)
    return None


def run_command(name, args):
    """run a command with args"""
    path = find_command_script(name)
    if path is not None:
        command = [sys.executable, path]
        command.extend(args)
        return run_subprocess(command)
    return "`" + name + "` is not a command"


def find_command_script(name):
    """return the path to the script if it exists"""
    folder = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(folder, "sbc_" + name + ".py")
    if os.path.isfile(path):
        return path
    return None


def run_subprocess(command):
    """run a terminal command and return it's stdout as a string"""
    result = subprocess.run(command, stdout=subprocess.PIPE, check=False)
    return result.stdout.decode("utf-8")[:-1]
