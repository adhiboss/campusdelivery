import uuid
from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base

class Discount(Base):
    __tablename__ = "discounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    brand_name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    discount_type = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    active = Column(Boolean, default=True)
