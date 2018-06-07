"""
rolecolour.py
Commands for rolecolour.

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
import cogs.util.rolecolour_functions as rolecolour
from cogs.util.botpresets import CBot

class Rolecolour:

    def __init__(self, bot:CBot):
        self.bot = bot

    @commands.command()
    async def col(self, ctx, msg=None):
        if msg is not None:

            col = rolecolour.create_colour(msg)

            if col is not None:

                server = ctx.message.guild
                user = ctx.message.author

                role = rolecolour.get_role(server, user)

                if role is not None:
                    await role.edit(colour=discord.Colour(col))
                else:
                    role = await rolecolour.create_role(server, user, col)
                    await user.add_roles(role)


def setup(bot:CBot):
    bot.add_cog(Rolecolour(bot))
