from langsmith.integrations.otel import configure
from openai.types.responses import WebSearchToolParam
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIResponsesModel, OpenAIResponsesModelSettings

from item_value_estimator.core.logging_config import get_logger, setup_logging
from item_value_estimator.core.settings import settings

logger = get_logger(__name__)

Agent.instrument_all()
configure(project_name=settings.langsmith_project)


def run_llm(item_url: str) -> str:
    logger.info("Running LLM")

    model_settings = OpenAIResponsesModelSettings(
        openai_builtin_tools=[WebSearchToolParam(type="web_search")]
    )
    model = OpenAIResponsesModel("gpt-5.1-2025-11-13")
    agent = Agent(model=model, model_settings=model_settings)

    prompt = (
        "You are an AI agent tasked with estimating the market value of items on "
        "marketplaces and providing the value for flippers.\n"
        f"How much would you estimate the fair market value of this item: {item_url}"
        "\n"
        "If the link provided is not a valid item to estimate, please reply with 'Invalid item URL'"
    )

    result = agent.run_sync(prompt)
    return result.output


if __name__ == "__main__":
    setup_logging()
    run_llm("")
