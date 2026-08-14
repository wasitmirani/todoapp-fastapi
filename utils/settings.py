from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


# Create a settings class
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8",extra="ignore")
    DB_URL: str = Field(..., env="DB_URL")

# Create a settings instance
settings = Settings()
