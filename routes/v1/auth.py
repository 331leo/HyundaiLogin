from fastapi import APIRouter, HTTPException, Security
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBasic

from models.jwt import JTWType, TokenResponse
from utils import generate_oauth_link
from utils.auth import gen_access_token, verify_oauth_code
from utils.db import client_credentials_db

auth_router = APIRouter()


@auth_router.get("/login", response_class=RedirectResponse)
async def route_login(redirect_uri: str):
    response = RedirectResponse(url=generate_oauth_link())
    response.set_cookie(key="hyundai_id_callback", value=redirect_uri)
    return response


@auth_router.post("/oauth2/token", response_model=TokenResponse)
async def get_access_token(
    code: str = Form(...),
    credentials: HTTPAuthorizationCredentials = Security(HTTPBasic()),
):
    if client_credentials_db.get(credentials.username) == credentials.password.encode():
        id = verify_oauth_code(code)
        if id:
            data = gen_access_token(id)
            return TokenResponse.parse_obj(
                {
                    "access_token": data.get("token"),
                    "token_type": JTWType.ACCESS_TOKEN,
                    "expires_in": 36000,
                    "generated_in": data.get("ts"),
                }
            )
        raise HTTPException(status_code=401, detail="Unauthorized (oAuthCode)")
    raise HTTPException(status_code=401, detail="Unauthorized (Client Secret)")
