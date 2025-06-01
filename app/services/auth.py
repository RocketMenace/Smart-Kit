from typing import Self
from app.repository.user import UserRepository
from app.auth.schemas import UserLoginSchema
from fastapi.exceptions import HTTPException
from fastapi import status
from app.auth.security import verify_password
from app.models.user import User


class AuthService:
    def __init__(self: Self, repository: UserRepository):
        self.repository = repository

    async def login(self: Self, schema: UserLoginSchema):
        user: User = await self.repository.get_by_email(schema.email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with this email: {schema.email} not found",
            )
        if not verify_password(password=schema.password, hashed_password=user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Wrong password"
            )
