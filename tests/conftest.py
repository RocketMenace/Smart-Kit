from typing import AsyncGenerator, Generator
from httpx import AsyncClient, ASGITransport
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config.database import TEST_DATABASE_URL, database


import pytest

test_async_engine = create_async_engine(url=TEST_DATABASE_URL, echo=False)
testing_async_session = async_sessionmaker(
    test_async_engine, class_=AsyncSession, expire_on_commit=False
)


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
async def db_session():
    """Create and drop test DB tables."""
    async with test_async_engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)

    yield

    async with test_async_engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.drop_all)

    await test_async_engine.dispose()


@pytest.fixture()
async def client(db_session) -> AsyncGenerator:
    async with testing_async_session() as session:

        async def override_get_db():
            yield session

    app.dependency_overrides[database.get_session] = override_get_db
    with TestClient(app=app) as test_client:
        yield test_client


@pytest.fixture()
async def async_client(client: TestClient) -> AsyncGenerator:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url=client.base_url
    ) as ac:
        yield ac


@pytest.fixture()
async def register_user(async_client: AsyncClient):
    payload = {
        "email": "bob@gmail.com",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringst1&",
    }
    await async_client.post(url="/users/register", json=payload)
