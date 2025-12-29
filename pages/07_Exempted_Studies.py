import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🚫 Exempted Studies")

db = load_application("application_0001")
items = db.get("exempted_studies", [])

if not items:
    st.info("No exempted studies.")
    st.stop()

rows = []
for e in items:
    rows.append({
        "Study": e.get("study", ""),
        "Reason": e.get("reason", ""),
        "Justification": e.get("justification", ""),
        "Complementary Studies": e.get("complementary_studies", ""),
        "Handler": e.get("handler", ""),
        "Attachments": ", ".join(e.get("attachments", []))
    })

df = pd.DataFrame(rows)
st.dataframe(df, use_container_width=True)


# import streamlit as st
# import pandas as pd
# from utils.json_db import load_application

# st.set_page_config(layout="wide")
# st.title("🚫 Exempted Studies")

# db = load_application("application_0001")
# items = db.get("exempted_studies", [])

# if not items:
#     st.info("No exempted studies.")
#     st.stop()

# rows = []
# for e in items:
#     rows.append({
#         "Study": e["study"],
#         "Reason": e["reason"],
#         "Justification": e["justification"],
#         "Complementary Studies": e["complementary_studies"],
#         "Handler": e["handler"],
#         "Attachments": ", ".join(a["filename"] for a in e["attachments"])
#     })

# df = pd.DataFrame(rows)
# st.dataframe(df, use_container_width=True)
