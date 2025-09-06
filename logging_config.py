"""Logging configuration for the application."""

import logging
import sys
from pathlib import Path

from settings import settings


def setup_logging() -> None:
    """Configure logging with best practices and minimal setup."""
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, settings.log_level.upper()))

    # Remove existing handlers to avoid duplicates
    root_logger.handlers.clear()

    # Console handler with colored output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, settings.log_level.upper()))

    # File handler for persistent logging
    file_handler = logging.FileHandler(logs_dir / "app.log")
    file_handler.setLevel(logging.INFO)

    # Create formatters
    console_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Set formatters
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # Add handlers to root logger
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Suppress verbose third-party logging in production
    if not settings.debug:
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("requests").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance for the given name."""
    return logging.getLogger(name)


# Convenience logger for quick use (not recommended for production modules)
logger = logging.getLogger("app")
