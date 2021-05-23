'''sugg bot main'''

import sys
import getopt
import discord

import sb

def main():
    opts, args = getopt.getopt(sys.argv[1:], '', ['offline'])
    offline = False
    for opt in opts:
        if opt[0] == '--offline':
            offline = True
    if offline:
        main_offline()
    else:
        main_online()

def main_online():
    client = discord.Client()
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        result = sb.parse_input_str(message.content)
        if result != '':
            await message.reply(result)
    token = sb.read_file(sb.DATA_PATH + 'token.txt')
    client.run(token)

def main_offline():
    while True:
        string = input(':')
        if string == 'q':
            break
        result = sb.parse_input_str(string)
        if result != '':
            print(result)

if __name__ == '__main__':
    main()
