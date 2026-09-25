import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.user import User, UserRole
from app.models.student import Student
from app.models.marketplace import MarketplaceListing, ListingStatus
from app.schemas.marketplace import ListingCreate, ListingResponse
from app.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[ListingResponse])
def get_listings(db: Session = Depends(get_db)):
    return db.query(MarketplaceListing).filter(MarketplaceListing.status == ListingStatus.AVAILABLE).all()

@router.post("/", response_model=ListingResponse)
def create_listing(
    listing_in: ListingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.role != UserRole.STUDENT:
        raise HTTPException(status_code=403, detail="Only students can post listings")
    
    student = db.query(Student).filter(Student.user_id == current_user.id).first()
    if not student:
        raise HTTPException(status_code=400, detail="Student profile not found")

    db_listing = MarketplaceListing(
        seller_id=student.id,
        title=listing_in.title,
        description=listing_in.description,
        price=listing_in.price,
        status=ListingStatus.AVAILABLE
    )
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing
