import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.models.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    usn = Column(String, unique=True, index=True, nullable=False)
    hostel_block = Column(String, nullable=False)
    room_no = Column(String, nullable=False)

    user = relationship("User", backref="student_profile")
