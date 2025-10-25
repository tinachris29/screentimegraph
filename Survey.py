# Page for data entry that appends to a CSV.
import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Survey", page_icon="📝")

st.title("Data Collection Survey 📝")
st.write("Enter your top 3 most used apps and estimated time spent (hours). Feel free to adapt fields to your schema.")

APP_DIR = Path(__file__).resolve().parents[1]    # points to Lab02/
CSV_PATH = APP_DIR / "data.csv"

with st.form("entry_form", clear_on_submit=True):
    name = st.text_input("Your name")
    app1 = st.text_input("App 1")
    hrs1 = st.number_input("Hours on App 1", min_value=0.0, step=0.1)
    app2 = st.text_input("App 2")
    hrs2 = st.number_input("Hours on App 2", min_value=0.0, step=0.1)
    app3 = st.text_input("App 3")
    hrs3 = st.number_input("Hours on App 3", min_value=0.0, step=0.1)
    submitted = st.form_submit_button("Submit")

if submitted:
    row = {
        "name": name.strip(),
        "app1": app1.strip(),
        "hrs1": float(hrs1),
        "app2": app2.strip(),
        "hrs2": float(hrs2),
        "app3": app3.strip(),
        "hrs3": float(hrs3),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    try:
        if CSV_PATH.exists() and CSV_PATH.stat().st_size > 0:
            df = pd.read_csv(CSV_PATH)
        else:
            df = pd.DataFrame(columns=list(row.keys()))
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
        df.to_csv(CSV_PATH, index=False)
        st.success(f"Saved! CSV at {CSV_PATH.name}")
    except Exception as e:
        st.error(f"Failed to save to CSV: {e}")

st.divider()
st.header("Current Data in CSV")
try:
    if CSV_PATH.exists() and CSV_PATH.stat().st_size > 0:
        st.dataframe(pd.read_csv(CSV_PATH))
    else:
        st.info("CSV not found or empty yet.")
except Exception as e:
    st.error(f"Error reading CSV: {e}")
