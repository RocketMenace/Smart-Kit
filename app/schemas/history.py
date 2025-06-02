from pydantic import BaseModel, Field, ConfigDict


class RequestBaseSchema(BaseModel):
    cadastral_number: str = Field(
        ...,
        min_length=5,
        max_length=30,
        examples=["77:01:0001012:123"],
        pattern=r"^\d{2}:\d{2}:\d{7}:\d+$"
    )
    latitude: float = Field(...,ge=-90, le=90, strict=True, examples=[55.755825])
    longitude: float = Field(...,ge=-180, le=180, strict=True, examples=[37.617298])


class RequestInputSchema(RequestBaseSchema):
    pass


class RequestOutputSchema(RequestBaseSchema):
    response: bool


class HistoryResponseSchema(RequestBaseSchema):
    id: int
    response: bool
    model_config = ConfigDict(from_attributes=True)
