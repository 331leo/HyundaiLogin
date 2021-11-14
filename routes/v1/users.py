import json as jsonlib

from fastapi import APIRouter, HTTPException, Security
from fastapi.param_functions import Depends
from fastapi.params import Form
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import RedirectResponse
from starlette.responses import JSONResponse

from models.jwt import JTWType, TokenResponse
from models.user import User
from utils import generate_oauth_link
from utils.auth import gen_access_token, gen_oauth_code, verify_oauth_code, verify_access_token
from utils.db import user_db

user_router = APIRouter()



@user_router.get("/@me", response_model=User)
async def get_user_data(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    hash = verify_access_token(credentials.credentials)
    if not hash:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return User.parse_obj(jsonlib.loads(user_db.get(hash).decode("UTF-8")))