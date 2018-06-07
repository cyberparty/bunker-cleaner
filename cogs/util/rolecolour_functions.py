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
