from fastapi import APIRouter, status, Depends
from app.schemas.user import UserResponseSchema, UserCreateSchema
from typing import Annotated
from app.use_cases.register_user import UserRegisterUseCase
from app.dependencies.use_cases import get_user_register_use_case

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    path="/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponseSchema,
)
async def register(
    request: UserCreateSchema,
    use_case: Annotated[UserRegisterUseCase, Depends(get_user_register_use_case)],
):
    return await use_case.register(schema=request)


@router.post(path="/login", status_code=status.HTTP_200_OK, response_model=...)
async def login(request: ..., use_case: Annotated[..., Depends()]):
    pass
