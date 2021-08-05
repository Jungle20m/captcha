from pydantic import BaseModel


class CaptchaVerify(BaseModel):
    key: int
    end_width: int
    end_height: int