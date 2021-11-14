import datetime
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from utils import generate_oauth_link
from utils.etc import REQ_TYPE, md5hash, request

from os import getenv
from base64 import b64encode

def get_basic_auth_token(username, password):
    return "Basic "+b64encode(f'{username}:{password}'.encode()).decode()

test_router = APIRouter()


@test_router.get("/callback", include_in_schema=False)
async def test(code: str):
    token =(await request(REQ_TYPE.POST, url=f"http://localhost:{getenv('PORT')}/v1/oauth2/token", data={"code": code}, headers={"Authorization": get_basic_auth_token(getenv('TEST_CLIENT_ID'),getenv('TEST_CLIENT_SECRET'))})).get("access_token")
    return (await request(REQ_TYPE.GET, url=f"http://localhost:{getenv('PORT')}/v1/users/@me", headers={"Authorization": f"Bearer {token}"}))