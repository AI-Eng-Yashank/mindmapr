#core/config.py
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    APP_NAME: str = "email_scrap"
    SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:0000@localhost/email_scrap"
    SECRET_KEY: str = "your_secret_key_here"
    REFRESH_SECRET_KEY: str = "your_refresh_secret_key_here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600

    EMAIL_USERNAME: Optional[str] = None
    EMAIL_PASSWORD: Optional[str] = None
    GROQ_API_TOKEN: Optional[str] = None
    li_at_cookie: Optional[str] = None
    PGHOST: Optional[str] = None
    PGDATABASE: Optional[str] = None
    PGUSER: Optional[str] = None
    PGPASSWORD: Optional[str] = None
    SENDER_EMAIL: Optional[str] = None
    SENDER_FIRST_NAME: Optional[str] = None
    SENDER_LAST_NAME: Optional[str] = None
    FERNET_SECRET: str


    class Config:
        case_sensitive = True
        env_file = ".env"


try:
    settings = Settings()
except Exception as e:
    print(f"❌ Error loading .env: {e}")
