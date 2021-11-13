from redis import Redis
from os import getenv
from models.db import RedisData

user_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=RedisData.USER)
oauth_code_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=RedisData.OAUTHCODE)
token_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=RedisData.TOKENS)
