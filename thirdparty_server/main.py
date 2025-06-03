from fastapi import FastAPI
from thirdparty_server.routers import router


app = FastAPI(title="third_party_service", root_path="/api")

app.include_router(router, prefix="/third-party-server")
