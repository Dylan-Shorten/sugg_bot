'''input parser'''

import shlex

async def parse_input(message, channel):
    '''parses an input string'''
    if message.startswith('sb '):
        try:
            words = shlex.split(message)
        except ValueError:
            # echo error
            pass
        else:
            if len(words) == 2 and words[1] == 'ping':
                await channel.send('pong')
