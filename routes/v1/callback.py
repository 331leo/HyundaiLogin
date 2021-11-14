import json as jsonlib
from os import getenv
from typing import Optional

from fastapi import APIRouter
from fastapi.params import Cookie
from starlette.responses import JSONResponse, RedirectResponse

from models.user import User, parse_google_response
from utils.auth import gen_oauth_code
from utils.db import user_db
from utils.etc import md5hash
from utils.google import get_token, get_user_info

callback_router = APIRouter()


@callback_router.get("/google", response_class=RedirectResponse)
async def callback_google(code: str, hyundai_id_callback: Optional[str] = Cookie(None)):
    # print(hyundai_id_callback)
    try:
        user = User.parse_obj(
            parse_google_response(
                await get_user_info((await get_token(code)).get("access_token"))
            )
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            {
                "code": "PARSE_ERROR",
                "message": f"Failed Parsing user informaing from Google. Please retry and contact to: {getenv('CONTACT')}",
            },
            status_code=500,
        )
    user_db.set(md5hash(user.id), jsonlib.dumps(user.dict(), ensure_ascii=False))
    return RedirectResponse(
        hyundai_id_callback + f"?code={gen_oauth_code(user.id).get('code')}"
    )
