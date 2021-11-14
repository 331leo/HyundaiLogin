import hashlib
from datetime import datetime
from os import getenv

from dotenv import load_dotenv
from etc import md5hash
from redis import Redis

load_dotenv()

client_credentials_db = Redis(
    host=getenv("REDIS_HOST"), port=getenv("REDIS_PORT"), db=2
)


def md5hash(string: str):
    string = str(string)
    return hashlib.md5(string.encode("utf-8")).hexdigest()


def register():
    print("--HyundaiID oAuth Client Secret Register Tool--")
    id = input("Please enter the Client ID: ")
    secret = md5hash(int(md5hash(id), 16) + int(datetime.now().timestamp()))
    client_credentials_db.set(id, secret)
    print("User registered with Client Secret: ", secret)


if __name__ == "__main__":
    register()
