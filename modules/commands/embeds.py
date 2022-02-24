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


class Embeds(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex
    
    @commands.command(aliaes=['author', 'credits'])
    async def credit(self, ctx):
        embed=discord.Embed(title='', 
                            desciption='\n**The Bot was programmed by Immanuel\n\n━━━━━━━━━━━━━━━━━━\n☰ [Github](https://github.com/ximmanuel)\n☰ [Twitter](https://twitter.com/heisserhundtv)\n☰ [Twitch](https://www.twitch.tv/ximmanuel4)\n☰ [Instagram](https://www.instagram.com/ximmanuelm/)', 
                            color=discord.Color.green())
        embed.set_footer(text='©️ Immanuel | All right reserved')
        message = await ctx.send(embed=embed)
        await message.add_reaction('©️')
        

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clickrole_embed(self, ctx, arg):
        if arg == 'lang':
            embed=discord.Embed(title='Programming languages',
            description='\n\nHTML: <:html:939515990537023508>\n\nCSS: <:css:939515990746759218>\n\nJavascript: <:javascript:939515991212310578>\n\nPython: <:python:938153116585566248>\n\nKotlin: <:kotlin:939515990256009328>\n\nDart: <:dart:939516810166947910>\n\nPhp: <:php:939515991623340082>\n\nTypescript: <:typescript:939515990801281074>\n\nRuby: <:ruby:939516810733187123>\n\nJava: <:java:939515990801285170>\n\nGolang: <:go:939515990889361418>\n\nLua: <:lua:939515990608334898>                                                          \n\n\n\n',
            color=discord.Color.blurple())
            embed.set_author(name=messages.TEAM_NAME)
            await ctx.send(embed=embed)



def setup(lytex):
    lytex.add_cog(Embeds(lytex))