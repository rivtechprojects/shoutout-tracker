from discord.ext import commands
from utils.cache import TeamCache
from utils.file_io import load_json, save_json
from utils.resolve_user import resolve_user
from utils.encryption import CipherManager
from utils.constants import TEAM_FILE, HELP_MESSAGES

@commands.command(name='addplayer', help=HELP_MESSAGES["addplayer"])
async def add_player(ctx, *, player_name: str = None):
    if not player_name:
        await ctx.send("Please provide a player name or mention a user. Usage: `!addplayer @user`\n")
        return

    # Resolve the user
    user = resolve_user(ctx, player_name)
    if not user:
        await ctx.send(f"User `{player_name}` not found.")
        return

    # Encrypt the user ID before storing
    encrypted_user_id = CipherManager.encrypt(str(user.id))

    # Check if the user is already in the team
    if TeamCache.get(str(user.id)):
        await ctx.send(f"{user.display_name} is already in the team.")
        return

    # Add the user to the team
    add_user_to_team(str(user.id), encrypted_user_id, user.name)

    # Respond with success
    await ctx.send(f"{user.display_name} has been added to the team!")


def add_user_to_team(user_id: str, encrypted_user_id: str, username: str):
    """
    Add a user to the team and save it to the cache and file.
    """
    team = load_json(TEAM_FILE)
    team[encrypted_user_id] = username
    save_json(TEAM_FILE, team)
    TeamCache.set(user_id, username)


@commands.command(name='players', help=HELP_MESSAGES["players"])
async def list_players(ctx):
    if not TeamCache.all():
        await ctx.send("The team is currently empty. Use `!addplayer @user` to add players.")
        return

    members = []
    for user_id, username in TeamCache.all().items():
        member = ctx.guild.get_member(int(user_id))
        if member:
            members.append(member.display_name)
        else:
            members.append(f"Unknown User ({username})")

    team_list = ", ".join(members)
    await ctx.send(f"Current team: {team_list}")