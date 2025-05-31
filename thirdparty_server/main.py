from fastapi import FastAPI
from thirdparty_server import routers


app = FastAPI(title="third_party_service", root_path="/api")

app.include_router(routers.router, prefix="/third-party-server")
