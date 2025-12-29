import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🏢 Places of Performance & Attachments")

db = load_application("application_0001")
places = db.get("places_of_performance", [])

if not places:
    st.info("No places of performance added.")
    st.stop()

rows = []
for p in places:
    rows.append({
        "ID": p.get("id", ""),
        "Option": p.get("type", ""),  # education / work / other
        "Performance Type": p.get("place_type", ""),
        "Place of Performance": p.get("place_name", ""),
        "Previous Degree / Exchange / Open Studies": "",
        "Description": p.get("description", ""),
        "Knowledge vs Objectives": p.get("learning_outcomes", ""),
        "Attachments": ", ".join(p.get("attachments", []))
    })

df = pd.DataFrame(rows).astype(str)
st.dataframe(df, use_container_width=True)


# import streamlit as st
# import pandas as pd
# from utils.json_db import load_application

# st.set_page_config(layout="wide")
# st.title("🏢 Places of Performance")

# db = load_application("application_0001")
# places = db["places_of_performance"]

# if not places:
#     st.info("No places of performance added.")
#     st.stop()

# rows = []
# for p in places:
#     rows.append({
#         "ID": p["id"],
#         "Type": p["type"],
#         "Place Name": p["place_name"],
#         "Title (FI)": p["job_title"]["fi"],
#         "Title (EN)": p["job_title"]["en"],
#         "Description": p["description"],
#         "Learning Outcomes": p["learning_outcomes"]
#     })

# df = pd.DataFrame(rows)

# st.dataframe(df, use_container_width=True)
