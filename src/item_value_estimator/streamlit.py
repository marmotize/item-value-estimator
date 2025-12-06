"""Streamlit app entry point."""

import logging
from urllib.parse import urlparse

import streamlit as st

from item_value_estimator.core.logging_config import setup_logging
from item_value_estimator.llms.pydantic_ai_client import run_llm

logger = logging.getLogger(__name__)

if "logging_configured" not in st.session_state:
    setup_logging()
    st.session_state["logging_configured"] = True

st.title("Item Value Estimator")

st.text_input("Item URL", key="item_url")

if st.button("Estimate Value"):
    item_url = st.session_state.get("item_url", "").strip()
    if not item_url:
        st.warning("Please enter an item URL.")
    elif not urlparse(item_url).scheme or not urlparse(item_url).netloc:
        st.error("Please enter a valid URL (including http/https).")
    else:
        with st.spinner("Estimating value..."):
            try:
                value = run_llm(item_url)
            except Exception:
                logger.exception("Failed to estimate value for URL: %s", item_url)
                st.error("Something went wrong while estimating value. Please try again.")
            else:
                st.write(value)
