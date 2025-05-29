from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime


class UserBaseSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserResponseSchema(UserBaseSchema):
    id: UUID4
    created_at: datetime
