
from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    price: float

    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price is smaller or equal to 0.")
        return value