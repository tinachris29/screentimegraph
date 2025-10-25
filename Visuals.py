# Page for rendering charts from CSV + JSON.
import streamlit as st
import pandas as pd
import json
from pathlib import Path

st.set_page_config(page_title="Visualizations", page_icon="📈")

st.title("Data Visualizations 📈")
st.write("This page reads **data.csv** and **data.json** (if present) and renders charts.")

APP_DIR = Path(__file__).resolve().parents[1]  # points to Lab02/
CSV_PATH = APP_DIR / "data.csv"
JSON_PATH = APP_DIR / "data.json"

# Load CSV if available
df = None
if CSV_PATH.exists() and CSV_PATH.stat().st_size > 0:
    try:
        df = pd.read_csv(CSV_PATH)
        st.subheader("CSV Preview")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading data.csv: {e}")
else:
    st.info("No CSV found yet. Add data on the Survey page.")

# Load JSON if available
json_data = {}
if JSON_PATH.exists() and JSON_PATH.stat().st_size > 0:
    try:
        json_data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        st.subheader("JSON Preview")
        st.json(json_data)
    except Exception as e:
        st.error(f"Error reading data.json: {e}")
else:
    st.info("No JSON found or empty.")

# Example chart from CSV if it contains hours columns
if df is not None:
    possible_cols = [c for c in df.columns if c.startswith("hrs")]
    if possible_cols:
        st.subheader("Hours per App (stacked by row)")
        # Create a long-form view if needed
        long_rows = []
        for _, row in df.iterrows():
            for i in range(1, 4):
                app_col = f"app{i}"
                hrs_col = f"hrs{i}"
                if app_col in df.columns and hrs_col in df.columns:
                    long_rows.append({
                        "name": row.get("name", ""),
                        "app": row.get(app_col, f"app{i}"),
                        "hours": row.get(hrs_col, 0.0),
                    })
        if long_rows:
            long_df = pd.DataFrame(long_rows)
            st.bar_chart(long_df.pivot_table(index="app", values="hours", aggfunc="sum"))
        else:
            st.info("No app/hour columns found to chart.")
