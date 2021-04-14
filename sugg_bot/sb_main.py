'''sugg discord bot'''

import pathlib
import shlex
import discord

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
        if message.content.startswith('sb '):
            try:
                words = shlex.split(message.content)
                if words[1] == 'ping':
                    await message.channel.send('pong')
            except ValueError:
                pass
    token = load_token()
    client.run(token)

if __name__ == '__main__':
    main()
