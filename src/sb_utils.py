'''sugg bot utils'''

import os

data_path = '../data/'
logs_path = data_path + 'logs/'

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
