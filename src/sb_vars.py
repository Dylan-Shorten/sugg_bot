'''sugg bot variables'''

def replace_range(string, start, length, value):
    return string[:start] + value + string[start + length:]

def replace_var(string, name, value):
    var_string = '<' + name + '>'
    count = 0
    while True:
        i = string.find(var_string)
        if i == -1:
            break
        string = replace_range(string, i, len(var_string), value)
        count += 1
    return (string, count)

class VarHandler:
    file_path = ''
    variables = {}

    def __init__(self, file_path):
        self.file_path = file_path
        self.load_vars()

    def replace_vars(self, string):
        while True:
            total = 0
            for name in self.variables:
                (string, count) = replace_var(string, name, self.variables[name])
                total += count
            if total == 0:
                break
        return string

    def load_vars(self):
        self.variables.clear()
        with open(self.file_path) as vars_file:
            for line in vars_file:
                i = line.index('=')
                name = line[:i]
                value = line[i + 1:].replace('\n', '')
                self.variables[name] = value

    def save_vars(self):
        string = ''
        for i in self.variables:
            string += i + '=' + self.variables[i] + '\n'
        string = string[:-1]
        with open(self.file_path, 'w') as vars_file:
            vars_file.write(string)
