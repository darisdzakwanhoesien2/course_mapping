import streamlit as st

from ui.acquired_knowledge import acquired_knowledge_form
from ui.applicant_form import applicant_form
from ui.exempted_study import exempted_study_form
from ui.guidance_form import guidance_form
from ui.place_of_performance import place_of_performance_form
from utils.json_db import load_application, save_application

APP_ID = "application_0001"


def main() -> None:
    st.set_page_config(layout="wide")
    st.title("🎓 Recognition of Prior Learning (JSON-based)")

    if "db" not in st.session_state:
        st.session_state.db = load_application(APP_ID)

    db = st.session_state.db

    with st.expander("👤 Applicant information", expanded=True):
        applicant_form(db)

    with st.expander("🧭 Guidance discussion"):
        guidance_form(db)

    with st.expander("🏢 Places of performance"):
        place_of_performance_form(db)

    with st.expander("🧠 Previously acquired knowledge"):
        acquired_knowledge_form(db)

    with st.expander("🚫 Exempted studies (language)"):
        exempted_study_form(db)

    st.divider()
    if st.button("💾 Save application"):
        save_application(APP_ID, db)
        st.success("Application saved to JSON")


if __name__ == "__main__":
    main()
