"""Main application entry point."""

from logging_config import get_logger, setup_logging
from settings import settings

# Initialize logging
setup_logging()
logger = get_logger(__name__)


def main() -> None:
    """Run the main application."""
    logger.info("Starting %s", settings.app_name)
    logger.debug("Debug mode: %s", settings.debug)
    logger.debug("Log level: %s", settings.log_level)

    logger.info("Application started successfully")


if __name__ == "__main__":
    main()
