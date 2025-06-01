from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from sqladmin import Admin
from app.config.database import database

from app.infrastructure.http_client import AsyncHTTPClient
from app.routers import history, request, user
from app.admin.user import UserAdmin
from app.admin.history import HistoryAdmin


@asynccontextmanager
async def lifespan(_: FastAPI):
    _.state.http_client = AsyncHTTPClient(base_url="http://localhost:8000/api")
    yield
    await _.state.http_client.close()


app = FastAPI(root_path="/api", title="Smartkit", lifespan=lifespan)
admin = Admin(app, database.engine)

app.include_router(history.router)
app.include_router(request.router)
app.include_router(user.router)

admin.add_view(UserAdmin)
admin.add_view(HistoryAdmin)

