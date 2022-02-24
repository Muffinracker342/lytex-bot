import discord
from discord.ext import commands
import asyncio
import datetime
import sqlite3
import time
import os

import config.bot as bot
import config.messages as messages


class Reactionhandler(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            pass
        else:
            guild = self.lytex.get_guild(938143761060495370)

            db = sqlite3.connect('db.sqlite3')
            cursor = db.cursor()
            cursor.execute(f"SELECT channel_id FROM clickrole_setup WHERE guild_id = {guild.id}")
            result = cursor.fetchone()

            if result is not None:
                cursor.execute(f"SELECT channel_id FROM clickrole_setup WHERE guild_id = {guild.id}")
                channel_id = cursor.fetchone()

                cursor.execute(f"SELECT message_id FROM clickrole_setup WHERE guild_id = {guild.id}")
                message_id = cursor.fetchone()

                cursor.execute(f"SELECT role_id FROM clickrole_setup WHERE guild_id = {guild.id}")
                role_id = cursor.fetchone()

                cursor.execute(f"SELECT emoji FROM clickrole_setup WHERE guild_id = {guild.id}")
                emoji = cursor.fetchone()

                if payload.channel_id == int(channel_id[0]):
                    print(1)
                    if payload.message_id == int(message_id[0]):
                        print(2)
                        if str(payload.emoji) == (emoji[0]):
                            print(3)
                            channel = self.lytex.get_channel(id=int(channel_id[0]))
                            role = discord.utils.get(guild.roles, id=int(role_id[0]))

                            message = await channel.fetch_message(int(message_id[0]))
                            await message.remove_reaction(payload.emoji, payload.member)

                            if role in payload.member.roles:
                                await payload.member.remove_roles(role)
                                embed=discord.Embed(title='Clickrole',
                                    description=f'{payload.member.mention} | Role: {role.mention} was removed!',
                                    color=discord.Color.red())
                                embed.set_footer(text='This Message will be deleted in 3 seconds...')
                                await channel.send(embed=embed, delete_after=3)
                                db.commit()
                                cursor.close()
                                db.close()
                                pass
                            else:
                                await payload.member.add_roles(role)
                                embed=discord.Embed(title='Clickrole',
                                    description=f'{payload.member.mention} | Role: {role.mention} was added!',
                                    color=discord.Color.green())
                                embed.set_footer(text='This Message will be deleted in 3 seconds...')
                                await channel.send(embed=embed, delete_after=3)
                                cursor.close()
                                db.close()
                                pass
            elif result is None:
                pass



def setup(lytex):
    lytex.add_cog(Reactionhandler(lytex))