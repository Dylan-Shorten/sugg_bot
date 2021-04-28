import sb_bot
import shlex

def main():
    sbot = sb_bot.SuggBot('sb ', '../data/')
    prefix = 'sb '
    while True:
        inp = input(':')
        if inp == 'exit':
            break
        out = sbot.parse(inp)
        if out != '':
            print(out)

if __name__ == '__main__':
    main()
