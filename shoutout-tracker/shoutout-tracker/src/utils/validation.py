import discord


def sanitize_custom_message(message: str) -> str:
    """
    Sanitize the custom message to remove mentions and ensure it's safe.
    """
    # Remove mentions
    sanitized_message = message.replace("@everyone", "").replace("@here", "")
    sanitized_message = discord.utils.remove_markdown(sanitized_message)  # Remove Markdown formatting
    return sanitized_message.strip()  # Remove leading/trailing whitespace


def validate_custom_message(message: str, max_length: int = 200) -> bool:
    """
    Validate the custom message to ensure it meets criteria.
    """
    return 1 <= len(message) <= max_length and message.isprintable()