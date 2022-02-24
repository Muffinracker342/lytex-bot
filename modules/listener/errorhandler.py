import discord
from discord.ext import commands
import asyncio
import datetime
import time
import os

from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import CommandNotFound
from discord.ext.commands import BadArgument
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands import MissingPermissions
from discord.ext.commands import MissingRole
from discord.ext.commands import BotMissingPermissions
from discord.ext.commands import NoPrivateMessage
from discord.ext.commands import MemberNotFound
from discord.ext.commands import PrivateMessageOnly
from discord.ext.commands import PrivateMessageOnly

import config.bot as bot
import config.messages as messages


class Errorhandler(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            embed=discord.Embed(title='Error', description='Command not found!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title='Error', description='Missing argument!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        
        elif isinstance(error, commands.BadArgument):
            embed=discord.Embed(title='Error', description='Bad argument!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.NoPrivateMessage):
            embed=discord.Embed(title='Error', description='No PN command!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingPermissions):
            embed=discord.Embed(title='Error', description='Missing permission!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MissingRole):
            embed=discord.Embed(title='Error', description='Missing role!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.BotMissingPermissions):
            embed=discord.Embed(title='Error', description='Missing Bot permission!', color=0xff675c)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.MemberNotFound):
            embed=discord.Embed(title='Error', description='Member not found!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

        elif isinstance(error, commands.PrivateMessageOnly):
            embed=discord.Embed(title='Error', description='No guild command!', color=0xff675c)
            embed.set_footer(text='Use !help', icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)



def setup(lytex):
    lytex.add_cog(Errorhandler(lytex))