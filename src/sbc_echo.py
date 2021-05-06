import sys

def main():
    if len(sys.argv) == 1:
        print('invalid argc')
        return
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == '__main__':
    main()
