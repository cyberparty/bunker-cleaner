import discord
import asyncio
from random import randint, choice
import json
from discord.ext import commands
from discord.ext.commands import Bot
des = "Someone's gotta clean up those drugs."
pref = "!"
client = discord.Client()
bot = commands.Bot(description=des, command_prefix=pref)
botId = 379970263917264926

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

def factspew(fileName, fileEncoding):
    factFile = open(str(fileName), "r", encoding=fileEncoding)
    facts = factFile.read().splitlines()
    factFile.close()
    return facts

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
    await ctx.send(choice(factspew("catfacts.txt", None)))

@bot.command()
async def shark(ctx):
    await ctx.send(choice(factspew("sharkfacts.txt", None)))

@bot.command()
async def herken(ctx):
    await ctx.send(choice(factspew("hwkquotes.txt", 'UTF-8')))

@bot.command()
async def grab(ctx, arg):
    msgFound = False
    messages = await ctx.channel.history(limit=500).flatten()
    if int(arg.strip('<>@!')) != botId and int(arg.strip('<>@!')) != ctx.author.id:
        for i in messages:
            if str(i.author.mention) == arg:
                msgFound = True
                msgQuote = str(i.content).replace('"', '/"')
                await ctx.send('Quote saved: "'+msgQuote+'"')
                with open("db.json", "r+") as quotesjson:
                    quotedb = json.load(quotesjson)
                idFound = False
                for i in quotedb["users"]:
                    if i["id"] == int(arg.strip('<>@!')):
                        idFound = True
                        i["quotes"].insert(0, {"text":msgQuote, "id":quotedb["next_id"]})
                        i["count"] += 1
                        print("MSG saved into existing user.")
                        break
                if not idFound:
                    quotedb["users"].append({"id":int(arg.strip('<>@!')), "quotes":[], "count":1})
                    quotedb["users"][-1]["quotes"].insert(0, {"text":msgQuote, "id":quotedb["next_id"]})
                    print("MSG saved into new user")
                quotedb["count"] += 1
                quotedb["next_id"] += 1
                with open("db.json", "w") as quotesjson:
                    json.dump(quotedb, quotesjson)
                break
        if not msgFound:
            await ctx.send("Error: User not found / User's message not within 500 messages.")
    else:
        await ctx.send("No, fuck you.")

@bot.command()
async def quote(ctx, arg):
    quoteFound = False
    with open("db.json") as quotesjson:
        quotedb = json.load(quotesjson)
        try:
            for i in quotedb["users"]:
                if i["id"] == int(arg.strip('<>@!')):
                    userQuote = i["quotes"][0]["text"].replace('/"', '"')
                    quoteFound = True  # todo: just check if userQuote is set. stop being a skrub.
                    break
            if quoteFound:
                await ctx.send('They said: "'+userQuote+'"')
            else:
                await ctx.send("ERROR: No such user.")
        except:
            ctx.send("ERROR: Sparky fucked up. Go talk to him and tell him the command you entered to get this message.")
            #json.dump(quotedb, quotesjson)

@bot.command()
async def list(ctx, arg):
    with open("db.json") as quotesjson:
        quotedb = json.load(quotesjson)
        for user in quotedb["users"]:
            if user["id"] == int(arg.strip('<>@!')):  # todo: just add this to variable.
                listString = "Their quotes: "
                for quote in user["quotes"]:
                    listString += "("+str(quote["id"])+": "+quote["text"]+")"
                break
        await ctx.send(listString)

@bot.command()
async def context(ctx):
    await ctx.send("Probably something to do with cocks.")

@bot.command()
async def random(ctx):
    with open("db.json") as quotesjson:
        quotedb = json.load(quotesjson)
        randomQuoteIter = randint(0, quotedb["count"])
        idPos = -1
        while randomQuoteIter >= 0:
            idPos += 1
            randomQuoteIter -= quotedb["users"][idPos]["count"]
        randQuote = quotedb["users"][idPos]["quotes"][randomQuoteIter]["text"]
        mentionId = "<@"+str(quotedb["users"][idPos]["id"])+">"
        await ctx.send(mentionId+': "'+randQuote+'"')


@bot.command()
async def ping(ctx):
    await ctx.send("pong")

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


keyfile = open("key.txt", "r")
key = keyfile.readline()
keyfile.close()
bot.run(key)
