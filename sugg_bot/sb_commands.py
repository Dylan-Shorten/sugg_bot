'''commands'''

import collections

Command = collections.namedtuple('Command', ['opts', 'long_opts', 'func'])

# pylint: disable=unused-argument
async def command_ping(opts, args, channel):
    '''command ping'''
    if len(args) > 0:
        await channel.send('ping takes 0 args')
        return
    await channel.send('pong')

async def command_echo(opts, args, channel):
    '''command echo'''
    if len(args) < 1:
        await channel.send('echo takes 1 or more args')
        return
    string = ''
    for arg in args:
        string += arg + ' '
    string = string[:-1]
    for (opt, arg) in opts:
        if opt == '-l':
            string = string.lower()
        elif opt == '-u':
            string = string.upper()
    await channel.send(string)

COMMANDS = {
        'ping': Command('', [], command_ping),
        'echo': Command('lu', [], command_echo)
        }
