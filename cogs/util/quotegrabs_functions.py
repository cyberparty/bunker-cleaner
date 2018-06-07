
def get_user_nick(bot, userID):
    userID = int(userID)
    if bot.get_user(userID) is not None:
        return bot.get_user(userID).name
    else:
        return convert_to_mention(userID)

async def say_quote(ctx, bot, user_id, quote_text):
    try:
        await ctx.send(get_user_nick(bot, user_id) + " -> " + quote_text)
    except Exception:
        await ctx.send("Quote not found.")

def convert_ID(userMention):
    try:
        return int(userMention.strip("!@<>"))
    except Exception:
        return None

def convert_to_mention(userID):
    try:
        userID = int(userID)
    except Exception:
        return None
    return "<@" + str(userID) + ">"

def get_last_msg(messages, userid):
    for message in messages:
        if message.author.id == userid:
            return message
    return None

def sanitize_msg(message):
    return message.replace('"', '/"')

