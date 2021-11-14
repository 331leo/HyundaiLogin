from os import getenv

from utils.etc import REQ_TYPE, request


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
