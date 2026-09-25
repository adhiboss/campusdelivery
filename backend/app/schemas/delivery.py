import uuid
from datetime import datetime
from pydantic import BaseModel
from app.models.delivery import DeliveryStatus

class DeliveryBase(BaseModel):
    vendor_name: str
    product_name: str

class DeliveryCreate(DeliveryBase):
    pass

class DeliveryResponse(DeliveryBase):
    id: uuid.UUID
    student_id: uuid.UUID
    tracking_id: str
    status: DeliveryStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
