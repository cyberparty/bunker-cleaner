"""
rolecolour_functions.py
Functions to be used by the rolecolour commands.

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


def create_colour(raw_colour):
    try:
        return int(raw_colour, 16)
    except:
        return None


def get_role_name(user):
    return "col_" + str(user.id)


def get_role(server, user):
    role_name = get_role_name(user)
    for role in server.roles:
        if role.name == role_name:
            return role

    return None


async def create_role(server, user, role_col):
    role_name = get_role_name(user)
    role = await server.create_role(name=role_name, colour=discord.Colour(role_col))
    return role
