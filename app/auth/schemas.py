from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access: str
    refresh: str
