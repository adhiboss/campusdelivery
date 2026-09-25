import uuid
from pydantic import BaseModel, condecimal

class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: condecimal(max_digits=10, decimal_places=2)
    category: str
    image_url: str | None = None

class ProductResponse(ProductBase):
    id: uuid.UUID

    class Config:
        from_attributes = True
