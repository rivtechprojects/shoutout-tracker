import discord


def resolve_user(ctx, player_name: str) -> discord.Member:
    """
    Resolve a user by their global name or display name (case-insensitive).
    Returns the discord.Member object if found, otherwise None.
    """
    player_name_lower = player_name.lower()
    for member in ctx.guild.members:
        if (member.global_name and member.global_name.lower() == player_name_lower) or \
           (member.display_name.lower() == player_name_lower):
            return member
    return None