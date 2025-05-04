from discord.ext import commands
from utils.cache import TeamCache
from utils.resolve_user import resolve_user
from utils.constants import HELP_MESSAGES
from utils.validation import sanitize_custom_message, validate_custom_message
from history import update_shoutout_history


@commands.command(name='shoutout', help=HELP_MESSAGES["shoutout"])
@commands.cooldown(1, 10, commands.BucketType.user)
async def shoutout_player(ctx, *, player_name_and_message: str = None):
    if not player_name_and_message or " " not in player_name_and_message:
        await ctx.send(
            "Please provide a player name and a custom message. Usage: `!shoutout <player_name> <custom_message>`"
        )
        return

    # Split the input into player name and custom message
    player_name, custom_message = player_name_and_message.split(" ", 1)

    # Sanitize and validate the custom message
    custom_message = sanitize_custom_message(custom_message)
    if not validate_custom_message(custom_message):
        await ctx.send("Messages can be max 200 characters.")
        return
    
    if custom_message.lower().startswith("for "):
        custom_message = custom_message[4:]

    # Resolve the user
    user = resolve_user(ctx, player_name)
    if not user:
        await ctx.send(
            f"User `{player_name}` not found."
        )
        return

    # Check if the user is in the team cache
    if not TeamCache.get(str(user.id)):
        await ctx.send(f"{user.display_name} is not in the team. Use `!addplayer @user` to add them.")
        return

    # Update the user's shoutout history
    update_shoutout_history(str(user.id), custom_message)

    # Respond with the custom message
    await ctx.send(f"Shoutout to {user.mention} for {custom_message}!")