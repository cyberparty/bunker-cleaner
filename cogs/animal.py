"""
animal.py
Animal-related commands.

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
