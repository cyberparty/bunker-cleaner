"""
facts.py
Commands for regurgitating facts.
Caution: Facts may not be true.

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

from discord.ext import commands
from random import choice
import cogs.util.facts_functions as facts
from cogs.util.botpresets import CBot

class Facts:

    def __init__(self, bot:CBot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        await ctx.send(choice(facts.fact_spew("catfacts.txt", None)))

    @commands.command()
    async def shark(self, ctx):
        await ctx.send(choice(facts.fact_spew("sharkfacts.txt", None)))

    @commands.command()
    async def herken(self, ctx):
        await ctx.send(choice(facts.fact_spew("hwkquotes.txt", 'UTF-8')))


def setup(bot:CBot):
    bot.add_cog(Facts(bot))
