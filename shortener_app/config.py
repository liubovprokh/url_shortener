from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):

    env_name: str = "Local"
    base_url: str = "http://localhost"
    db_url: str = ""

    class Config:
        _env_file = "/code/.env",
        _env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
