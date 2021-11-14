from fastapi import APIRouter

from .auth import auth_router

# from .users import users_router
from .callback import callback_router
from .test import test_router
from .users import user_router

v1_router = APIRouter()

# v1_router.include_router(users_router, prefix="/users", tags=["users"])
v1_router.include_router(test_router, prefix="/test", tags=["test"])


v1_router.include_router(callback_router, prefix="/callback", tags=["callback"])
v1_router.include_router(auth_router, tags=["auth"])
v1_router.include_router(user_router, prefix="/users", tags=["users"])