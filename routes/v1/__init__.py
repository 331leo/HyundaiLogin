from fastapi import APIRouter

# from .users import users_router
from .callback import callback_router

v1_router = APIRouter()

# v1_router.include_router(users_router, prefix="/users", tags=["users"])
v1_router.include_router(callback_router, prefix="/callback", tags=["callback"])
