from app.repository.base import BaseRepository
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, model=User)
