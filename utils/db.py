from os import getenv

from redis import Redis

user_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=0)
oauth_code_db = Redis(host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=1)
client_credentials_db = Redis(
    host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=2
)
