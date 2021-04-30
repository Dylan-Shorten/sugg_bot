'''sugg bot main'''

import pathlib

import discord

import sb_bot

def main():
    '''main function'''
    data_path = '../data/'
    bot = sb_bot.SuggBot('sb ', data_path)

    client = discord.Client()
    @client.event
    async def on_message(message):
        '''on message event'''
        if message.author == client.user:
            return
        result = bot.parse(message.content)
        if result != '':
            await message.reply(result)

    token = pathlib.Path(data_path + 'token.txt').read_text()
    token = token.replace('\n', '')
    client.run(token)

if __name__ == '__main__':
    main()
