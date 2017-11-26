import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
des = "Someone's gotta clean up those drugs."
pref = "!"
client = discord.Client()
bot = commands.Bot(description=des, command_prefix=pref)

@bot.event
async def on_ready():
    print("Commander, your favourite cleaner bot is now online!")
    print("Name:", bot.user.name)
    print("ID:", bot.user.id)
    await bot.change_presence(game=discord.Game(name="FDX_GOL"))
    #await bot.get_channel(187319694363983873).send("Yeah yeah, I'm here, let me get my mop.")

@bot.event
async def on_message(message):
    print(message.author, "|", message.channel, ">",message.content)
    await bot.process_commands(message)

@bot.command()
async def barney(ctx):
    await ctx.send("Barney is your god. All hail the midget dog.")

@bot.command()
async def sin(ctx):
    await ctx.send("None of you are free of sin.")

@bot.command()
async def cat(ctx):
    factFile = open("catfacts.txt", "r")
    facts = factFile.read().splitlines()
    factFile.close()
    await ctx.send(random.choice(facts))

@bot.command()
async def grab(ctx, arg):
    messages = await ctx.channel.history(limit=500).flatten()
    print(arg)
    for i in messages:
        if str(i.author.mention) == arg:
            await ctx.send("Message found! "+str(i.content))
            break


bot.run("key-goes-here")

