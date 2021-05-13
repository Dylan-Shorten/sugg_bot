'''sugg bot'''

import datetime
import pathlib
import os
import shlex
import subprocess
import sys

import discord

import sb_utils

def timestamp():
    '''get a timestamp'''
    zone = datetime.timezone(datetime.timedelta(hours=10))
    return datetime.datetime.now(tz=zone)

async def send_reply(message, response, client, log_file):
    '''send a message to discord and the log'''
    await message.reply(response)
    log_str = ''
    log_str += str(timestamp()) + '\n'
    log_str += str(message.channel.guild) + ' #' + str(message.channel) + '\n'
    log_str += str(message.author) + ': ' + message.content + '\n'
    log_str += str(client.user) + ': ' + response + '\n'
    print(log_str)
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, 'a') as file:
        file.write(log_str + '\n')

def replace_vars(string):
    '''replace vars in a string'''
    variables = sb_utils.read_dict(sb_utils.DATA_PATH + 'vars.txt')
    for _ in range(0, 100):
        replaced = False
        for name in variables:
            var_str = '<' + name + '>'
            result = string.replace(var_str, variables[name])
            if result != string:
                string = result
                replaced = True
        if not replaced:
            break
    return string

def get_react(string):
    '''get a react if it exists'''
    reacts = sb_utils.read_dict(sb_utils.DATA_PATH + 'reacts.txt')
    if string in reacts:
        return reacts[string]
    return ''

def run_command(string):
    '''run a bot command'''
    words = shlex.split(string)
    name = words[0]
    args = words[1:]
    script = 'sbc_' + name + '.py'
    if not os.path.isfile(script):
        return name + ' is not a command'
    command = [
        sys.executable,
        script
        ]
    command.extend(args)
    result = subprocess.run(command, stdout=subprocess.PIPE, check=False)
    return result.stdout.decode('utf-8')[:-1]

def parse_message(string, prefix):
    '''parse an input message'''
    string = replace_vars(string)
    react = get_react(string)
    if react != '':
        return react
    if string.startswith(prefix):
        return run_command(string[len(prefix):])
    return ''

def main():
    '''main func'''
    log_file = sb_utils.LOGS_PATH + str(timestamp()) + '.txt'
    client = discord.Client()
    # pylint: disable=unused-variable
    @client.event
    async def on_message(message):
        '''on message event'''
        if message.author == client.user:
            return
        result = parse_message(message.content, 'sb ')
        if result != '':
            await send_reply(message, result, client, log_file)
    # pylint: enable=unused-variable
    token = pathlib.Path(sb_utils.DATA_PATH + 'token.txt').read_text()
    token = token.replace('\n', '')
    client.run(token)

if __name__ == '__main__':
    main()
