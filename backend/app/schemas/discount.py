import uuid
from datetime import date
from pydantic import BaseModel

class DiscountBase(BaseModel):
    brand_name: str
    title: str
    description: str | None = None
    discount_type: str
    start_date: date
    end_date: date
    active: bool

class DiscountResponse(DiscountBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
