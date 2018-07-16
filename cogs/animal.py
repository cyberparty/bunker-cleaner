from discord.ext import commands
from discord import File
from aiohttp import ClientSession
from cogs.util.botpresets import CBot
from io import BytesIO

class Animal:
    def __init__(self, bot:CBot):
        self.bot = bot
        self.session = ClientSession(loop=bot.loop)

    def __unload(self):
        self.session.close()

    @commands.command()
    async def dog(self, ctx):
        async with self.session.get("https://api.thedogapi.co.uk/v2/dog.php") as d:
            json = await d.json()
        url = json["data"][0]["url"]
        async with self.session.get(url) as i:
            data = await i.read()
        await ctx.send(file=File(fp=BytesIO(data), filename="dog.png"))


def setup(bot:CBot):
    bot.add_cog(Animal(bot))
