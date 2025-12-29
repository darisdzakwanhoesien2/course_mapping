import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("📘 Completed Studies (from External Programs)")

db = load_application("application_0001")
items = db.get("previous_studies", [])

items = [i for i in items if i.get("source_external_program_id")]

if not items:
    st.info("No completed studies converted from external programs.")
    st.stop()

rows = []
for s in items:
    rows.append({
        "Course Code": s["course_code"],
        "Name": s["name"]["english"],
        "Credits (ECTS)": s["credits"]["value"],
        "Assessment": s["assessment"],
        "Completion Date": s["date_of_completion"],
        "Source Program": s["source_external_program_id"]
    })

st.dataframe(pd.DataFrame(rows), use_container_width=True)
