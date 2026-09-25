import uuid
from pydantic import BaseModel, condecimal
from app.models.marketplace import ListingStatus

class ListingBase(BaseModel):
    title: str
    description: str | None = None
    price: condecimal(max_digits=10, decimal_places=2)

class ListingCreate(ListingBase):
    pass

class ListingResponse(ListingBase):
    id: uuid.UUID
    seller_id: uuid.UUID
    status: ListingStatus

    class Config:
        from_attributes = True
