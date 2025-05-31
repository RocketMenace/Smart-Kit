from pydantic import BaseModel


class RequestBaseSchema(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float


class RequestInputSchema(RequestBaseSchema):
    pass
