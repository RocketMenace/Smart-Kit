from pydantic import BaseModel


class QueryBase(BaseModel):
    cadastral_number: int
    latitude: float
    longtitude: float


class Query(QueryBase):
    pass


class QueryResponse(QueryBase):
    response: bool
