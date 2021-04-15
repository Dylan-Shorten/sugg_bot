'''sugg bot command parser'''

import shlex
import collections
import getopt

Command = collections.namedtuple('Command', ['opts', 'long_opts', 'func'])

def invalid_arg_count(name, count):
    return name + ' does not take ' + str(count) + ' args'

class CommandParser:
    commands = {}
    reactor = None
    variables = None

    def __init__(self, reactor, variables):
        self.reactor = reactor
        self.variables = variables
        self.add_command('ping', '', [], self.ping)
        self.add_command('echo', 'lu', ['lower', 'upper'], self.echo)
        self.add_command('react', '', [], self.react)
        self.add_command('listreacts', '', [], self.listreacts)
        self.add_command('set', '', [], self.set)
        self.add_command('listvars', '', [], self.listvars)

    def add_command(self, name, opts, long_opts, func):
        self.commands[name] = Command(opts, long_opts, func)

    # parses command input
    # returns a string containing command output
    # command prefix should be trimmed off before calling parse
    def parse(self, string):
        words = shlex.split(string)
        if len(words) < 1:
            return 'no command'
        name = words[0]
        if not name in self.commands:
            return name + ' is not a command'
        com = self.commands[name]
        try:
            (opts, args) = getopt.getopt(words[1:], com.opts, com.long_opts)
        except getopt.GetoptError as error:
            return error
        return com.func(opts, args)

    def ping(self, opts, args):
        if len(args) > 0:
            return invalid_arg_count('ping', len(args))
        return 'pong'

    def echo(self, opts, args):
        if len(args) == 0:
            return invalid_arg_count('echo', 0)
        string = ''
        for arg in args:
            string += arg + ' '
        string = string[:-1]
        for (opt, arg) in opts:
            if opt in ['-l', '--lower']:
                string = string.lower()
            elif opt in ['-u', '--upper']:
                string = string.upper()
        return string

    def react(self, opts, args):
        if not len(args) == 2:
            return invalid_arg_count('react', len(args))
        self.reactor.reacts[args[0]] = args[1]
        self.reactor.save_reacts()
        return 'set react ' + args[0] + ' to ' + args[1]

    def listreacts(self, opts, args):
        if len(self.reactor.reacts) == 0:
            return 'no reacts'
        string = ''
        for i in self.reactor.reacts:
            string += i + ' = ' + self.reactor.reacts[i] + '\n'
        return string[:-1]

    def set(self, opts, args):
        if not len(args) == 2:
            return invalid_arg_count('set', len(args))
        self.variables.variables[args[0]] = args[1]
        self.variables.save_vars()
        return 'set var ' + args[0] + ' to ' + args[1]

    def listvars(self, opts, args):
        if len(self.variables.variables) == 0:
            return 'no vars'
        string = ''
        for i in self.variables.variables:
            string += i + ' = ' + self.variables.variables[i] + '\n'
        return string[:-1]