from datetime import datetime
from discord.ext import commands
from utils.cache import TeamCache, ShoutoutDatesCache
from utils.resolve_user import resolve_user
from utils.constants import DATES_FILE, HELP_MESSAGES 
from utils.file_io import save_json
from utils.encryption import CipherManager


@commands.command(name='history', help=HELP_MESSAGES["history"])
async def shoutout_history(ctx, *, player_name: str = None):
    if not player_name:
        await ctx.send("Please provide a player name. Usage: `!history <player_name>`")
        return

    # Resolve the user
    user = resolve_user(ctx, player_name)
    if not user:
        await ctx.send(
            f"Member `{player_name}` not found in the server. Please check the spelling or try mentioning the user."
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

    # Format and send the history
    history_text = format_history(user.display_name, player_data)
    await ctx.send(history_text)
    

def update_shoutout_history(user_id: str, custom_message: str):
    """
    Update the shoutout history for a user and save it to the cache and file.
    """
    user_history = ShoutoutDatesCache.get(user_id) or []
    user_history.append({
        "message": custom_message,
        "date": datetime.now().strftime('%Y-%m-%d')
    })

    ShoutoutDatesCache.set(user_id, user_history)
    encrypted_dates = {
    CipherManager.encrypt(key): value for key, value in ShoutoutDatesCache.all().items()
    }
    save_json(DATES_FILE, encrypted_dates)


def format_history(display_name: str, history: list) -> str:
    history_messages = [
        f"- {event['date']}: {event['message']}" for event in history
    ]
    history_text = "\n".join(history_messages)
    return f"{display_name} received a shoutout for:\n{history_text}"
