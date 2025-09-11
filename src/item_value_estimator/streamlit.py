"""Streamlit app entry point."""

import streamlit as st

from item_value_estimator.llms.pydantic_ai_client import run_llm

st.title("Item Value Estimator")

st.text_input("Item URL", key="item_url")

if st.button("Estimate Value"):
    st.write("Estimating value...")
    value = run_llm(st.session_state.item_url)
    st.write(value)
