'''sugg discord bot'''

import pathlib
import discord

import sb_commands
import sb_reacts
import sb_vars

def run(data_path, prefix):
    '''run the bot'''
    client = discord.Client()
    token = pathlib.Path(data_path + 'token.txt').read_text()
    token = token.replace('\n', '')
    variables = sb_vars.VarHandler(data_path + 'vars.txt')
    reactor = sb_reacts.Reactor(data_path + 'reacts.txt')
    parser = sb_commands.CommandParser(reactor, variables)

    # pylint: disable=unused-variable
    @client.event
    async def on_message(message):
        '''on message event'''
        if message.author == client.user:
            return
        string = variables.replace_vars(message.content)
        react = reactor.react(string)
        if react != '':
            await message.channel.send(react)
            return
        if string.startswith(prefix):
            trimmed = string[len(prefix):]
            result = parser.parse(trimmed)
            await message.channel.send(result)
    # pylint: enable=unused-variable

    client.run(token)

def main():
    '''main'''
    run('../data/', 'sb ')

if __name__ == '__main__':
    main()
