"""Application settings configuration using Pydantic Settings."""

import os
from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent


class AppSettings(BaseSettings):
    """Application settings loaded from environment variables and .env file."""

    # Application settings
    app_name: str = Field(default="Item Value Estimator", description="Application name")
    debug: bool = Field(default=False, description="Debug mode flag")
    log_level: str = Field(default="INFO", description="Logging level")

    # OpenAI settings
    openai_api_key: SecretStr = Field(..., description="OpenAI API key")

    # LangSmith settings
    langsmith_project: str = Field(..., description="LangSmith project name")
    langsmith_api_key: SecretStr = Field(..., description="LangSmith API key")
    langsmith_endpoint: str = Field(..., description="LangSmith API endpoint")

    model_config = SettingsConfigDict(
        env_file=str(PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        env_prefix="ITEM_ESTIMATOR_",
        case_sensitive=False,
        env_ignore_empty=True,
        extra="ignore",
    )

    def export_for_libs(self) -> None:
        def _set(name: str, value: SecretStr | str) -> None:
            os.environ[name] = str(
                value.get_secret_value() if isinstance(value, SecretStr) else value
            )

        _set("OPENAI_API_KEY", self.openai_api_key)
        _set("LANGSMITH_API_KEY", self.langsmith_api_key)
        _set("LANGSMITH_PROJECT", self.langsmith_project)
        _set("LANGSMITH_ENDPOINT", self.langsmith_endpoint)


# Global settings instance
settings = AppSettings()
settings.export_for_libs()
