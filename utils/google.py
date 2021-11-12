import asyncio, aiohttp
from os import getenv
from enum import Enum


class REQ_TYPE(str, Enum):
    GET = "GET"
    POST = "POST"


async def request(type: REQ_TYPE, **kwargs) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.request(type, **kwargs) as resp:
            return await resp.json()


async def get_token(code: str) -> dict:
    return await request(
        REQ_TYPE.POST,
        url="https://oauth2.googleapis.com/token",
        data={
            "code": code,
            "client_id": getenv("GOOGLE_CLIENT_ID"),
            "client_secret": getenv("GOOGLE_CLIENT_SECRET"),
            "redirect_uri": getenv("GOOGLE_REDIRECT_URI"),
            "grant_type": "authorization_code",
        },
    )


async def get_user_info(token: str) -> dict:
    return await request(
        REQ_TYPE.GET,
        url="https://www.googleapis.com/userinfo/v2/me",
        headers={"Authorization": f"Bearer {token}"},
    )
