import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import datetime
import time
import os

import config.bot as bot
import config.messages as messages


class Tags(commands.Cog):
    def __init__(self, lytex):
        self.lytex = lytex

    @commands.command()
    async def tags(self, ctx, lang, *, arg):
        if ctx.author.bot:
            await ctx.send('You are a Bot!?!')
            pass
        else:
            if lang == 'html':
                if arg == 'grundgerüst' or arg == '1':
                    await ctx.send('__**HTML Tag 1 | Grundgerüst**__\n```html\n<!DOCTYPE html>\n<html lang="de">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\n<!-- Title and Logo -->\n<link rel="icon" type="image/png" sizes="600x600" href="logo.png">\n<title>Test Website</title>\n\n<!-- Stylesheet -->\n<link rel="stylesheet" href="stuff/css/main.css">\n\n<!-- Javascriptt -->\n<script src="stuff/js/main.js"></script>\n</head>\n<body>\n\n</body>\n</html>\n```')
                elif arg == 'headline' or arg == '2':
                    await ctx.send('__**HTML Tag 2 | Headlines**__\n\nHeadline = h1 - h6\n```html\n<h1>Headline 1</h1>\n<h2>Headline 2</h2>>\n<h3>Headline 3</h3>>\n<h4>Headline 4</h4>>\n<h5>Headline 5</h5>>\n<h6>Headline 6</h6>\n```')
                    await ctx.send('https://cdn.discordapp.com/attachments/938868094565228544/944949466966925332/headline.PNG')
            elif lang == 'python' or lang == 'py':
                if arg == 'import' or arg == '1':
                    await ctx.send('__**Python Tag 1 | Import**__\n```py\nimport some_package\nimport discord\n```')



def setup(lytex):
    lytex.add_cog(Tags(lytex))