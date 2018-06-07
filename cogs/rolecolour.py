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
