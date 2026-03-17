from fastapi import APIRouter
from .routes.auth import router as auth_router
from .routes.novels import router as novels_router
from .routes.chapters import router as chapters_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(novels_router)
api_router.include_router(chapters_router)
