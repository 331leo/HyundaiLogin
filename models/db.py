from enum import Enum

class RedisData(int, Enum):
    USER = 0
    OAUTHCODE = 1
    TOKENS = 2