'''sugg bot var command'''

import sys
import getopt

import sb_utils

def read_vars():
    '''read vars from file'''
    return sb_utils.read_dict(sb_utils.DATA_PATH + 'vars.txt')

def write_vars(variables):
    '''write vars to file'''
    sb_utils.write_dict(variables, sb_utils.DATA_PATH + 'vars.txt')

def mode_var(args):
    '''var set mode'''
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
    '''var list mode'''
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
    '''var delete mode'''
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

def mode_help():
    '''var help message'''
    print('for controlling variables')
    print('options:\n-l: list variables\n-d: delete a variable')

def main():
    '''main func'''
    func = mode_var
    opts, args = getopt.getopt(sys.argv[1:], 'ld', ['list', 'delete', 'help'])
    for opt in opts:
        if opt[0] in ['-l', '--list']:
            func = mode_list
        elif opt[0] in ['-d', '--delete']:
            func = mode_delete
        elif opt[0] == '--help':
            mode_help()
            return
    func(args)

if __name__ == '__main__':
    main()
