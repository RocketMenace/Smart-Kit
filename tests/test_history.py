import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.anyio
async def test_get_history(async_client: AsyncClient, login_user):
    response = await async_client.get(
        url="/history", headers={"Authorization": "Bearer " + login_user["access"]}
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_history_unauthorized(async_client: AsyncClient):
    response = await async_client.get(url="/history")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
