from pydantic import BaseModel, EmailStr, UUID4, Field
from datetime import datetime
from app.schemas.validators import Password


class UserBaseSchema(BaseModel):
    email: EmailStr = Field(..., max_length=25, examples=["bob@gmail.com"])
    first_name: str = Field(..., min_length=2, max_length=25, examples=["Bob"])
    last_name: str = Field(..., min_length=2, max_length=24, examples=["Martin"])


class UserCreateSchema(UserBaseSchema):
    password: Password = Field(
        ..., min_length=10, max_length=20, examples=["Stringst1!"]
    )


class UserResponseSchema(UserBaseSchema):
    id: UUID4
    created_at: datetime
