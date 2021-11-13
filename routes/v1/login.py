from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from utils import generate_oauth_link

login_router = APIRouter()


@login_router.get("/login")
async def route_login(redirect_uri: str):
    response = RedirectResponse(url=generate_oauth_link())
    response.set_cookie(key="hyundai_id_callback", value=redirect_uri)
    return response
