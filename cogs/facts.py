from discord.ext import commands
from random import choice
import cogs.util.facts_functions as facts
from cogs.util.botpresets import CBot

"""
Commands for regurgitating facts.
Caution: Facts may not be true.
"""

class Facts:

    def __init__(self, bot):
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
