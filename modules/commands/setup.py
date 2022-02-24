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


class Setup(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clickrole(self, ctx, mode, channel: discord.TextChannel, message_id, role: discord.Role, emoji):
        if ctx.author.bot:
            pass
        else:
            if mode == 'setup':
                db = sqlite3.connect('db.sqlite3')
                cursor = db.cursor()
                cursor.execute(f"SELECT channel_id FROM clickrole_setup WHERE guild_id = {ctx.guild.id}")

                try:
                    message = await channel.fetch_message(int(message_id))

                    sql = ("INSERT INTO clickrole_setup(guild_id, channel_id, message_id, role_id, emoji, author_id) VALUES(?,?,?,?,?,?)")
                    val = (ctx.guild.id, channel.id, message_id, role.id, emoji, ctx.author.id)
                    cursor.execute(sql, val)

                    db.commit()
                    cursor.close()
                    db.close()

                    await message.add_reaction(emoji)

                    embed=discord.Embed(title='Clickrole-Setup',
                                        description=f'\nClickrole was successfully created!\n\nChannel: {channel.mention}\nRole: {role.mention}\nMessage: https://discord.com/channels/{ctx.guild.id}/{channel.id}/{message.id}\n',
                                        color=discord.Color.green())
                    embed.set_author(name=messages.TEAM_NAME)
                    embed.set_footer(text=f'Requested by: {ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title='',
                    description='Error: Error when saving the data!',
                    color=discord.Color.red())
                    pass



def setup(lytex):
    lytex.add_cog(Setup(lytex))