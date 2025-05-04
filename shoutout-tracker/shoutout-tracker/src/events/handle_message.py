from utils.constants import ALLOWED_CHANNEL_NAME

async def handle_message(bot, message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is in the allowed channel
    if message.channel.name != ALLOWED_CHANNEL_NAME:
        return  # Ignore messages in other channels

    # Process commands if the message is in the allowed channel
    await bot.process_commands(message)