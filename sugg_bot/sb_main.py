'''sugg discord bot'''

import pathlib
import discord

import sb_parser
import sb_vars

def load_token():
    '''load discord token'''
    token = pathlib.Path('../data/token.txt').read_text()
    return token.replace('\n', '')

def main():
    '''main'''
    client = discord.Client()
    @client.event
    # pylint: disable=unused-variable
    async def on_message(message):
        if message.author == client.user:
            return
        await sb_parser.parse_input(message.content, message.channel)
    sb_vars.load_vars()
    token = load_token()
    client.run(token)

if __name__ == '__main__':
    main()
