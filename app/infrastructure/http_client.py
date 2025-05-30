import httpx
from typing import Self

from fastapi.exceptions import HTTPException
from fastapi import status


class AsyncHTTPClient:
    def __init__(self, base_url: str):
        self.client = httpx.AsyncClient(
            base_url=base_url,
            limits=httpx.Limits(max_connections=50, max_keepalive_connections=20),
        )

    async def post(self: Self, endpoint: str, **kwargs) -> httpx.Response:
        try:
            response = await self.client.post(endpoint, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            raise HTTPException(
                detail=f"HTTP error: {str(e)}", status_code=status.HTTP_400_BAD_REQUEST
            )
        except httpx.RequestError as e:
            raise HTTPException(
                detail=f"Connection failed: {str(e)}",
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    async def close(self):
        await self.client.aclose()
