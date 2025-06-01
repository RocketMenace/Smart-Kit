from datetime import datetime, timezone, timedelta
from app.models.user import User

from app.config.settings import config
import jwt


def create_access_token(
    user: User,
) -> str:
    access_expiration = datetime.now(tz=timezone.utc) + timedelta(
        minutes=config.ACCESS_JWT_EXPIRED
    )
    access_jwt_data = {"sub": user.id, "exp": access_expiration, "type": "access"}
    return jwt.encode(access_jwt_data, config.API_KEY, algorithm=config.JWT_ALGORITHM)


def create_refresh_token(user: User) -> str:
    refresh_expiration = datetime.now(tz=timezone.utc) + timedelta(
        minutes=config.REFRESH_JWT_EXPIRED
    )
    refresh_jwt_data = {"sub": user.id, "exp": refresh_expiration, "type": "refresh"}
    return jwt.encode(refresh_jwt_data, config.API_KEY, algorithm=config.JWT_ALGORITHM)

def generate_jwt(user: User) -> dict[str,str]:
    access = create_access_token(user=user)
    refresh = create_refresh_token(user=user)
    return {"access": access, "refresh": refresh}
