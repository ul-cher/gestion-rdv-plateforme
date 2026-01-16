from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASSWORD: str
    
    REDIS_URL: str
    
    DEBUG: bool = False
    ENVIRONMENT: str = "production"
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()