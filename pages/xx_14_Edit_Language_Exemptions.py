import streamlit as st
import pandas as pd
import uuid
from utils.json_db import load_application, save_application
from utils.table_editors import list_to_csv, csv_to_list

APP_ID = "application_0001"
st.set_page_config(layout="wide")
st.title("✏️ Language Study Exemptions")

db = load_application(APP_ID)
items = db.get("exempted_studies", [])

df = pd.DataFrame([
    {
        "id": e.get("id", ""),
        "study": e.get("study", ""),
        "reason": e.get("reason", ""),
        "justification": e.get("justification", ""),
        "complementary_studies": e.get("complementary_studies", ""),
        "handler": e.get("handler", ""),
        "attachments": list_to_csv(e.get("attachments", []))
    }
    for e in items
])

if df.empty:
    df = pd.DataFrame([{
        "id": "", "study": "", "reason": "",
        "justification": "", "complementary_studies": "",
        "handler": "", "attachments": ""
    }])

edited_df = st.data_editor(
    df.astype(str),
    num_rows="dynamic",
    use_container_width=True,
    key="language_exemptions_editor"
)

if st.button("💾 Save language exemptions"):
    new_items = []

    for _, r in edited_df.iterrows():
        if not r["study"]:
            continue

        new_items.append({
            "id": r["id"] or f"ex_{uuid.uuid4().hex[:6]}",
            "study": r["study"],
            "reason": r["reason"],
            "justification": r["justification"],
            "complementary_studies": r["complementary_studies"],
            "handler": r["handler"],
            "attachments": csv_to_list(r["attachments"])
        })

    db["exempted_studies"] = new_items
    save_application(APP_ID, db)
    st.success("✅ Language exemptions saved")
