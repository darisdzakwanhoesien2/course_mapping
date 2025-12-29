import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("🧠 Previously Acquired Knowledge")

db = load_application("application_0001")
knowledge = db.get("previously_acquired_knowledge", [])

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
        "Credit Transfer Type": k.get("credit_transfer_type", ""),
        "Completion Date": k.get("date_of_completion", ""),
        "Places of Performance": ", ".join(
            places_lookup.get(pid, pid)
            for pid in k.get("places_of_performance", [])
        ),
        "Justification": k.get("justification", ""),
        "Attachments": ", ".join(
            a.get("filename", str(a))
            for a in k.get("attachments", [])
        )
    })

df = pd.DataFrame(rows).astype(str)
st.dataframe(df, use_container_width=True)


# import streamlit as st
# import pandas as pd
# from utils.json_db import load_application

# st.set_page_config(layout="wide")
# st.title("🧠 Previously Acquired Knowledge")

# db = load_application("application_0001")
# items = db.get("previously_acquired_knowledge", [])

# if not items:
#     st.info("No acquired knowledge entries.")
#     st.stop()

# rows = []
# for k in items:
#     rows.append({
#         "Assessment": k["assessment"],
#         "Completion Date": k["date_of_completion"],
#         "Justification": k["justification"],
#         "Attachments": ", ".join(a["filename"] for a in k["attachments"])
#     })

# df = pd.DataFrame(rows)
# st.dataframe(df, use_container_width=True)
