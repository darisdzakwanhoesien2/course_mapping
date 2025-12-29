import streamlit as st
from utils.json_db import load_application, save_application

from ui.applicant_form import applicant_form
from ui.guidance_form import guidance_form
from ui.place_of_performance import place_of_performance_form
from ui.acquired_knowledge import acquired_knowledge_form
from ui.exempted_study import exempted_study_form

st.set_page_config(layout="wide")
st.title("🎓 Recognition of Prior Learning (JSON-based)")

APP_ID = "application_0001"

if "db" not in st.session_state:
    st.session_state.db = load_application(APP_ID)

db = st.session_state.db

# =========================
# Applicant
# =========================
with st.expander("👤 Applicant information", expanded=True):
    applicant_form(db)

# =========================
# Guidance
# =========================
with st.expander("🧭 Guidance discussion"):
    guidance_form(db)

# =========================
# Places of performance
# =========================
with st.expander("🏢 Places of performance"):
    place_of_performance_form(db)

# =========================
# Acquired knowledge
# =========================
with st.expander("🧠 Previously acquired knowledge"):
    acquired_knowledge_form(db)

# =========================
# Exemptions
# =========================
with st.expander("🚫 Exempted studies (language)"):
    exempted_study_form(db)

# =========================
# Save
# =========================
st.divider()
if st.button("💾 Save application"):
    save_application(APP_ID, db)
    st.success("Application saved to JSON")


# import streamlit as st
# from ui.applicant_form import applicant_form
# from ui.guidance_form import guidance_form
# from ui.place_of_performance import place_of_performance_form
# from ui.previous_studies import previous_study_form
# from models import create_application

# st.set_page_config(layout="wide")
# st.title("🎓 Recognition of Prior Learning")

# with st.expander("Basic information", expanded=True):
#     applicant = applicant_form()

# with st.expander("Guidance discussion"):
#     guidance = guidance_form()

# with st.expander("Places of performance"):
#     place = place_of_performance_form()

# with st.expander("Previously completed studies"):
#     prev = previous_study_form()

# with st.expander("Additional information"):
#     additional = st.text_area("Additional information")

# if st.button("Save draft"):
#     app_id = create_application(applicant)
#     st.success(f"Application saved (ID: {app_id})")