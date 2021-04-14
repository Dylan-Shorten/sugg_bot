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

COMMANDS = {
        'ping': Command('', [], command_ping)
        }
