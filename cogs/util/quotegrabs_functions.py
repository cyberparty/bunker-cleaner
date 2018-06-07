"""
quotegrabs_functions.py
Functions to be used by the quotegrabs commands.

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

