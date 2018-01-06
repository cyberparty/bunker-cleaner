import discord
import asyncio
from random import randint, choice
import db
from discord.ext import commands
from discord.ext.commands import Bot
des = "Someone's gotta clean up those drugs."
pref = "!"
client = discord.Client()
bot = commands.Bot(description=des, command_prefix=pref)
#botId = 379970263917264926

def create_colour(raw_colour):
    try:
        return int(raw_colour,16)
    except:
        return None

def get_role_name(user):
    return "col_"+str(user.id)
    
def get_role(server,user):
    role_name=get_role_name(user)
    
    for role in server.roles:
        if role.name==role_name:
            return role

    return None

async def create_role(server,user,role_col):
    role_name=get_role_name(user)
    role=await server.create_role(name=role_name,colour=discord.Colour(role_col))
    await role.edit(position=2)
    return role

async def say_quote(ctx,user_quote):
    try:
        (userID,quote)=user_quote
        quote_text=quote["text"]
        await ctx.send(get_user_nick(userID)+" -> "+quote_text)
    except Exception:
        await ctx.send("Quote not found.")
            

def get_db():
    return db.JsonDB("db.json")

def convert_ID(userMention):
    try:
        return int(userMention.strip("!@<>"))
    except Exception:
        return None

def convert_to_mention(userID):
    try:
        userID=int(userID)
    except Exception:
        return None
    return "<@"+str(userID)+">"

def get_user_nick(userID):
    userID=int(userID)
    if bot.get_user(userID) is not None:
        return bot.get_user(userID).name
    else:
        return convert_to_mention(userID)

def fact_spew(fileName, fileEncoding):
    factFile = open(str(fileName), "r", encoding=fileEncoding)
    facts = factFile.read().splitlines()
    factFile.close()
    return facts

def get_last_msg(messages, userid):
    for message in messages:
        if message.author.id == userid:
            return message
    return None

def sanitize_msg(message):
    return message.replace('"', '/"')

@bot.event
async def on_ready():
    print("Commander, your favourite cleaner bot is now online!")
    print("Name:", bot.user.name)
    print("ID:", bot.user.id)
    await bot.change_presence(game=discord.Game(name="FDX_GOL"))

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
    await ctx.send(choice(fact_spew("catfacts.txt", None)))

@bot.command()
async def shark(ctx):
    await ctx.send(choice(fact_spew("sharkfacts.txt", None)))

@bot.command()
async def herken(ctx):
    await ctx.send(choice(fact_spew("hwkquotes.txt", 'UTF-8')))

@bot.command()
async def grab(ctx, arg=None):
    messages = await ctx.channel.history(limit=512).flatten()
    if arg is None:
        userID = messages[0].author.id
        lastMessage = sanitize_msg(messages[0].content)
    else:
        userID = convert_ID(arg)
        lastMessage = sanitize_msg(get_last_msg(messages,userID).content)
    
    if lastMessage is None:
        await ctx.send("ERROR: ID doesn't exist / User hasn't sent a message in the last 512 messages.")
    else:
        db=get_db()
        db.add_quote(lastMessage,userID)
        await ctx.send("Quote saved.")

@bot.command()
async def ungrab(ctx, arg):
    db=get_db()
    quoteID = int(arg)
    (user,quote)=db.remove_quote_ID(quoteID)

    if quote is None:
        await ctx.send("Quote not found.")
    else:
        await ctx.send("Quote deleted.")

@bot.command()
async def quote(ctx, arg):
    db=get_db()
    userID = convert_ID(arg)
    quote = db.get_quote_user_index(userID)
    await say_quote(ctx, quote)

@bot.command()
async def list(ctx, arg):
    db=get_db()
    userID = convert_ID(arg)
    quotes = db.get_user(userID)

    if quotes is None:
        await ctx.send("No quotes found")
    else:

        msg = ""
        for quote in quotes:
            msg += "({0} | {1})".format(quote["ID"],quote["text"])
        await ctx.send(msg)

@bot.command()
async def random(ctx):
    db = get_db()
    quote=db.get_random_quote()
    await say_quote(ctx, quote)

@bot.command()
async def say(ctx, arg):
    db = get_db()
    quote = db.get_quote_ID(int(arg))
    await say_quote(ctx, quote)

@bot.command()
async def col(ctx,msg=None):
    if msg is not None:

        col=create_colour(msg)

        if col is not None:

            server=ctx.message.guild
            user=ctx.message.author

            role=get_role(server,user)

            if role is not None:
                await role.delete()

            role=await create_role(server,user,col)
            await user.add_roles(role)

if __name__ == "__main__":
    keyfile = open("key.txt", "r")
    key = keyfile.readline()
    keyfile.close()
    bot.run("Mzc5OTcwMjYzOTE3MjY0OTI2.DTG8Hg.hXsXyoiKexwVjoNs3NQbe1ItDZM")
