'''input parser'''

import shlex
import getopt

import sb_commands

async def parse_input(message, channel):
    '''parses an input string'''
    if not message.startswith('sb '):
        return
    try:
        words = shlex.split(message)
    except ValueError as error:
        await channel.send(error)
        return
    if not words[1] in sb_commands.COMMANDS:
        await channel.send(words[1] + ' is not a command')
        return
    com = sb_commands.COMMANDS[words[1]]
    try:
        (opts, args) = getopt.getopt(words[2:], com.opts, com.long_opts)
    except getopt.GetoptError as error:
        await channel.send(error)
        return
    await com.func(opts, args, channel)
