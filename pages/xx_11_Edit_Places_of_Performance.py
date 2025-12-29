import streamlit as st
import pandas as pd
import uuid
from utils.json_db import load_application, save_application
from utils.table_editors import list_to_csv, csv_to_list

APP_ID = "application_0001"
st.set_page_config(layout="wide")
st.title("✏️ Places of Performance")

# -----------------------
# Load DB once
# -----------------------
db = load_application(APP_ID)
places = db.get("places_of_performance", [])

# -----------------------
# Build initial DataFrame
# -----------------------
df = pd.DataFrame([
    {
        "id": p.get("id", ""),
        "option": p.get("type", ""),
        "performance_type": p.get("place_type", ""),
        "place_name": p.get("place_name", ""),
        "description": p.get("description", ""),
        "knowledge_vs_objectives": p.get("learning_outcomes", ""),
        "attachments": list_to_csv(p.get("attachments", []))
    }
    for p in places
])

if df.empty:
    df = pd.DataFrame([{
        "id": "", "option": "", "performance_type": "",
        "place_name": "", "description": "",
        "knowledge_vs_objectives": "", "attachments": ""
    }])

# -----------------------
# Data editor (KEY IS CRITICAL)
# -----------------------
edited_df = st.data_editor(
    df.astype(str),
    num_rows="dynamic",
    use_container_width=True,
    key="places_editor"   # 🔑 REQUIRED
)

# -----------------------
# Save back to JSON
# -----------------------
if st.button("💾 Save changes"):
    saved_rows = []

    for _, row in edited_df.iterrows():
        if not row["place_name"]:
            continue

        saved_rows.append({
            "id": row["id"] or f"place_{uuid.uuid4().hex[:6]}",
            "type": row["option"],
            "place_type": row["performance_type"],
            "place_name": row["place_name"],
            "job_title": {"fi": "", "en": ""},
            "description": row["description"],
            "learning_outcomes": row["knowledge_vs_objectives"],
            "attachments": csv_to_list(row["attachments"])
        })

    db["places_of_performance"] = saved_rows
    save_application(APP_ID, db)

    st.success("✅ Places of performance saved")
