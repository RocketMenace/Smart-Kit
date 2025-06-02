from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.auth.jwt import decode_jwt
from app.config.settings import config
import jwt
from jwt.exceptions import InvalidTokenError
from app.auth.exceptions import NotAuthenticated
from app.repository.user import UserRepository
from app.dependencies.repository import get_user_repository
from fastapi import Request


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, token: str) -> bool:
        is_token_valid: bool = False

        try:
            payload = decode_jwt(token)
        except:
            payload = None
        if payload:
            is_token_valid = True

        return is_token_valid


async def get_current_user(
    token: Annotated[str, Depends(JWTBearer())],
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
