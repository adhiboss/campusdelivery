from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.discount import Discount
from app.schemas.discount import DiscountResponse

router = APIRouter()

@router.get("/", response_model=List[DiscountResponse])
def get_discounts(db: Session = Depends(get_db)):
    return db.query(Discount).filter(Discount.active == True).all()
