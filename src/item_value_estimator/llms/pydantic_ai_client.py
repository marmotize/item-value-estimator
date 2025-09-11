from openai.types.responses import WebSearchToolParam
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIResponsesModel, OpenAIResponsesModelSettings

from item_value_estimator.core.logging_config import get_logger, setup_logging
from item_value_estimator.core.settings import settings

setup_logging()
logger = get_logger(__name__)


def run_llm(item_url: str) -> str:
    logger.info("Running LLM")
    logger.info(settings.model_dump_json())

    model_settings = OpenAIResponsesModelSettings(
        openai_builtin_tools=[WebSearchToolParam(type="web_search")]
    )
    model = OpenAIResponsesModel("gpt-4o")
    agent = Agent(model=model, model_settings=model_settings)

    result = agent.run_sync(
        f"How much would you estimate the fair marker value of this item: {item_url}"
    )
    return result.output


if __name__ == "__main__":
    run_llm("")
