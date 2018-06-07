from discord.ext import commands
import cogs.util.quotegrabs_functions as quotegrabs
from cogs.util.db import DBConn
from cogs.util.botpresets import CBot
import time

"""
Commands for quotegrabs.
Do you enjoy sleeping? I know I used to.
"""

class Quotegrabs:

    def __init__(self, bot:CBot):
        self.bot = bot

    # Grab a user msg. If no arg is supplied, grab most recent message that isn't the sender.
    @commands.command()
    async def grab(self, ctx, arg=None):
        messages = await ctx.channel.history(limit=512).flatten()
        if arg is None:
            userID = messages[1].author.id
            lastMessage = quotegrabs.sanitize_msg(messages[1].content)
        else:
            userID = quotegrabs.convert_ID(arg)
            lastMessage = quotegrabs.sanitize_msg(quotegrabs.get_last_msg(messages, userID).content)

        if lastMessage is None:
            await ctx.send("ERROR: ID doesn't exist / User hasn't sent a message in the last 512 messages.")
        else:
            g_id = ctx.message.author.id
            datetime = time.strftime('%Y-%m-%d %H:%M:%S')
            # We need the largest quote ID, so we query it. If it doesn't exist, set to 0. Else, set to largest + 1.
            async with DBConn() as db:
                id_res = await db("SELECT MAX(quote_id) AS quote_id FROM quotes;", None)
                if id_res[0]['quote_id'] is None:
                    q_id = 0
                else:
                    q_id = id_res[0]['quote_id'] + 1

                # Write data to database.
                await db("INSERT INTO quotes VALUES (%s, %s ,%s, %s, %s);", (userID, lastMessage, q_id, g_id, datetime))

            await ctx.send("Quote saved.")

    # Ungrab quote based on passed quote ID. Removes entry from database.
    @commands.command()
    async def ungrab(self, ctx, arg):
        quoteID = int(arg)
        async with DBConn() as db:
            await db("DELETE FROM quotes WHERE quote_id=%s;", (quoteID,))
        await ctx.send("Quote deleted.")

    # Quote user. Pulls most recent quote saved under user's ID.
    @commands.command()
    async def quote(self, ctx, arg):
        user_id = quotegrabs.convert_ID(arg)
        # We need the latest quote, so order by quote_id descending but only return top.
        async with DBConn() as db:
            quote = await db("SELECT * FROM quotes WHERE user_id=%s ORDER BY quote_id DESC LIMIT 1;", (user_id,))
        if quote is None:
            await ctx.send("User has no quotes / doesn't exist.")
        else:
            await quotegrabs.say_quote(ctx, self.bot, user_id, quote[0]['quote_text'])

    # Say quote based on passed quote ID.
    @commands.command()
    async def say(self, ctx, arg):
        async with DBConn() as db:
            quote = await db("SELECT * FROM quotes WHERE quote_id=%s;", (arg,))
            if quote is None:
                ctx.send("No such quote. Check your passed ID.")
            else:
                await quotegrabs.say_quote(ctx, self.bot, quote[0]['user_id'], quote[0]['quote_text'])

    # List quotes of passed user.
    @commands.command()
    async def list(self, ctx, arg):
        user_id = quotegrabs.convert_ID(arg)
        async with DBConn() as db:
            quote_list = await db("SELECT * FROM quotes WHERE user_id=%s ORDER BY quote_id DESC;", (user_id,))
            if quote_list is None:
                ctx.send("User has no quotes / doesn't exist.")
            else:
                list_send = "Quotes: "
                # Keep casting formatted string to list_send, and then send list_send
                for r in quote_list:
                    to_add = "({0}: {1}) ".format(r['quote_id'], r['quote_text'][0:70])
                    list_send += to_add
        await ctx.send(list_send)

    # Get a single random quote from the database..,
    @commands.command()
    async def random(self, ctx):
        async with DBConn() as db:
            quote = await db("SELECT * FROM quotes ORDER BY RAND() LIMIT 1;", None)
        if quote is None:
            await ctx.send("No quotes available.")
        else:
            await quotegrabs.say_quote(ctx, self.bot, quote[0]['user_id'], quote[0]['quote_text'])

def setup(bot:CBot):
    bot.add_cog(Quotegrabs(bot))

