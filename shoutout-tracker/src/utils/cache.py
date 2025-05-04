class ShoutoutDatesCache:
    _cache = {}

    @classmethod
    def initialize(cls, dates_data: dict):
        cls._cache = dates_data

    @classmethod
    def get(cls, user_id: str):
        return cls._cache.get(user_id)

    @classmethod
    def set(cls, user_id: str, history: list):
        cls._cache[user_id] = history

    @classmethod
    def all(cls):
        return cls._cache

    @classmethod
    def refresh(cls, dates_data: dict):
        cls._cache = dates_data


class TeamCache:
    _cache = {}

    @classmethod
    def initialize(cls, team_data: dict):
        cls._cache = team_data

    @classmethod
    def get(cls, user_id: str):
        return cls._cache.get(user_id)

    @classmethod
    def set(cls, user_id: str, username: str):
        cls._cache[user_id] = username

    @classmethod
    def all(cls):
        return cls._cache

    @classmethod
    def refresh(cls, team_data: dict):
        cls._cache = team_data