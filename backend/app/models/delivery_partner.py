import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class DeliveryPartner(Base):
    __tablename__ = "delivery_partners"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    company = Column(String, nullable=False)
    vehicle_no = Column(String, nullable=False)

    user = relationship("User", backref="delivery_partner_profile")
