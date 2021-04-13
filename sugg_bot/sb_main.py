import pathlib
import shlex
import discord

def load_token():
    token = pathlib.Path('../data/token.txt').read_text()
    return token.replace('\n', '')

def main():
    client = discord.Client()
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        words = shlex.split(message.content)
        if words[0] == 'sb':
            if words[1] == 'ping':
                await message.channel.send('pong')
    token = load_token()
    client.run(token)

if __name__ == '__main__':
    main()
