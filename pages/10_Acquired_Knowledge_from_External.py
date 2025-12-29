import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🧠 Acquired Knowledge (from External Programs)")

db = load_application("application_0001")
items = db.get("previously_acquired_knowledge", [])

items = [i for i in items if i.get("source_external_program_id")]

if not items:
    st.info("No acquired knowledge converted from external programs.")
    st.stop()

rows = []
for k in items:
    rows.append({
        "Assessment": k["assessment"],
        "Completion Date": k["date_of_completion"],
        "Justification": k["justification"],
        "Source Program": k["source_external_program_id"]
    })

st.dataframe(pd.DataFrame(rows), use_container_width=True)
