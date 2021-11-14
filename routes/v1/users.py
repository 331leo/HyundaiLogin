import json as jsonlib

from fastapi import APIRouter, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from models.user import User
from utils.auth import verify_access_token
from utils.db import user_db

user_router = APIRouter()


@user_router.get("/@me", response_model=User)
async def get_user_data(
    credentials: HTTPAuthorizationCredentials = Security(HTTPBearer()),
):
    hash = verify_access_token(credentials.credentials)
    if not hash:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return User.parse_obj(jsonlib.loads(user_db.get(hash).decode("UTF-8")))
