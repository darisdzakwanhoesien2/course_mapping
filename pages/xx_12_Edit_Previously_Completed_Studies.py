import streamlit as st
import pandas as pd
import uuid
from utils.json_db import load_application, save_application
from utils.table_editors import list_to_csv, csv_to_list

APP_ID = "application_0001"
st.set_page_config(layout="wide")
st.title("✏️ Previously Completed Studies")

db = load_application(APP_ID)
items = db.get("previous_studies", [])

df = pd.DataFrame([
    {
        "id": s.get("id", ""),
        "credit_transfer_type": s.get("credit_transfer_type", ""),
        "course_code": s.get("course_code", ""),
        "name": s.get("name", ""),
        "credits": s.get("credits", ""),
        "credit_type": s.get("credit_type", ""),
        "language": s.get("language", ""),
        "assessment": s.get("assessment", ""),
        "date_of_completion": s.get("date_of_completion", ""),
        "justification": s.get("justification", ""),
        "attachments": list_to_csv(s.get("attachments", []))
    }
    for s in items
])

if df.empty:
    df = pd.DataFrame([{
        "id": "", "credit_transfer_type": "", "course_code": "",
        "name": "", "credits": "", "credit_type": "",
        "language": "", "assessment": "",
        "date_of_completion": "", "justification": "",
        "attachments": ""
    }])

edited_df = st.data_editor(
    df.astype(str),
    num_rows="dynamic",
    use_container_width=True,
    key="completed_studies_editor"
)

if st.button("💾 Save completed studies"):
    new_items = []

    for _, r in edited_df.iterrows():
        if not r["course_code"]:
            continue

        new_items.append({
            "id": r["id"] or f"pcs_{uuid.uuid4().hex[:6]}",
            "credit_transfer_type": r["credit_transfer_type"],
            "course_code": r["course_code"],
            "name": r["name"],
            "credits": r["credits"],
            "credit_type": r["credit_type"],
            "language": r["language"],
            "assessment": r["assessment"],
            "date_of_completion": r["date_of_completion"],
            "justification": r["justification"],
            "attachments": [{"filename": f} for f in csv_to_list(r["attachments"])]
        })

    db["previous_studies"] = new_items
    save_application(APP_ID, db)
    st.success("✅ Previously completed studies saved")
