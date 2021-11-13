from typing import Optional
from fastapi import APIRouter
from fastapi.params import Cookie
from starlette.responses import JSONResponse, RedirectResponse
from models.user import User, parse_google_response
from utils.google import get_token, get_user_info
from utils.auth import gen_oauth_code
from os import getenv

callback_router = APIRouter()


@callback_router.get("/google")
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
        
    return RedirectResponse(hyundai_id_callback + f"?code={gen_oauth_code(user.id).get('code')}")
