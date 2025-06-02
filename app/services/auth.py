from typing import Self

from jwt import InvalidTokenError

from app.repository.user import UserRepository
from app.auth.schemas import UserLoginSchema
from fastapi.exceptions import HTTPException
from fastapi import status
from app.auth.security import verify_password
from app.models.user import User
from app.auth.jwt import generate_jwt, decode_jwt
from fastapi.responses import JSONResponse


class AuthService:
    def __init__(self: Self, repository: UserRepository):
        self.repository = repository

    async def login(self: Self, schema: UserLoginSchema) -> dict[str, str]:
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
        return generate_jwt(user=user)

    async def logout(self: Self):
        return JSONResponse(
            content={"message": "Successfully logged out"},
            status_code=status.HTTP_200_OK,
        )

    async def refresh(self: Self, token: str) -> dict[str, str]:
        try:
            payload = decode_jwt(token)
            user: User = await self.repository.get_by_uuid(uuid=payload.get("sub"))
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
                )
            return generate_jwt(user=user)
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token."
            )
