'''sugg bot main'''

import sys
import os
import pathlib

import discord

import sb.commands

def src_path():
    '''get the folder that contains this script'''
    filepath = os.path.realpath(__file__)
    return os.path.dirname(filepath)

def script_path():
    '''get the folder that contains command scripts'''
    return os.path.join(src_path(), 'sb')

def load_token():
    '''read the token file'''
    path = os.path.join(src_path(), '..', 'data', 'token.txt')
    token = pathlib.Path(path).read_text()
    if token.endswith('\n'):
        return token[:-1]
    return token

def main(argv):
    '''main function'''
    debug = '--offline' in argv
    if debug:
        run_offline()
    else:
        run_online()

def run_online():
    '''run the bot online'''
    sp = script_path()
    client = discord.Client()
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        result = sb.commands.parse_input(message.content, sp)
        if result != None:
            await message.reply(result)
    client.run(load_token())

def run_offline():
    '''run the bot offline'''
    sp = script_path()
    while True:
        string = input(':')
        if string == 'q':
            break
        result = sb.commands.parse_input(string, sp)
        if result != None:
            print(result)

if __name__ == '__main__':
    main(sys.argv[1:])
