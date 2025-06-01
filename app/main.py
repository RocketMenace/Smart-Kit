from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from app.infrastructure.http_client import AsyncHTTPClient
from app.routers import history, request, user


@asynccontextmanager
async def lifespan(_: FastAPI):
    _.state.http_client = AsyncHTTPClient(base_url="http://localhost:8000/api")
    yield
    await _.state.http_client.close()


app = FastAPI(root_path="/api", title="Smartkit", lifespan=lifespan)

app.include_router(history.router)
app.include_router(request.router)
app.include_router(user.router)
