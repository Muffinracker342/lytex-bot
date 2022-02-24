
'''
    The Bot was programmed by Immanuel
    in the name of LYTEX Development!

    used:
    - Python
    - SQlite

'''

import discord
from discord.ext import commands
import asyncio
import random
import sqlite3
import os

import config.bot as bot
import config.messages as messages

intents = discord.Intents.default()
intents.members=True
intents.presences=True

lytex = commands.Bot(command_prefix=bot.PREFIX,
                    intents=discord.Intents.all(),
                    help_command=None)

class Main():
    @lytex.event
    async def on_ready():
        try:
            print(f'\n-----------------------\n') 
            print(f'Name: {lytex.user.name}#{lytex.user.discriminator}')
            print(f'ID: {lytex.user.id}')
            print(f'Ping: {round(lytex.latency * 100)}ms')
            print(f'\n-----------------------\n')
            if bot.STATUS is True:
                await lytex.change_presence(activity=discord.Game(bot.STATUS_TEXT), status=discord.Status.online)
            else:
                pass
        except:
            print('Error: Failed to start the Bot!')
            pass

    def open_database():
        try:
            db = sqlite3.connect('db.sqlite3')
            cursor = db.cursor()
            #cursor.execute('''CREATE TABLE IF NOT EXISTS team(guild_id TEXT, member_id TEXT, role TEXT)''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS clickrole_setup(guild_id TEXT, channel_id TEXT, message_id TEXT, role_id TEXT, emoji TEXT, author_id TEXT)''')
        except:
            print("Error: the SQlite database couldn't be created with the tables!")
            pass
        try:
            db.commit()
            cursor.close()
            db.close()
        except:
            pass

    def load_bot():
        try:
            for filename in os.listdir('./modules'):
                if filename.endswith('.py'):
                    lytex.load_extension(f'modules.{filename[:-3]}')
                    print('- Module "{}" loaded'.format(filename[:-3]))
                
            for filename in os.listdir('./modules/listener'):
                if filename.endswith('.py'):
                    lytex.load_extension(f'modules.listener.{filename[:-3]}')
                    print('- Module "{}" loaded'.format(filename[:-3]))
                
            for filename in os.listdir('./modules/commands'):
                if filename.endswith('.py'):
                    lytex.load_extension(f'modules.commands.{filename[:-3]}')
                    print('- Module "{}" loaded'.format(filename[:-3]))
        except:
            print('Error: Failed to load the Modules!')
            pass

        # run bot with token
        lytex.run(bot.BOT_TOKEN)

    # ------------------------- #

    # start functions
    open_database()
    load_bot()
    