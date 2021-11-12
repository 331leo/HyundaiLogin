import asyncio, aiohttp
from os import getenv


async def get_token(code: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.post('https://oauth2.googleapis.com/token', data={"code":code, "client_id":getenv("GOOGLE_CLIENT_ID"), "client_secret":getenv("GOOGLE_CLIENT_SECRET"), "redirect_uri":getenv("GOOGLE_REDIRECT_URI"), "grant_type":"authorization_code"}) as resp:
            return await resp.json()

async def get_user_info(token: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.googleapis.com/userinfo/v2/me', headers={"Authorization":f"Bearer {token}"}) as resp:
            return await resp.json()