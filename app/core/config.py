from pydantic_settings import BaseSettings
from pydantic import field_validator
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./novel.db"
    JWT_SECRET: str = "dev-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def validate_database_url(cls, v: str) -> str:
        """Validate DATABASE_URL is a valid SQLAlchemy URL format."""
        if isinstance(v, str):
            valid_prefixes = ("postgresql://", "postgresql+psycopg2://", "sqlite:///", "mysql://", "mysql+pymysql://")
            if v.startswith(valid_prefixes):
                return v
        # Fallback to SQLite if invalid
        return "sqlite:///./novel.db"

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()
