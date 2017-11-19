import discord
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Bot
des = "Someone's gotta clean up those drugs."
pref = "!"
client = commands.Bot(description=des, command_prefix=pref)

@client.event
async def on_ready():
    print("Commander, your favourite cleaner bot is now online!")
    print("Name:", client.user.name)
    print("ID:", client.user.id)
    await client.change_presence(game=discord.Game(name="FDX_GOL"))

@client.event
async def on_message(message):
    print(message.author, "|", message.channel, ">",message.content)
    await client.process_commands(message)

@client.command(pass_context=True)
async def barney(ctx):
    await client.say("Barney is your god. All hail the midget dog.")

@client.command(pass_context=True)
async def sin(ctx):
    await client.say("None of you are free of sin.")

@client.command(pass_context=True)
async def cat(ctx):
    factFile = open("catfacts.txt", "r")
    facts = factFile.read().splitlines()
    factFile.close()
    await client.say(random.choice(facts))

client.run("key")

