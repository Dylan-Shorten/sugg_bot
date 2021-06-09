"""sugg bot main"""

import sys
import os
import pathlib

import discord

import sb.commands
import sb.utils


def main(argv):
    """main function"""
    debug = "--offline" in argv
    if debug:
        run_offline()
    else:
        run_online()


def run_online():
    """run the bot online"""
    # setup bot
    client = discord.Client()
    # pylint: disable=unused-variable
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        result = sb.commands.parse_input(message.content)
        if result is not None:
            await message.reply(result)

    # pylint: enable=unused-variable
    # load discord token
    token_path = os.path.join(sb.utils.data_path(), "token.txt")
    token = pathlib.Path(token_path).read_text()
    if token.endswith("\n"):
        token = token[:-1]
    # run bot
    client.run(token)


def run_offline():
    """run the bot offline"""
    while True:
        string = input(":")
        if string == "q":
            break
        result = sb.commands.parse_input(string)
        if result is not None:
            print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
