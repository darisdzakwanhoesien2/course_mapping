import streamlit as st

def previous_study_form():
    st.subheader("Previously completed study")

    transfer_type = st.selectbox(
        "Credit transfer type",
        ["Replacement", "Inclusion", "Exemption"]
    )

    handler = st.text_input("Handler")
    study_name = st.text_input("Study name")
    credits = st.number_input("Credits", 0.0)
    institution = st.text_input("Institution")
    description = st.text_area("Description")

    return locals()