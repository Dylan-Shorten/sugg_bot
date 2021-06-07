'''help command'''

import os

def get_commands():
    '''get a list of bot command python scripts'''
    file_path = os.path.realpath(__file__)
    path = os.path.dirname(file_path)
    prefix = 'sbc_'
    ext = '.py'
    scripts = []
    for i in os.listdir(path):
        if i.startswith(prefix) and i.endswith(ext):
            name = i[len(prefix):-len(ext)]
            scripts.append(name)
    return scripts

def main():
    '''main function'''
    for i in get_commands():
        print(i)

if __name__ == '__main__':
    main()
