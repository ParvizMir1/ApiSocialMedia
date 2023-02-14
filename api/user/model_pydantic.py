from pydantic import BaseModel, validator
from typing import Optional


class User(BaseModel):
    id: int
    user_name: str
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: str
    about: Optional[str]

    # Проверка почты
    @validator('email')
    def check_email(cls, mail: str):
        if "@" in mail:
            return mail

        raise TypeError('Почта указано неверна')

    # Проверка номера телефона
    @validator('phone_number')
    def check_phone_number(cls, number: str):
        pass
