from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class JTWType(int, Enum):
    OAUTH_CODE = 0
    ACCESS_TOKEN = 1


class oAuthCode(BaseModel):
    type: JTWType
    ts: int
    id: str


class AccessToken(BaseModel):
    type: JTWType
    ts: int
    hash: str

class TokenResponse(BaseModel):
    access_token: str
    generated_in: int
    expires_in: int
    token_type: JTWType

class TokenRequest(BaseModel):
    code: str