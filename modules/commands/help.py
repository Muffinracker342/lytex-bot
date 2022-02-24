import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
import time
import os

import config.bot as bot
import config.messages as messages


class Setup(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command(aliases=['hilfe', 'commands'])
    async def help(self, ctx, page=None):
        if ctx.author.bot:
            pass
        else:
            if page == None:
                await ctx.send(messages.MAINTEANCE)
                pass



def setup(lytex):
    lytex.add_cog(Setup(lytex))