import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

from events import initialize, handle_command_error, handle_message
from commands import player, recent, history, shoutout
from utils.encryption import CipherManager

# Load environment variables
load_dotenv()

# Constants
TOKEN = os.getenv('DISCORD_TOKEN') or ""
ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')

# Initialize encryption
CipherManager.initialize(ENCRYPTION_KEY)

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=commands.DefaultHelpCommand(no_category='Commands')
)

# Register events
@bot.event
async def on_ready():
    await initialize(bot)

@bot.event
async def on_command_error(ctx, error):
    await handle_command_error(bot, ctx, error)

@bot.event
async def on_message(message):
    await handle_message(bot, message)

# Register commands
bot.add_command(player.add_player)
bot.add_command(player.list_players)
bot.add_command(shoutout.shoutout_player)
bot.add_command(recent.last_shoutout)
bot.add_command(history.shoutout_history)

if __name__ == "__main__":
    bot.run(TOKEN)