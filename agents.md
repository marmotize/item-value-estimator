# Agents

## Overview
- Purpose: estimate fair market value of a marketplace listing given its URL, optimized for flippers looking for quick price guidance.
- Location: the agent lives in `src/item_value_estimator/llms/pydantic_ai_client.py` and is invoked from the Streamlit UI (`src/item_value_estimator/streamlit.py`).
- Stack: [PydanticAI](https://ai.pydantic.dev/) `Agent` using `OpenAIResponsesModel` with the built-in `web_search` tool enabled.

## Runtime flow
1. Streamlit collects an `item_url` and calls `run_llm(item_url)`.
2. `run_llm` logs the current settings, builds a responses model (`gpt-5.1-2025-11-13`) with `web_search` enabled, and creates a simple agent.
3. The agent runs a single message prompt (value estimation with flipper context) and returns the string output.
4. The result is sent back to Streamlit and shown in the UI.

## Configuration
- API key: set `ITEM_ESTIMATOR_OPENAI_API_KEY` (loaded via `src/item_value_estimator/core/settings.py`; also exported as `OPENAI_API_KEY` for the OpenAI client).
- Model: `gpt-5.1-2025-11-13` in responses mode; adjust in `run_llm` if you need a different model or transport.
- Tools: OpenAI’s built-in `web_search` tool is enabled via `WebSearchToolParam(type="web_search")`. Add more tools by extending `openai_builtin_tools` in `model_settings`.
- Logging: configured through `setup_logging()` and controlled by `ITEM_ESTIMATOR_LOG_LEVEL`/`ITEM_ESTIMATOR_DEBUG`.

## Running locally
- Ensure dependencies are installed and your `.env` is populated (see `.env.example`).
- Start the UI: `streamlit run src/item_value_estimator/streamlit.py`
- Enter an item URL and click “Estimate Value” to trigger the agent call.
- After any change (especially LLM-generated), run `poe check` to apply formatting, lint, and type checks.

## Customizing the agent
- Update the prompt in `run_llm` to include stricter output formatting (e.g., JSON with fields like `estimated_price`, `confidence`, `reasoning`).
- Swap models or add system instructions by editing the `Agent` construction in `pydantic_ai_client.py`.
- If you add new tools (pricing APIs, marketplace scrapers), register them in `model_settings` and incorporate their outputs into the prompt or post-processing.
