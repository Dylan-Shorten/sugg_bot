'''sugg discord bot'''

import pathlib
import discord

import sb_commands
import sb_reacts
import sb_vars

class SuggBot:
    client = None
    token = ''
    prefix = ''
    variables = None
    reactor = None
    parser = None

    def __init__(self, data_path, prefix):
        self.client = discord.Client()
        self.token = pathlib.Path(data_path + 'token.txt').read_text()
        self.token = self.token.replace('\n', '')
        self.prefix = prefix
        self.variables = sb_vars.VarHandler(data_path + 'vars.txt')
        self.reactor = sb_reacts.Reactor(data_path + 'reacts.txt')
        self.parser = sb_commands.CommandParser(self.reactor, self.variables)

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            string = self.variables.replace_vars(message.content)
            react = self.reactor.react(string)
            if not react == '':
                await message.channel.send(react)
                return
            if string.startswith(self.prefix):
                trimmed = string[len(self.prefix):]
                result = self.parser.parse(trimmed)
                await message.channel.send(result)

    def run(self):
        self.client.run(self.token)

def main():
    '''main'''
    bot = SuggBot('../data/', 'sb ')
    bot.run()

if __name__ == '__main__':
    main()
