import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
import time
import os

import config.bot as bot
import config.messages as messages

class Moderation(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex
    
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        if member.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            embed=discord.Embed(title='Moderation | Ban',
                                description=f'- {member.mention} were banned!',
                                color=discord.Color.red())
            embed.set_author(name=messages.TEAM_NAME)
            await channel.send(embed=embed)
            try:
                await member.send(f'You are banned from {guild.name}!')
            except:
                await channel.send(f"Ban-Message couldn't be send to {member}!")
                pass
    

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        if member.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            embed=discord.Embed(title='Moderation | Unban',
                                description=f'- {member.mention} were unbanned!',
                                color=discord.Color.green())
            embed.set_author(name=messages.TEAM_NAME)
            await channel.send(embed=embed)
            try:
                await member.send(f'You have been unbanned from {guild.name}!\nhttps://discord.gg/4FxVkSBmjR')
            except:
                await channel.send(f"Unban-Message couldn't be send to {member}!")
                pass



def setup(lytex):
    lytex.add_cog(Moderation(lytex))