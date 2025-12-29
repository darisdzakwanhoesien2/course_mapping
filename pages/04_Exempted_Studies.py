import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🚫 Exempted Studies")

db = load_application("application_0001")
exemptions = db["exempted_studies"]

if not exemptions:
    st.info("No exemptions added.")
    st.stop()

rows = []
for e in exemptions:
    rows.append({
        "ID": e["id"],
        "Study": e["study"],
        "Reason": e["reason"],
        "Justification": e["justification"],
        "Complementary Studies": e["complementary_studies"]
    })

df = pd.DataFrame(rows)

st.dataframe(df, use_container_width=True)
