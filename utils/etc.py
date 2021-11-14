import hashlib
from enum import Enum

import aiohttp


class REQ_TYPE(str, Enum):
    GET = "GET"
    POST = "POST"

async def request(type: REQ_TYPE, **kwargs) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.request(type, **kwargs) as resp:
            return await resp.json()

def md5hash(string: str):
    string = str(string)
    return hashlib.md5(string.encode('utf-8')).hexdigest()