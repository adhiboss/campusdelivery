import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Campus Delivery Hub API"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+psycopg://cdh_user:cdh_password@localhost:5432/campus_delivery_db")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "super-secret-development-key")
    JWT_ACCESS_EXPIRATION: int = 3600  # 1 hour
    JWT_REFRESH_EXPIRATION: int = 604800  # 7 days

    class Config:
        case_sensitive = True

settings = Settings()
