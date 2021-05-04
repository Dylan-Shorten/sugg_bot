'''sugg bot main'''

import datetime
import pathlib
import os

import discord

import sb_bot

def timestamp():
    zone = datetime.timezone(datetime.timedelta(hours=10))
    return datetime.datetime.now(tz=zone)

async def send_reply(message, response, client, log_file):
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

def main():
    '''main function'''
    data_path = '../data/'
    log_file = data_path + 'logs/' + str(timestamp()) + '.txt'
    bot = sb_bot.SuggBot('sb ', data_path)

    client = discord.Client()
    @client.event
    async def on_message(message):
        '''on message event'''
        if message.author == client.user:
            return
        result = bot.parse(message.content)
        if result != '':
            await send_reply(message, result, client, log_file)

    token = pathlib.Path(data_path + 'token.txt').read_text()
    token = token.replace('\n', '')
    client.run(token)

if __name__ == '__main__':
    main()
