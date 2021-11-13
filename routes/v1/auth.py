from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from models.jwt import JTWType, TokenRequest, TokenResponse

from utils import generate_oauth_link
from utils.auth import gen_access_token, gen_oauth_code, verify_oauth_code
auth_router = APIRouter()


@auth_router.get("/login")
async def route_login(redirect_uri: str):
    response = RedirectResponse(url=generate_oauth_link())
    response.set_cookie(key="hyundai_id_callback", value=redirect_uri)
    return response


@auth_router.post("/oauth2/token", response_model=TokenResponse)
async def get_access_token(code: TokenRequest):
    id = verify_oauth_code(code.code)
    if id:
        data = gen_access_token(id)
        return TokenResponse.parse_obj({"access_token": data.get("token"), "token_type": JTWType.ACCESS_TOKEN, "expires_in": 36000, "generated_in": data.get("ts")})
    
