import discord
from discord.ext import commands
from cogs.util.botpresets import CBot

"""
Commands that don't fit into any category go here.
"""

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
