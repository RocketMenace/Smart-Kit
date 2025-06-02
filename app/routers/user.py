from fastapi import APIRouter, status, Depends

from app.auth.dependencies import get_current_user
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
    path="/login", status_code=status.HTTP_200_OK, response_model=TokenResponseSchema
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
    """
    Logs out the current user by blacklisting their JWT token.

    - **token**: The JWT access token to invalidate
    - **returns**: Success message
    """
    return await use_case.logout_user(token=token)


@router.post(path="/refresh", status_code=status.HTTP_200_OK)
async def refresh(
    use_case: Annotated[LoginUserUseCase, Depends(get_user_login_use_case)],
    token: Annotated[str, Depends(get_current_user)],
):
    return await use_case.refresh_token(token=token)
