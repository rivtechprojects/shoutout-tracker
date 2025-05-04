from utils.cache import TeamCache, ShoutoutDatesCache
from utils.file_io import load_json
from utils.encryption import CipherManager
from utils.constants import TEAM_FILE, DATES_FILE


def initialize_team_cache():
    team = load_json(TEAM_FILE)
    decrypted_team = {CipherManager.decrypt(key): value for key, value in team.items()}
    TeamCache.initialize(decrypted_team)
    print("Team cache initialized.")


def initialize_shoutout_dates_cache():
    dates = load_json(DATES_FILE)
    decrypted_dates = {CipherManager.decrypt(key): value for key, value in dates.items()}
    ShoutoutDatesCache.initialize(decrypted_dates)
    print("Shoutout dates cache initialized.")


async def initialize(bot):
    initialize_team_cache()
    initialize_shoutout_dates_cache()
    print(f"{bot.user.name} is ready.")