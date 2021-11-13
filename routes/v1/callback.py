from typing import Optional
from fastapi import APIRouter
from fastapi.params import Cookie
from models.user import User, parse_google_response
from utils.google import get_token, get_user_info

callback_router = APIRouter()


@callback_router.get("/google", response_model=User)
async def callback_google(code: str, hyundai_id_callback: Optional[str] = Cookie(None)):
    # print(hyundai_id_callback)
    user = User.parse_obj(
        parse_google_response(
            await get_user_info((await get_token(code)).get("access_token"))
        )
    )
    return user
