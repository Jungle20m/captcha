from fastapi import APIRouter

from src.controllers import captcha

router = APIRouter()
router.include_router(captcha.router, prefix="")