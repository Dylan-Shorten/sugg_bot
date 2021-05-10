'''sugg bot uptime command'''

import sys
import subprocess

def main():
    if len(sys.argv) != 1:
        print('invalid argc')
        return
    result = subprocess.run(['uptime', '-p'], stdout=subprocess.PIPE, check=False)
    print(result.stdout.decode('utf-8')[:-1])

if __name__ == '__main__':
    main()
