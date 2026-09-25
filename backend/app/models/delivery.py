import uuid
import enum
from datetime import datetime
from sqlalchemy import Column, String, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class DeliveryStatus(str, enum.Enum):
    CREATED = "CREATED"
    ASSIGNED = "ASSIGNED"
    IN_TRANSIT = "IN_TRANSIT"
    ARRIVED_AT_HUB = "ARRIVED_AT_HUB"
    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    VERIFICATION_PENDING = "VERIFICATION_PENDING"
    PICKED_UP = "PICKED_UP"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)
    delivery_partner_id = Column(UUID(as_uuid=True), ForeignKey("delivery_partners.id"), nullable=True)
    vendor_name = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    tracking_id = Column(String, unique=True, index=True, nullable=False)
    pickup_counter_id = Column(UUID(as_uuid=True), ForeignKey("pickup_counters.id"), nullable=True)
    status = Column(Enum(DeliveryStatus), nullable=False, default=DeliveryStatus.CREATED)
    otp_code = Column(String, nullable=True)
    qr_payload = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    student = relationship("Student")
    delivery_partner = relationship("DeliveryPartner")
    pickup_counter = relationship("PickupCounter")
