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
botId = 379970263917264926

def get_db():
    return db.JsonDB("db.json")

def convert_ID(userMention):
    try:
        return int(userMention.strip("!@<>"))
    except Exception:
        return None

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

def create_user_in_db(jsondb, userid):
    jsondb["users"].append({"id": userid, "quotes": [], "count": 0})

def insert_msg_into_db(jsondb, message):
    auth_id = message.author.id
    text = message.content
    for user in jsondb["users"]:
        if user["id"] == auth_id:
            user["quotes"].insert(0, {"text": text, "id": jsondb["next_id"]})
            user["count"] += 1
            break
    else:
        create_user_in_db(jsondb, auth_id)

    jsondb["count"] += 1
    jsondb["next_id"] += 1





# def grab_quote(jsonDb, channelMsgs, userID):
#     for message in channelMsgs:
#         if str(message.author.mention) == userID:
#             msgQuote = str(message.content).replace('"', '/"')
#             for user in jsonDb["users"]:
#                 if user["id"] == int(userID.strip('<>@!')):
#                     user["quotes"].insert(0, {"text":msgQuote, "id":jsonDb["next_id"]})
#                     user["count"] += 1
#                     print("MSG saved into existing user.")
#                     return jsonDb
#             jsonDb["users"].append({"id":int(userID.strip('<>@!')), "quotes":[], "count":1})
#             jsonDb["users"][-1]["quotes"].insert(0, {"text":msgQuote, "id":jsonDb["next_id"]})
#             print("MSG saved into new user")
#             return jsonDb
#     return None

def get_quote_by_id(jsonDb, quoteID):
    for user in jsonDb["users"]:
        for q in user["quotes"]:
            if q["id"] == int(quoteID):
                return q["text"]
    return "No such quote"

def get_quote_by_user(jsonDb, userID):
    for i in jsonDb["users"]:
        if i["id"] == int(userID.strip('<>@!')):
            userQuote = i["quotes"][0]["text"].replace('/"', '"')
            return 'They said: "'+userQuote+'"'
    return "No such user."

def list_quotes(jsonDb, userID):
    listString = ""
    for user in jsonDb["users"]:
        if user["id"] == int(userID.strip('<>@!')):
            for quote in user["quotes"]:
                listString += "("+str(quote["id"])+": "+quote["text"]+")"
            return "Their quotes: "+listString
    return "No such user."

def random_quote(jsonDb):
    randomQuoteIter = randint(0, jsonDb["count"])
    idPos = -1
    while randomQuoteIter >= 0:
        idPos += 1
        randomQuoteIter -= jsonDb["users"][idPos]["count"]
    randQuote = jsonDb["users"][idPos]["quotes"][randomQuoteIter]["text"]
    mentionId = "<@"+str(jsonDb["users"][idPos]["id"])+">"
    return mentionId + ": " + randQuote

@bot.event
async def on_ready():
    print("Commander, your favourite cleaner bot is now online!")
    print("Name:", bot.user.name)
    print("ID:", bot.user.id)
    await bot.change_presence(game=discord.Game(name="FDX_GOL"))

@bot.event
async def on_message(message):
    print(message.author, "|", message.channel, ">", message.content)
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
async def grab(ctx, arg):
    userID = convert_ID(arg)
    messages = await ctx.channel.history(limit=512).flatten()
    lastMessage = sanitize_msg(get_last_msg(messages,userID).content)
    
    if lastMessage is None:
        await ctx.send("ERROR: ID doesn't exist / User hasn't sent a message in the last 512 messages.")
    else:
        db=get_db()
        db.add_quote(lastMessage,userID)
        await ctx.send("Quote saved.")

@bot.command()
async def quote(ctx, arg):
    db=get_db()
    userID = convert_ID(arg)
    (user,quote) = db.get_quote_user_index(userID)
    if quote is None:
        await ctx.send("No quote found")
    else:
        quote_text = quote["text"]
        await ctx.send(quote_text)

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
    await ctx.send(db.get_random_quote())

@bot.command()
async def say(ctx, arg):
    db = get_db()
    (user,quote) = db.get_quote_ID(int(arg))
    if quote is None:
        await ctx.send("No quote found")
    else:
        await ctx.send(quote["text"])

if __name__ == "__main__":

	keyfile = open("key.txt", "r")
	key = keyfile.readline()
	keyfile.close()
	bot.run(key)
