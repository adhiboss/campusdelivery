from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import router as auth_router
from app.api.v1.deliveries import router as deliveries_router
from app.api.v1.notifications import router as notifications_router
from app.api.v1.marketplace import router as marketplace_router
from app.api.v1.university_store import router as store_router
from app.api.v1.discounts import router as discounts_router

app = FastAPI(
    title="Campus Delivery Hub API",
    description="API for managing deliveries, users, and marketplace at Jain University.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(deliveries_router, prefix="/api/v1/deliveries", tags=["Deliveries"])
app.include_router(notifications_router, prefix="/api/v1/notifications", tags=["Notifications"])
app.include_router(marketplace_router, prefix="/api/v1/marketplace", tags=["Marketplace"])
app.include_router(store_router, prefix="/api/v1/store", tags=["Store"])
app.include_router(discounts_router, prefix="/api/v1/discounts", tags=["Discounts"])

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/ready")
def readiness_check():
    # Will check DB connection later
    return {"status": "ready"}
