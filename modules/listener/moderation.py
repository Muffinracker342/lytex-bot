import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
import sqlite3
import time
import os

import config.bot as bot
import config.messages as messages

class Moderation(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command(aliases =["slowmode"])
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def cooldown(self, ctx, seconds: int=None):
        if ctx.author.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            await ctx.channel.edit(slowmode_delay=seconds)

            embed=discord.Embed(title='Moderation | Cooldown',
                                description=f'- {ctx.author.mention} set the Cooldown for {ctx.channel.mention} to {seconds} seconds.',
                                color=0xccbb11 )
            embed.set_author(name=messages.TEAM_NAME)
            await ctx.send(embed=embed)
            await channel.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def lock(self, ctx, arg):
        if ctx.author.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            if arg == 'on':
                await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
                embed=discord.Embed(title='Moderation | Lockdown',
                                description=f'- {ctx.author.mention} enabled the Lockdown for {ctx.channel.mention}',
                                color=discord.Color.green())
                embed.set_author(name=messages.TEAM_NAME)
                await ctx.send(embed=embed)
                await channel.send(embed=embed)
            
            elif arg == 'off':
                await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
                embed=discord.Embed(title='Moderation | Lockdown',
                                description=f'- {ctx.author.mention} disabled the Lockdown for {ctx.channel.mention}',
                                color=discord.Color.red())
                embed.set_author(name=messages.TEAM_NAME)
                await ctx.send(embed=embed)
                await channel.send(embed=embed)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.guild_only()
    async def clear(self, ctx, amount=1):
        if ctx.author.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            await ctx.channel.purge(limit=amount)

            embed=discord.Embed(title='Moderation | Clear',
                            description=f'{ctx.author.mention} deleted {amount} Messages from {ctx.channel.mention}.',
                            color=0x440077)
            embed.set_author(name=messages.TEAM_NAME)
            await ctx.send(embed=embed)
            await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.bot:
            pass
        else:
            channel = self.lytex.get_channel(944951186442833950)

            embed=discord.Embed(title='Moderation | Message',
                                description=f'- {after.author.mention} edited a Message in {after.channel.mention}',
                                color=0x118844)
            embed.set_author(name=messages.TEAM_NAME)
            embed.add_field(name='before', value=f'{before.content}', inline=False)
            embed.add_field(name='after', value=f'{after.content}', inline=False)
            await channel.send(embed=embed)
    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            empty_array = []
            modmail_channel = self.lytex.get_channel(945712138939420824)

            if str(message.channel.type) == "private":
                if message.attachments != empty_array:
                    files = message.attachments
                    await modmail_channel.send(f'{message.author.mention}')
                    for file in files:
                        await modmail_channel.send(file.url)
                else:
                    try:
                        embed=discord.Embed(title='Question', description=f'{message.content}', color=discord.Color.red())
                        embed.set_author(name=f'from: {message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
                        await message.author.send(embed=embed)
                        await modmail_channel.send(embed=embed)
                    except:
                        print('I can not send the message to the modmail channel!')
                        await message.author.send('I can not send the message to the modmail channel!')

            if message.channel == modmail_channel and message.content.startswith("answer"):
                member_object = message.mentions[0]
                if message.attachments != empty_array:
                    files = message.attachments
                    await member_object.send(f'{message.author.mention}')
                    for file in files:
                        await member_object.send(file.url)
                else:
                    try:
                        index = message.content.index(" ")
                        string = message.content
                        mod_message = string[index:]
                        embed=discord.Embed(title='answer', description=f'{mod_message}', color=discord.Color.green())
                        embed.set_author(name=f'from: {message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
                        await modmail_channel.send(embed=embed)
                        await member_object.send(embed=embed)
                        await message.delete()
                    except:
                        await modmail_channel.send('I can not send there the message!')



def setup(lytex):
    lytex.add_cog(Moderation(lytex))