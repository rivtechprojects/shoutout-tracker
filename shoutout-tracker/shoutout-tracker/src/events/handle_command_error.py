from discord.ext import commands


async def handle_command_error(bot, ctx, error):
    if isinstance(error, commands.CommandNotFound):
        # Get the list of available commands
        available_commands = ", ".join([f"`{bot.command_prefix}{cmd}`" for cmd in bot.commands])
        await ctx.send(
            f"Command not found. Here is a list of available commands:\n{available_commands}"
        )
    else:
        # If it's another type of error, re-raise it to let the default handler deal with it
        raise error