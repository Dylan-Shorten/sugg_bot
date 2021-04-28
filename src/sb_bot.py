import getopt
import collections
import shlex

Command = collections.namedtuple('Command', ['opts', 'lopts', 'argc', 'func'])

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
            'ping': Command('', [], 0, self.__ping),
            'echo': Command('lu', [], 1, self.__echo),
            'react': Command('', [], 2, self.__react),
            'listreacts': Command('', [], 0, self.__listreacts)
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
        if len(args) != com.argc:
            return name + ' takes ' + str(com.argc) + ' args'
        return com.func(opts, args)

    def __ping(self, opts, args):
        return 'pong'

    def __echo(self, opts, args):
        string = args[0]
        for opt, arg in opts:
            if opt == '-l':
                string = string.lower()
            elif opt == '-u':
                string = string.upper()
        return string

    def __react(self, opts, args):
        name = args[0]
        val = args[1]
        self.reacts[name] = val
        save_dict(self.reacts, self.reacts_path)
        return 'set react \"' + name + '\" = ' + '\"' + val + '\"'

    def __listreacts(self, opts, args):
        string = ''
        for key in self.reacts:
            val = self.reacts[key]
            string += key + ' = ' + val + '\n'
        string = string[:-1]
        return string
