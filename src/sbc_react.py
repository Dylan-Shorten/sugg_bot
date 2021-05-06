'''sugg bot react command'''

import sys
import getopt

import sb_utils

def read_reacts():
    '''read reacts from file'''
    return sb_utils.read_dict(sb_utils.DATA_PATH + 'reacts.txt')

def write_reacts(reacts):
    '''write reacts to file'''
    sb_utils.write_dict(reacts, sb_utils.DATA_PATH + 'reacts.txt')

def mode_react(args):
    '''react set mode'''
    if len(args) != 2:
        print('invalid argc')
        return
    reacts = read_reacts()
    name = args[0]
    value = args[1]
    reacts[name] = value
    write_reacts(reacts)
    print('set react', name, 'to', value)

def mode_list(args):
    '''react list mode'''
    if len(args) != 0:
        print('invalid argc')
        return
    reacts = read_reacts()
    if len(reacts) == 0:
        print('no reacts')
        return
    for i in reacts:
        print(i, '=', reacts[i])

def mode_delete(args):
    '''react delete mode'''
    if len(args) != 1:
        print('invalid argc')
        return
    reacts = read_reacts()
    name = args[0]
    if name in reacts:
        reacts.pop(name)
        write_reacts(reacts)
        print('deleted react', name)
        return
    print('react', name, 'does not exist')

def main():
    '''main func'''
    func = mode_react
    opts, args = getopt.getopt(sys.argv[1:], 'ld', ['list', 'delete'])
    for opt in opts:
        if opt[0] in ['-l', '--list']:
            func = mode_list
        elif opt[0] in ['-d', '--delete']:
            func = mode_delete
    func(args)

if __name__ == '__main__':
    main()
