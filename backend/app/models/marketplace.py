import uuid
from sqlalchemy import Column, String, ForeignKey, Numeric, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class ListingStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"

class MarketplaceListing(Base):
    __tablename__ = "marketplace_listings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    seller_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(ListingStatus), nullable=False, default=ListingStatus.AVAILABLE)

    seller = relationship("Student")
