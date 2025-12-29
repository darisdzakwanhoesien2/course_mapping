import streamlit as st
import pandas as pd
import uuid
from utils.json_db import load_application, save_application
from utils.table_editors import list_to_csv, csv_to_list

APP_ID = "application_0001"
st.set_page_config(layout="wide")
st.title("✏️ Previously Acquired Knowledge")

db = load_application(APP_ID)
items = db.get("previously_acquired_knowledge", [])

df = pd.DataFrame([
    {
        "id": k.get("id", ""),
        "assessment": k.get("assessment", ""),
        "date_of_completion": k.get("date_of_completion", ""),
        "justification": k.get("justification", ""),
        "attachments": list_to_csv(k.get("attachments", []))
    }
    for k in items
])

if df.empty:
    df = pd.DataFrame([{
        "id": "", "assessment": "",
        "date_of_completion": "", "justification": "",
        "attachments": ""
    }])

edited_df = st.data_editor(
    df.astype(str),
    num_rows="dynamic",
    use_container_width=True,
    key="acquired_knowledge_editor"
)

if st.button("💾 Save acquired knowledge"):
    new_items = []

    for _, r in edited_df.iterrows():
        if not r["assessment"]:
            continue

        new_items.append({
            "id": r["id"] or f"pak_{uuid.uuid4().hex[:6]}",
            "assessment": r["assessment"],
            "date_of_completion": r["date_of_completion"],
            "justification": r["justification"],
            "places_of_performance": [],
            "attachments": [{"filename": f} for f in csv_to_list(r["attachments"])]
        })

    db["previously_acquired_knowledge"] = new_items
    save_application(APP_ID, db)
    st.success("✅ Previously acquired knowledge saved")
