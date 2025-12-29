import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("📘 Previously Completed Studies")

db = load_application("application_0001")
studies = db.get("previous_studies", [])

places_lookup = {
    p["id"]: p.get("place_name", p["id"])
    for p in db.get("places_of_performance", [])
}

if not studies:
    st.info("No previously completed studies.")
    st.stop()

rows = []
for s in studies:
    rows.append({
        "Credit Transfer Type": s.get("credit_transfer_type", ""),
        "Course Code": s.get("course_code", ""),
        "Name": s.get("name", ""),
        "Credits": s.get("credits", ""),
        "Credit Type": s.get("credit_type", ""),
        "Language": s.get("language", ""),
        "Assessment": s.get("assessment", ""),
        "Places of Performance": ", ".join(
            places_lookup.get(pid, pid)
            for pid in s.get("places_of_performance", [])
        ),
        "Completion Date": s.get("date_of_completion", ""),
        "Justification": s.get("justification", ""),
        "Attachments": ", ".join(
            a.get("filename", str(a))
            for a in s.get("attachments", [])
        )
    })

df = pd.DataFrame(rows).astype(str)
st.dataframe(df, use_container_width=True)


# import streamlit as st
# import pandas as pd
# from utils.json_db import load_application

# st.set_page_config(layout="wide")
# st.title("📘 Previously Completed Studies")

# db = load_application("application_0001")
# items = db.get("previous_studies", [])

# if not items:
#     st.info("No previously completed studies.")
#     st.stop()

# rows = []
# for s in items:
#     rows.append({
#         "Course Code": s["course_code"],
#         "Name (Original)": s["name"]["original"],
#         "Name (EN)": s["name"]["english"],
#         "Credits": s["credits"]["value"],
#         "Credit Type": s["credits"]["type"],
#         "Language": s["language_of_instruction"],
#         "Assessment": s["assessment"],
#         "Completion Date": s["date_of_completion"],
#         "Justification": s["justification"]
#     })

# df = pd.DataFrame(rows)
# st.dataframe(df, use_container_width=True)
