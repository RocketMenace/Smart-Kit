from fastapi import APIRouter, status, Depends

from app.auth.dependencies import get_current_user, RefreshToken
from app.auth.schemas import UserLoginSchema
from app.schemas.user import UserResponseSchema, UserCreateSchema
from typing import Annotated
from app.use_cases.register_user import UserRegisterUseCase
from app.dependencies.use_cases import (
    get_user_register_use_case,
    get_user_login_use_case,
)
from app.use_cases.login_user import LoginUserUseCase
from app.auth.schemas import TokenResponseSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
    description="Register user with specified credentials.",
)
async def register(
    request: UserCreateSchema,
    use_case: Annotated[UserRegisterUseCase, Depends(get_user_register_use_case)],
):
    return await use_case.register(schema=request)


@router.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponseSchema,
    summary="Authenticate user and get access token",
    description="Authenticates user credentials and returns JWT tokens for authorization.",
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "description": "Invalid request data",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid email or password format"}
                }
            },
        },
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthorized - Invalid credentials",
            "content": {
                "application/json": {
                    "example": {"detail": "Incorrect email or password"}
                }
            },
        },
    },
)
async def login(
    request: UserLoginSchema,
    use_case: Annotated[LoginUserUseCase, Depends(get_user_login_use_case)],
):
    return await use_case.login_user(schema=request)


@router.post(
    path="/logout",
    status_code=status.HTTP_200_OK,
    summary="User logout",
    description="Invalidates the current access token by adding it to the blacklist",
    responses={
        status.HTTP_200_OK: {"description": "Successfully logged out"},
        status.HTTP_401_UNAUTHORIZED: {"description": "Invalid or expired token"},
    },
)
async def logout(
    use_case: Annotated[
        LoginUserUseCase,
        Depends(get_user_login_use_case),
    ],
    token: Annotated[str, Depends(get_current_user)],
):
    return await use_case.logout_user(token=token)


@router.get(
    path="/refresh",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponseSchema,
    summary="Refresh access token",
    description="Generates a new access token using a valid refresh token.",
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Unauthorized - Invalid or expired refresh token",
            "content": {
                "application/json": {
                    "examples": {
                        "invalid_token": {"value": {"detail": "Invalid refresh token"}},
                        "expired_token": {"value": {"detail": "Token has expired"}},
                    }
                }
            },
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "Forbidden - Token is not a refresh token",
            "content": {
                "application/json": {"example": {"detail": "Not a refresh token"}}
            },
        },
    },
)
async def refresh(
    use_case: Annotated[LoginUserUseCase, Depends(get_user_login_use_case)],
    token: Annotated[str, Depends(RefreshToken())],
):
    return await use_case.refresh_token(token=token)
