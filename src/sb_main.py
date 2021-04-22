'''sugg discord bot'''
#
#import pathlib
#import discord
#
#import sb_commands
#import sb_reacts
#import sb_vars
#
#def run(data_path, prefix):
#    '''run the bot'''
#    client = discord.Client()
#    token = pathlib.Path(data_path + 'token.txt').read_text()
#    token = token.replace('\n', '')
#    variables = sb_vars.VarHandler(data_path + 'vars.txt')
#    reactor = sb_reacts.Reactor(data_path + 'reacts.txt')
#    parser = sb_commands.CommandParser(reactor, variables)
#
#    # pylint: disable=unused-variable
#    @client.event
#    async def on_message(message):
#        '''on message event'''
#        if message.author == client.user:
#            return
#        string = variables.replace_vars(message.content)
#        react = reactor.react(string)
#        if react != '':
#            await message.channel.send(react)
#            return
#        if string.startswith(prefix):
#            trimmed = string[len(prefix):]
#            result = parser.parse(trimmed)
#            await message.channel.send(result)
#    # pylint: enable=unused-variable
#
#    client.run(token)
#
#def main():
#    '''main'''
#    run('../data/', 'sb ')
#
#if __name__ == '__main__':
#    main()

import discord

import sb_bot

def load_file(path):
    '''load an entire file into a string'''
    contents = ''
    with open(path) as f:
        for line in f:
            contents += line
    if contents.endswith('\n')
        return contents[:-1]
    return contents

def main():
    data_path = '../data/'
    # create sb
    s_bot = sb_bot.SuggBot()
    # create discord bot
    d_bot = discord.Client()
    @client.event
    def on_message(message):
        if message.author == d_bot.user:
            return
        response = s_bot.process_input(message.content)
        if response != '':
            await message.reply(reponse, mention_author=False)
    # load token
    token_path = data_path + 'token.txt'
    token = load_file(token_path)
    # run discord bot
    d_bot.run(token)

if __name__ == '__main__':
    main()
