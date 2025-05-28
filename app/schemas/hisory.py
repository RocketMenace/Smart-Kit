from pydantic import BaseModel


class QueryBase(BaseModel):
    cadastral_number: str
    latitude: float
    longtitude: float


class Query(QueryBase):
    pass


class QueryResponse(QueryBase):
    id: int
    response: bool
