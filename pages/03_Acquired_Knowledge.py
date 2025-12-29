import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🧠 Previously Acquired Knowledge")

db = load_application("application_0001")
knowledge = db.get("previously_acquired_knowledge", [])

# Map places (if any exist)
places_lookup = {
    p["id"]: p.get("place_name", p["id"])
    for p in db.get("places_of_performance", [])
}

if not knowledge:
    st.info("No acquired knowledge entries.")
    st.stop()

rows = []
for k in knowledge:
    rows.append({
        "ID": k.get("id", ""),
        "Source Program": k.get("source_external_program_id", ""),
        "Assessment": k.get("assessment", ""),
        "Completion Date": k.get("date_of_completion", ""),
        "Places of Performance": ", ".join(
            places_lookup.get(pid, pid)
            for pid in k.get("places_of_performance", [])
        ),
        "Justification": k.get("justification", ""),
        "Attachments": ", ".join(
            a.get("filename", str(a))
            for a in k.get("attachments", [])
        ),
        "Conversion Type": k.get("conversion_metadata", {}).get("conversion_type", ""),
        "Decision By": k.get("conversion_metadata", {}).get("decision_by", "")
    })

df = pd.DataFrame(rows)

# Ensure Arrow compatibility
df = df.astype(str)

st.dataframe(df, use_container_width=True)

