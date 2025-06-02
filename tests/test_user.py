import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.anyio
async def test_register_user(async_client: AsyncClient):
    payload = {
        "email": "bob@gmail.com",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringst1&",
    }
    response = await async_client.post(url="/users/register", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == payload["email"]


@pytest.mark.anyio
async def test_register_user_invalid_password_format(async_client: AsyncClient):
    payload = {
        "email": "bob@gmail.com",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringsdsfgdf",
    }
    response = await async_client.post(url="/users/register", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "password" in response.text.lower()


@pytest.mark.anyio
async def test_register_user_invalid_email_format(async_client: AsyncClient):
    payload = {
        "email": "bdffgs",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringsdsfgdf",
    }
    response = await async_client.post(url="/users/register", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert "email" in response.text.lower()


@pytest.mark.anyio
async def test_register_user_already_exists(async_client: AsyncClient, register_user):
    payload = {
        "email": "bob@gmail.com",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringst1&",
    }
    response = await async_client.post(url="/users/register", json=payload)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert "already exists" in response.text.lower()


@pytest.mark.anyio
async def test_password_not_in_response(async_client: AsyncClient):
    payload = {
        "email": "bob@gmail.com",
        "first_name": "Bob",
        "last_name": "Martin",
        "password": "Stringst1&",
    }
    response = await async_client.post(url="/users/register", json=payload)
    assert "password" not in response.json()
