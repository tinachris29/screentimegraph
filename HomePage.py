# Main landing page for the Streamlit application.
import streamlit as st

st.set_page_config(page_title="Homepage", page_icon="🏠")

st.title("Welcome to the Data Dashboard! 📊")

st.markdown(
    """
This simple multi‑page Streamlit app lets you:
- **Survey**: enter your data (we'll append it to a CSV stored relative to the app).
- **Visuals**: explore charts built from the CSV and a companion **data.json**.

Use the **sidebar** to switch pages.
"""
)
