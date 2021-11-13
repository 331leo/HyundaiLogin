from redis import Redis
from os import getenv

user_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=0)
oauth_code_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=1)
token_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=2)

