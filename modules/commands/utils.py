import discord
from discord.ext import commands
import asyncio
import datetime
import psutil
import time
import os

import config.bot as bot
import config.messages as messages


class Utils(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command()
    async def github(self, ctx):
        embed=discord.Embed(title='',
        description='\n\n»  [__**Github**__](https://github.com/immanuel-development)\n\n\n',
        color=discord.Color.light_grey())
        embed.set_author(name=messages.TEAM_NAME)
        embed.set_footer(text=f'Requested by: {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=['author'])
    async def copyright(self, ctx):
        embed=discord.Embed(title='', description='__**LYTEX Development ©**__', color=discord.Color.blue())
        embed.set_footer(text='the Bot was programmed by Immanuel.')
        await ctx.send(embed=embed)


    @commands.command()
    async def motto(self, ctx):
        embed=discord.Embed(title='', description='\n**LYTEX Development - learn programming**', color=discord.Color.green())
        await ctx.send(embed=embed)


    @commands.command()
    async def info(self, ctx):
        if ctx.author.bot:
            pass
        else:
            embed=discord.Embed(title='', description='', color=0x0cc9c9)
            embed.set_author(name=messages.TEAM_NAME)
            embed.add_field(name='created:', value='<t:1643808634:R>',
            inline=False)
            embed.add_field(name='founder:', value=f'<@510708544425951233>',
            inline=False)
            embed.add_field(name='location:', value='🇩🇪 Germany',
            inline=False)
            embed.set_thumbnail(url=messages.LOGO_URL)
            msg=await ctx.send(embed=embed)
            await msg.add_reactio(messages.EMOJI_NAME)


    @commands.command()
    async def vserver(self, ctx):
        if ctx.author.bot:
            pass
        else:
            embed=discord.Embed(title='', description='', color=0x0cc9c9)
            embed.set_author(name=messages.TEAM_NAME)
            embed.add_field(name='Ping:', value=f'{round(self.lytex.latency * 100)}ms',
            inline=False)
            embed.add_field(name='CPU usage:', value=f'{psutil.cpu_percent()} %',
            inline=False)
            embed.add_field(name='RAM usage:', value=f'{psutil.virtual_memory()[2]} %',
            inline=False)
            embed.add_field(name='Disk total in GB:', value=int(psutil.disk_usage('/').total // (2**30)),
            inline=False)
            embed.add_field(name='Disk used in GB:', value=psutil.disk_usage('/').used // (2**30),
            inline=False)
            embed.add_field(name='Disk free in GB:', value=psutil.disk_usage('/').free // (2**30),
            inline=False)
            embed.set_footer(text='vServer from our Partner Prohosting24!')
            await ctx.send(embed=embed)
    

    @commands.command(aliases=['imprint', 'impressum', 'dsvgo'])
    async def legal(self, ctx):
        if ctx.author.bot:
            pass
        else:
            embed=discord.Embed(title='',
            description='\n\n\n»  [__**Impressum**__](https://immanuelm.de/legal#imprint)\n\n»  [__**DSVGO**__](https://immanuelm.de/legal#gdpr)\n\n»  **Kontact:**\n__**contact@immanuelm.de**__',
            color=discord.Color.blurple())
            embed.set_author(name=f'{messages.TEAM_NAME} ©')
            await ctx.send(embed=embed)



def setup(lytex):
    lytex.add_cog(Utils(lytex))