"""
main.py
Main python file. Bot is executed from this script.

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
from cogs.util.botpresets import CBot

import sys, traceback


client = discord.Client()
bot = CBot()


cogextensions = ['cogs.quotegrabs',
                 'cogs.rolecolour',
                 'cogs.facts',
                 'cogs.misc']

@bot.event
async def on_ready():
    print("Starting up.")
    print("Name:", bot.user.name)
    print("ID:", bot.user.id)

if __name__ == "__main__":
    for extension in cogextensions:
        try:
            bot.load_extension(extension)
            print("Loaded extension " + extension + " successfully.")
        except Exception as e:
            print("Failed to load extension " + extension + ".", file=sys.stderr)
            traceback.print_exc()

    bot.run_with_token()
