"""
misc.py
Commands that don't fit into any category go here.

Copyright (C) 2018 Joseph Cole <jc@cyberparty.me>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import discord
from discord.ext import commands
from cogs.util.botpresets import CBot


class Misc:

    def __init__(self, bot:CBot):
        self.bot = bot

    @commands.command()
    async def barney(self, ctx):
        await ctx.send("Barney is your god. All hail the midget dog.")

    @commands.command()
    async def sin(self, ctx):
        await ctx.send("None of you are free of sin.")

    @commands.command()
    async def ready(self, ctx):
        img = discord.File(fp="cogs/util/img/ready.jpg")
        await ctx.send(file=img)

def setup(bot:CBot):
    bot.add_cog(Misc(bot))
