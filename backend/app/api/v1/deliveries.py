import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.user import User, UserRole
from app.models.delivery import Delivery, DeliveryStatus
from app.models.student import Student
from app.schemas.delivery import DeliveryCreate, DeliveryResponse
from app.api.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=DeliveryResponse)
def create_delivery(
    delivery_in: DeliveryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.STUDENT:
        raise HTTPException(status_code=403, detail="Only students can create deliveries")
    
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    if not student:
        raise HTTPException(status_code=400, detail="Student profile not found")

    tracking_id = f"TRK-{uuid.uuid4().hex[:8].upper()}"
    
    db_delivery = Delivery(
        student_id=student.id,
        vendor_name=delivery_in.vendor_name,
        product_name=delivery_in.product_name,
        tracking_id=tracking_id,
        status=DeliveryStatus.CREATED
    )
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery

@router.get("/", response_model=List[DeliveryResponse])
def get_deliveries(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role == UserRole.STUDENT:
        student = db.query(Student).filter(Student.user_id == current_user.id).first()
        if not student:
            return []
        return db.query(Delivery).filter(Delivery.student_id == student.id).all()
    elif current_user.role == UserRole.DELIVERY_PARTNER:
        return db.query(Delivery).all()
    else:
        return db.query(Delivery).all()
