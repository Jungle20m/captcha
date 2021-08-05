import json
import random
from fastapi import APIRouter
from src.database.database import Session
from src.database.crud.captcha import CRUDCaptcha
from src.schemas.captcha import CaptchaVerify

router = APIRouter()


@router.get("/generate")
async def generate():
    try:
        session = Session()
        captcha_ids = CRUDCaptcha.get_list_ids(session=session)
        if len(captcha_ids) == 0:
            raise Exception("captcha storage is empty")
        random_captcha_id = random.choice(captcha_ids)
        captcha = CRUDCaptcha.get_captcha(session=session, id=random_captcha_id)
        data = {
            "captcha_key": captcha[0],
            "backgroud_image": captcha[1],
            "puzzle_piece_image": captcha[2],
            "width": captcha[3],
            "height": captcha[4],
            "start_width": captcha[5],
            "start_height": captcha[6],
        }
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "failed", "message": f"{e}", "data": {}}
    finally:
        session.close()

@router.post("/verify")
async def generate(body: CaptchaVerify):
    try:
        session = Session()
        captcha = CRUDCaptcha.get_captcha(session, id=body.key)
        if (body.end_width == captcha[7]) and (body.end_height == captcha[8]):
            return {"status": "success", "message": "captcha matched"} 
        return {"status": "failed", "message": "captcha not match"}
    except Exception as e:
        return {"status": "failed", "message": f"{e}"}