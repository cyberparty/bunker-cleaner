import discord
import asyncio
from cogs.util.botpresets import CBot

import sys, traceback


des = "Someone's gotta clean up those drugs."
pref = "!"
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
