from dis import dis
import discord
from discord.ext import commands
import datetime
import asyncio
import psutil
import random
import time
import os

import config.bot as bot
import config.messages as messages


class Random(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command()
    async def speak(self, ctx, *, arg):
        if ctx.author.bot:
            pass
        else:
            await ctx.message.delete()
            await ctx.send(arg)
    

    @commands.command()
    async def print(self, ctx, *, arg):
        if ctx.author.bot:
            pass
        else:
            await ctx.message.delete()
            await ctx.send(f'```{arg}```')


    @commands.command(aliases=['password'])
    async def passwort(self, ctx):
        if ctx.author.bot:
            pass
        else:
            await ctx.message.delete()
            zahlen = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
            grossb = ("Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M")
            kleinb = ("q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m")
            #sonderz = ("^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",", ";", ":", "-", "_", "{", "}", "[", "]", "~")
            wort = ""
            zusammensetzung = (zahlen, grossb, kleinb, grossb, kleinb, zahlen, grossb, kleinb, grossb, kleinb, zahlen, grossb)
            for teil in zusammensetzung:
                zeichen = random.choice(teil)
                wort += zeichen
            try:
                await ctx.author.send(f'||{wort}||')
                await ctx.send(f'{ctx.author}, your generated password was sent to you via DM!', delete_after=5)
            except:
                await ctx.send("I couldn't send your password to you via DM!")
                pass


    @commands.command(aliases=['jaodernein', 'yesorno', 'orakel'])
    async def oracle(self, ctx, *, question):
        if ctx.author.bot:
            pass
        else:
            list = ['Ja', 'Nein', 'Vielleicht', 'Uhhhm']
            answer = random.choice(list)

            embed=discord.Embed(title='Oracle', description='', color=0xedff26)
            embed.add_field(name='question:', value=question, inline=False)
            embed.add_field(name='answer:', value=answer, inline=False)
            await ctx.send(embed=embed)
    

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        if ctx.author.bot:
            pass
        else:
            if member == ctx.author:
                member = ctx.author    
            await ctx.send(member.avatar_url)
    
    
    @commands.command()
    async def hello(self, ctx):
        if ctx.author.bot:
            pass
        else:
            await ctx.send('**Hello!**')



def setup(lytex):
    lytex.add_cog(Random(lytex))