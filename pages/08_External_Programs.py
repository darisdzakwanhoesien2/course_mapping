import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🌍 External Learning Programs")

db = load_application("application_0001")
programs = db.get("external_learning_programs", [])

if not programs:
    st.info("No external programs added.")
    st.stop()

rows = []
for p in programs:
    rows.append({
        "Program": p["program_title"],
        "Platform": p["platform"],
        "Provider": p["provider"]["partner_university"],
        "Completed": p["completion_status"],
        "Completion Date": p["completion_date"],
        "Total Hours": p["total_estimated_hours"],
        "Certificate": "Yes" if p["certificate_issued"] else "No"
    })

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)
