import getopt
import collections
import shlex

Command = collections.namedtuple('Command', ['opts', 'lopts', 'func'])

def concat_strs(strings):
    full = ''
    for i in strings:
        full += i
    return full

def load_dict(path):
    result = {}
    with open(path) as f:
        for line in f:
            i = line.find('=')
            if i == -1:
                continue
            name = line[:i]
            val = line[i + 1:]
            if val.endswith('\n'):
                val = val[:-1]
            result[name] = val
    return result

def save_dict(dict, path):
    string = ''
    for key in dict:
        val = dict[key]
        string += key + '=' + val + '\n'
    string = string[:-1]
    with open(path, 'w') as f:
        f.write(string)

class SuggBot:
    prefix = ''
    reacts_path = ''
    reacts = {}
    commands = {}

    def __init__(self, prefix, data_path):
        self.prefix = prefix
        self.reacts_path = data_path + 'reacts.txt'
        self.reacts = load_dict(self.reacts_path)
        self.commands = {
            'ping': Command('', [], self.__ping),
            'echo': Command('lu', [], self.__echo),
            'react': Command('l', [], self.__react)
            }

    def parse(self, string):
        react = self.__get_react(string)
        if react != '':
            return react
        if string.startswith(self.prefix):
            com_string = string[len(self.prefix):]
            return self.__run_command(com_string)
        return ''

    def __get_react(self, string):
        if string in self.reacts:
            return self.reacts[string]
        return ''

    def __run_command(self, string):
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

    def __ping(self, opts, args):
        if len(args) != 0:
            return 'ping cannot take ' + str(len(args)) + ' args'
        return 'pong'

    def __echo(self, opts, args):
        if len(args) != 1:
            return 'echo cannot take ' + str(len(args)) + ' args'
        string = args[0]
        for opt, arg in opts:
            if opt == '-l':
                string = string.lower()
            elif opt == '-u':
                string = string.upper()
        return string

    def __react(self, opts, args):
        mode_react = 0
        mode_list = 1
        mode = mode_react
        for opt, arg in opts:
            if opt == '-l':
                mode = mode_list
        if mode == mode_react:
            return self.__react_react(opts, args)
        else:
            return self.__react_list(opts, args)

    def __react_react(self, opts, args):
        if len(args) != 2:
            return 'react cannot take ' + str(len(args)) + ' args'
        name = args[0]
        val = args[1]
        self.reacts[name] = val
        save_dict(self.reacts, self.reacts_path)
        return 'set react \"' + name + '\" = ' + '\"' + val + '\"'

    def __react_list(self, opts, args):
        if len(args) != 0:
            return 'react cannot take ' + str(len(args)) + ' args'
        string = ''
        for key in self.reacts:
            val = self.reacts[key]
            string += key + ' = ' + val + '\n'
        string = string[:-1]
        return string
