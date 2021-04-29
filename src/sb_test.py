'''offline bot tester'''

import sb_bot

def main():
    '''main function'''
    sbot = sb_bot.SuggBot('sb ', '../data/')
    while True:
        inp = input(':')
        if inp == 'exit':
            break
        out = sbot.parse(inp)
        if out != '':
            print(out)

if __name__ == '__main__':
    main()
