from typing import AsyncGenerator

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.dependencies.services import get_http_client
from app.routers import history, user, request, response


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncGenerator:
    http_client = await get_http_client()
    yield
    await http_client.close()


app = FastAPI(root_path="/api", title="SmartKit", lifespan=lifespan)

app.include_router(user.router)
app.include_router(history.router)
app.include_router(request.router)
app.include_router(response.router)
