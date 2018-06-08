"""
admin.py
Administrator commands.

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
from cogs.util.botpresets import CBot


class Admin:

    def __init__(self, bot):
        self.bot = bot

    # Check that all commands within this cog are run by a user with the 'administrator' perm.
    async def __local_check(self, ctx):
        is_admin = ctx.author.permissions_in(ctx.channel).administrator
        if is_admin:
            return True
        return False

    # Run an SQL command to the bot's database. Return output where applicable.
    @commands.command()
    async def sql(self, ctx, arg:str=None):
        if arg is None:
            await ctx.send('Usage: !db "[SQL]"')
        else:
            async with self.bot.db() as db:
                try:
                    r = await db(arg)
                    if r is None:
                        await ctx.send("SQL OK: Empty response")
                    else:
                        await ctx.send(r[0:3000])
                except Exception as e:
                    await ctx.send(e)

    # Reload config. Report if it succeeds.
    @commands.command()
    async def reload_cfg(self, ctx):
        r = self.bot.reload_cfg()
        if r:
            await ctx.send("Config reloaded.")
        else:
            await ctx.send("Unable to reload config.")


def setup(bot:CBot):
    bot.add_cog(Admin(bot))

