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

variables = {}
