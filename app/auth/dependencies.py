from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.config.settings import config
import jwt
from jwt.exceptions import InvalidTokenError
from app.auth.exceptions import NotAuthenticated
from app.repository.user import UserRepository
from app.dependencies.repository import get_user_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    repository: Annotated[UserRepository, Depends(get_user_repository)],
):
    try:
        payload = jwt.decode(token, config.API_KEY, algorithms=[config.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise NotAuthenticated()
    except InvalidTokenError:
        raise NotAuthenticated()
    return await repository.get_by_uuid(uuid=user_id)
