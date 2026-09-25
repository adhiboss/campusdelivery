import uuid
from datetime import datetime
from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base
import enum

class UserRole(str, enum.Enum):
    STUDENT = "STUDENT"
    DELIVERY_PARTNER = "DELIVERY_PARTNER"
    UNIVERSITY_ADMIN = "UNIVERSITY_ADMIN"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    phone = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
