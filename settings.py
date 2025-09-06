"""Application settings configuration using Pydantic Settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # Application settings
    app_name: str = Field(default="Item Value Estimator", description="Application name")
    debug: bool = Field(default=False, description="Debug mode flag")
    log_level: str = Field(default="INFO", description="Logging level")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="ITEM_ESTIMATOR_",
        case_sensitive=False,
        extra="ignore",
    )


# Global settings instance
settings = AppSettings()
