from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.settings import config

DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"
TEST_DATABASE_URL = f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}"


class Database:
    def __init__(self):
        self.engine = create_async_engine(DATABASE_URL, echo=True, future=True)
        self.Base = declarative_base()

    async def get_session(self):
        async_session = sessionmaker(self.engine, class_=AsyncSession)
        session = None
        try:
            session = async_session()
            async with session:
                yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()


database = Database()
