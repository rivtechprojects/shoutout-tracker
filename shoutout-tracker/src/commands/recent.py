from datetime import datetime
from discord.ext import commands
from utils.resolve_user import resolve_user
from utils.constants import HELP_MESSAGES
from utils.cache import ShoutoutDatesCache, TeamCache


@commands.command(name='recent', help=HELP_MESSAGES["recent"])
async def last_shoutout(ctx, *, player_name: str = None):
    if not player_name:
        await ctx.send("Please provide a player name. Usage: `!recent <player_name>`")
        return

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

    # Retrieve the user's history from the cache
    user_id = str(user.id)
    player_data = ShoutoutDatesCache.get(user_id)
    if not player_data:
        await ctx.send(f"No shoutout history found for {user.display_name}.")
        return

    # Get the most recent event
    most_recent_event = player_data[-1]
    response = format_recent_shoutout(user.display_name, most_recent_event)
    await ctx.send(response)


def format_recent_shoutout(display_name: str, event: dict) -> str:
    """
    Format the response for the most recent shoutout.
    """
    custom_message = event["message"]
    days = calculate_days_since(event["date"])
    day_text = "day" if days == 1 else "days"
    return f"It has been **{days} {day_text}** since {display_name} received a shoutout for {custom_message}."


def calculate_days_since(date_str: str) -> int:
    start_date = datetime.strptime(date_str, '%Y-%m-%d')
    now = datetime.now()
    return (now - start_date).days