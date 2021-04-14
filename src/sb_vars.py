'''string var replacer'''

def replace_range(string, start, length, value):
    '''remove a range in a string and replace it with a value'''
    return string[:start] + value + string[start + length:]

def replace_var(string, name, value):
    '''replace all instances of a var in a string'''
    var_string = '{' + name + '}'
    while True:
        i = string.find(var_string)
        if i == -1:
            break
        string = replace_range(string, i, len(var_string), value)
    return string

def replace_vars(string):
    '''replace all instances of vars in a string'''
    for name in variables:
        string = replace_var(string, name, variables[name])
    return string

def load_vars():
    '''load vars from file'''
    variables.clear()
    with open('../data/vars.txt') as vars_file:
        for line in vars_file:
            split = line.replace('\n', '').split('=')
            variables[split[0]] = split[1]

def save_vars():
    '''save vars to file'''
    string = ''
    for i in variables:
        string += i + '=' + variables[i] + '\n'
    string = string[:-1]
    with open('../data/vars.txt', 'w') as vars_file:
        vars_file.write(string)

# pylint: disable=invalid-name
variables = {}
