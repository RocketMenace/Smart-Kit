from fastapi import APIRouter, status, Depends
from app.schemas.history import RequestInputSchema

router = APIRouter(prefix="/third-party-server", tags=["Response server"])

@router.post("/result", status_code=status.HTTP_200_OK)
async  def get_response(request: RequestInputSchema, use_case):
    pass


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping_server():
    pass