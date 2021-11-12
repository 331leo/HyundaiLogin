from fastapi import APIRouter
from utils.google import get_token, get_user_info

callback_router = APIRouter()


@callback_router.get("/google")
async def callback_google(code: str):
    return await get_user_info((await get_token(code)).get("access_token"))
