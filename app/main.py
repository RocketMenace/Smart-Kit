from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from app.infrastructure.http_client import AsyncHTTPClient


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = AsyncHTTPClient(base_url="https://api.thirdparty.com")
    yield
    await app.state.http_client.close()


app = FastAPI(root_path="/api", title="", lifespan=lifespan)
