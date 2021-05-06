import sys
import getopt

import sb_utils

def read_reacts():
    return sb_utils.read_dict(sb_utils.data_path + 'reacts.txt')

def write_reacts(reacts):
    sb_utils.write_dict(reacts, sb_utils.data_path + 'reacts.txt')

def mode_react(args):
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
    func = mode_react
    opts, args = getopt.getopt(sys.argv[1:], 'ld', ['list', 'delete'])
    for opt, arg in opts:
        if opt in ['-l', '--list']:
            func = mode_list
        elif opt in ['-d', '--delete']:
            func = mode_delete
    func(args)

if __name__ == '__main__':
    main()
