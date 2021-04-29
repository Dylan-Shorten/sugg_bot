'''sugg bot'''

import getopt
import collections
import shlex
import os

Command = collections.namedtuple('Command', ['opts', 'lopts', 'func'])

def read_dict(path):
    '''read a dict from file'''
    result = {}
    if not os.path.isfile(path):
        return result
    with open(path, 'r') as file:
        for line in file:
            i = line.find('=')
            if i == -1:
                continue
            name = line[:i]
            val = line[i + 1:]
            if val.endswith('\n'):
                val = val[:-1]
            result[name] = val
    return result

def write_dict(dictionary, path):
    '''write a dict to file'''
    string = ''
    for key in dictionary:
        val = dictionary[key]
        string += key + '=' + val + '\n'
    string = string[:-1]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(string)

# pylint: disable=too-few-public-methods
class SuggBot:
    '''sugg bot class'''
    prefix = ''
    variables_path = ''
    variables = {}
    reacts_path = ''
    reacts = {}
    commands = {}

    def __init__(self, prefix, data_path):
        '''constructor'''
        self.prefix = prefix
        self.variables_path = data_path + 'variables.txt'
        self.variables = read_dict(self.variables_path)
        self.reacts_path = data_path + 'reacts.txt'
        self.reacts = read_dict(self.reacts_path)
        self.commands = {
            'ping': Command('', [], self.__ping),
            'echo': Command('lu', [], self.__echo),
            'react': Command('ld', [], self.__react),
            'var': Command('ld', [], self.__var)
            }

    def parse(self, string):
        '''parse an input string'''
        string = self.__replace_vars(string)
        react = self.__get_react(string)
        if react != '':
            return react
        if string.startswith(self.prefix):
            com_string = string[len(self.prefix):]
            return self.__run_command(com_string)
        return ''

    def __get_react(self, string):
        '''get a react if it exists'''
        if string in self.reacts:
            return self.reacts[string]
        return ''

    def __run_command(self, string):
        '''run a command string'''
        words = shlex.split(string)
        name = words[0]
        if not name in self.commands:
            return name + ' is not a command'
        com = self.commands[name]
        try:
            opts, args = getopt.getopt(words[1:], com.opts, com.lopts)
        except getopt.GetoptError as error:
            return error
        return com.func(opts, args)

    def __replace_vars(self, string):
        for i in range(0, 100):
            replaced = False
            for name in self.variables:
                var_str = '<' + name + '>'
                result = string.replace(var_str, self.variables[name])
                if result != string:
                    string = result
                    replaced = True
            if not replaced:
                break
        return string

    # pylint: disable=unused-argument
    # pylint: disable=no-self-use

    def __ping(self, opts, args):
        '''ping command'''
        if len(args) != 0:
            return 'ping cannot take ' + str(len(args)) + ' args'
        return 'pong'

    def __echo(self, opts, args):
        '''echo command'''
        if len(args) != 1:
            return 'echo cannot take ' + str(len(args)) + ' args'
        string = args[0]
        for opt in opts:
            if opt[0] == '-l':
                string = string.lower()
            elif opt[0] == '-u':
                string = string.upper()
        return string

    def __react(self, opts, args):
        '''react command'''
        mode_react = 0
        mode_list = 1
        mode_del = 2
        mode = mode_react
        for opt in opts:
            if opt[0] == '-l':
                mode = mode_list
            elif opt[0] == '-d':
                mode = mode_del
        if mode == mode_react:
            return self.__react_react(opts, args)
        if mode == mode_list:
            return self.__react_list(opts, args)
        return self.__react_del(opts, args)

    def __react_react(self, opts, args):
        '''react add command'''
        if len(args) != 2:
            return 'react cannot take ' + str(len(args)) + ' args'
        name = args[0]
        val = args[1]
        self.reacts[name] = val
        write_dict(self.reacts, self.reacts_path)
        return 'set react \"' + name + '\" = ' + '\"' + val + '\"'

    def __react_list(self, opts, args):
        '''react list command'''
        if len(args) != 0:
            return 'react cannot take ' + str(len(args)) + ' args'
        if len(self.reacts) == 0:
            return 'no reacts'
        string = ''
        for key in self.reacts:
            val = self.reacts[key]
            string += key + ' = ' + val + '\n'
        string = string[:-1]
        return string

    def __react_del(self, opts, args):
        '''react del command'''
        if len(args) != 1:
            return 'react cannot take ' + str(len(args)) + ' args'
        name = args[0]
        if not name in self.reacts:
            return 'react \"' + name + '\" does not exist'
        del self.reacts[name]
        write_dict(self.reacts, self.reacts_path)
        return 'deleted react \"' + name + '\"'

    def __var(self, opts, args):
        '''var command'''
        mode_var = 0
        mode_list = 1
        mode_del = 2
        mode = mode_var
        for opt in opts:
            if opt[0] == '-l':
                mode = mode_list
            elif opt[0] == '-d':
                mode = mode_del
        if mode == mode_var:
            return self.__var_var(opts, args)
        if mode == mode_list:
            return self.__var_list(opts, args)
        return self.__var_del(opts, args)

    def __var_var(self, opts, args):
        '''var add command'''
        if len(args) != 2:
            return 'var cannot take ' + str(len(args)) + ' args'
        name = args[0]
        val = args[1]
        self.variables[name] = val
        write_dict(self.variables, self.variables_path)
        return 'set var \"' + name + '\" = ' + '\"' + val + '\"'

    def __var_list(self, opts, args):
        '''var list command'''
        if len(args) != 0:
            return 'var cannot take ' + str(len(args)) + ' args'
        if len(self.variables) == 0:
            return 'no vars'
        string = ''
        for key in self.variables:
            val = self.variables[key]
            string += key + ' = ' + val + '\n'
        string = string[:-1]
        return string

    def __var_del(self, opts, args):
        '''var del command'''
        if len(args) != 1:
            return 'var cannot take ' + str(len(args)) + ' args'
        name = args[0]
        if not name in self.variables:
            return 'var \"' + name + '\" does not exist'
        del self.variables[name]
        write_dict(self.variables, self.variables_path)
        return 'deleted var \"' + name + '\"'


    # pylint: disable=no-self-use
    # pylint: enable=unused-argument

# pylint: enable=too-few-public-methods
