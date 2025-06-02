from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from sqladmin import Admin
from app.config.database import database
from app.infrastructure.redis import redis_client

from app.routers import history, request, user
from app.admin.user import UserAdmin
from app.admin.history import HistoryAdmin


@asynccontextmanager
async def lifespan(_: FastAPI):
    await redis_client.connect()
    yield
    await redis_client.close()


app = FastAPI(root_path="/api", title="Smartkit", lifespan=lifespan)
admin = Admin(app, database.engine)

app.include_router(history.router)
app.include_router(request.router)
app.include_router(user.router)

admin.add_view(UserAdmin)
admin.add_view(HistoryAdmin)

