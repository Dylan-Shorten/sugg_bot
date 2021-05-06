import sys
import getopt

import sb_utils

def read_vars():
    return sb_utils.read_dict(sb_utils.data_path + 'vars.txt')

def write_vars(variables):
    sb_utils.write_dict(variables, sb_utils.data_path + 'vars.txt')

def mode_var(args):
    if len(args) != 2:
        print('invalid argc')
        return
    variables = read_vars()
    name = args[0]
    value = args[1]
    variables[name] = value
    write_vars(variables)
    print('set react', name, 'to', value)

def mode_list(args):
    if len(args) != 0:
        print('invalid argc')
        return
    variables = read_vars()
    if len(variables) == 0:
        print('no variables')
        return
    for i in variables:
        print(i, '=', variables[i])

def mode_delete(args):
    if len(args) != 1:
        print('invalid argc')
        return
    variables = read_vars()
    name = args[0]
    if name in variables:
        variables.pop(name)
        write_vars(variables)
        print('deleted var', name)
        return
    print('var', name, 'does not exist')

def main():
    func = mode_var
    opts, args = getopt.getopt(sys.argv[1:], 'ld', ['list', 'delete'])
    for opt, arg in opts:
        if opt in ['-l', '--list']:
            func = mode_list
        elif opt in ['-d', '--delete']:
            func = mode_delete
    func(args)

if __name__ == '__main__':
    main()
