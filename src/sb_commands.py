'''sugg bot commands'''

import collections

import sb_vars
import sb_reacts

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

async def command_set(opts, args, channel):
    '''command set'''
    if not len(args) == 2:
        await channel.send('set takes 2 args')
        return
    sb_vars.variables[args[0]] = args[1]
    sb_vars.save_vars()
    await channel.send('set ' + args[0] + ' to ' + args[1])

async def command_listvars(opts, args, channel):
    '''command listvars'''
    if len(args) > 0:
        await channel.send('listvars takes 0 args')
        return
    if len(sb_vars.variables) == 0:
        await channel.send('no vars')
        return
    string = ''
    for i in sb_vars.variables:
        string += i + ' = ' + sb_vars.variables[i] + '\n'
    string = string[:-1]
    await channel.send(string)

async def command_react(opts, args, channel):
    '''command react'''
    if not len(args) == 2:
        await channel.send('react takes 2 args')
        return
    sb_reacts.reacts[args[0]] = args[1]
    sb_reacts.save_reacts()
    await channel.send('set react ' + args[0] + ' to ' + args[1])

async def command_listreacts(opts, args, channel):
    '''command listreacts'''
    if len(args) > 0:
        await channel.send('listreacts takes 0 args')
        return
    if len(sb_reacts.reacts) == 0:
        await channel.send('no reacts')
        return
    string = ''
    for i in sb_reacts.reacts:
        string += i + ' = ' + sb_reacts.reacts[i] + '\n'
    string = string[:-1]
    await channel.send(string)

COMMANDS = {
        'ping': Command('', [], command_ping),
        'echo': Command('lu', [], command_echo),
        'set': Command('', [], command_set),
        'listvars': Command('', [], command_listvars),
        'react': Command('', [], command_react),
        'listreacts': Command('', [], command_listreacts)
        }
