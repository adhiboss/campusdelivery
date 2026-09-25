import uuid
from datetime import datetime
from pydantic import BaseModel

class NotificationBase(BaseModel):
    message: str
    type: str

class NotificationResponse(NotificationBase):
    id: uuid.UUID
    user_id: uuid.UUID
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
