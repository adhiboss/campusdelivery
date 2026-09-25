from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.models.university_store import StoreProduct
from app.schemas.university_store import ProductResponse

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(StoreProduct).all()
