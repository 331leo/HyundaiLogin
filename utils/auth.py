from typing import Union
import jwt
from os import getenv
from jwt.exceptions import InvalidTokenError, InvalidSignatureError
from models.jwt import oAuthCode, JTWType, AccessToken
from datetime import datetime, time
from utils.etc import md5hash

# jwt.encode({"user_id": 1}, getenv("JWT_SECRET"), algorithm="HS256")
# jwt.decode("TOKEN", getenv("JWT_SECRET"), algorithms="HS256")
# https://stackoverflow.com/questions/64146591/custom-authentication-for-fastapi


def gen_oauth_code(user_id: str):
    timestamp = int(datetime.now().timestamp())
    return {"code": jwt.encode(
        oAuthCode.parse_obj(
            {
                "type": JTWType.OAUTH_CODE,
                "ts": timestamp,
                "id": user_id,
            }
        ).dict(),
        getenv("JWT_SECRET"),
        algorithm="HS256",
    ), "ts": timestamp}

def gen_access_token(user_id: str):
    timestamp = int(datetime.now().timestamp())
    return {"token": jwt.encode(
        AccessToken.parse_obj(
            {
                "type": JTWType.ACCESS_TOKEN,
                "ts": timestamp,
                "hash": md5hash(user_id),
            }
        ).dict(),
        getenv("JWT_SECRET"),
        algorithm="HS256",
    ),"ts": timestamp}

def verify_oauth_code(code: str) -> Union[str, bool]:
    try:
        payload = jwt.decode(code, getenv("JWT_SECRET"), algorithms="HS256")
        return (
            payload.get("id")
            if (
                payload.get("type") == JTWType.OAUTH_CODE
                and int(payload.get("ts")) + 300 > int(datetime.now().timestamp())
            )
            else False
        )

    except (InvalidTokenError, InvalidSignatureError) as e:
        return False

def verify_access_token(token: str) -> Union[str, bool]:
    try:
        payload = jwt.decode(token, getenv("JWT_SECRET"), algorithms="HS256")
        return (
            payload.get("hash")
            if (
                payload.get("type") == JTWType.ACCESS_TOKEN
                and int(payload.get("ts")) + 36000 > int(datetime.now().timestamp())
            )
            else False
        )

    except (InvalidTokenError, InvalidSignatureError) as e:
        return False