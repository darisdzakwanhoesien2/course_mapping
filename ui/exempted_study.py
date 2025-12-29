import streamlit as st
import uuid
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def exempted_study_form(db):
    exemptions = db["exempted_studies"]

    reasons = json.loads(
        (BASE_DIR / "data/reference/exemption_reasons.json").read_text()
    )

    st.subheader("Existing exemptions")

    # ✅ markdown does NOT get keys
    for e in exemptions:
        st.markdown(f"- **{e['study']}** ({e['reason']})")

    st.divider()
    st.subheader("Add exemption")

    # ---- UNIQUE FORM ID ----
    form_id = "add_exemption"

    study = st.text_input(
        "Study",
        key=f"{form_id}_study"
    )

    reason = st.selectbox(
        "Reason",
        reasons,
        key=f"{form_id}_reason"
    )

    justification = st.text_area(
        "Justification",
        key=f"{form_id}_justification"
    )

    complementary = st.text_area(
        "Complementary studies",
        key=f"{form_id}_complementary"
    )

    if st.button("➕ Add exemption", key=f"{form_id}_submit"):
        exemptions.append({
            "id": f"exempt_{uuid.uuid4().hex[:6]}",
            "study": study,
            "reason": reason,
            "justification": justification,
            "complementary_studies": complementary,
            "handler": "",
            "attachments": []
        })

        # Reset form fields safely
        st.session_state[f"{form_id}_study"] = ""
        st.session_state[f"{form_id}_justification"] = ""
        st.session_state[f"{form_id}_complementary"] = ""

        st.success("Exemption added")


# import streamlit as st
# import uuid
# import json
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[1]

# def exempted_study_form(db):
#     exemptions = db["exempted_studies"]

#     reasons = json.loads(
#         (BASE_DIR / "data/reference/exemption_reasons.json").read_text()
#     )

#     st.subheader("Existing exemptions")

#     for i, e in enumerate(exemptions):
#         st.markdown(
#             f"- **{e['study']}** ({e['reason']})",
#             key=f"exempt_display_{e['id']}"
#         )

#     st.divider()
#     st.subheader("Add exemption")

#     # ---- UNIQUE FORM ID ----
#     form_id = "add_exemption"

#     study = st.text_input(
#         "Study",
#         key=f"{form_id}_study"
#     )

#     reason = st.selectbox(
#         "Reason",
#         reasons,
#         key=f"{form_id}_reason"
#     )

#     justification = st.text_area(
#         "Justification",
#         key=f"{form_id}_justification"
#     )

#     complementary = st.text_area(
#         "Complementary studies",
#         key=f"{form_id}_complementary"
#     )

#     if st.button("➕ Add exemption", key=f"{form_id}_submit"):
#         exemptions.append({
#             "id": f"exempt_{uuid.uuid4().hex[:6]}",
#             "study": study,
#             "reason": reason,
#             "justification": justification,
#             "complementary_studies": complementary,
#             "handler": "",
#             "attachments": []
#         })

#         # Reset form fields
#         st.session_state[f"{form_id}_study"] = ""
#         st.session_state[f"{form_id}_justification"] = ""
#         st.session_state[f"{form_id}_complementary"] = ""

#         st.success("Exemption added")


# import streamlit as st
# import uuid
# import json
# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parents[1]

# def exempted_study_form(db):
#     exemptions = db["exempted_studies"]

#     reasons = json.loads(
#         (BASE_DIR / "data/reference/exemption_reasons.json").read_text()
#     )

#     for e in exemptions:
#         st.markdown(f"- **{e['study']}** ({e['reason']})")

#     st.divider()
#     st.subheader("Add exemption")

#     study = st.text_input("Study")
#     reason = st.selectbox("Reason", reasons)
#     justification = st.text_area("Justification")
#     complementary = st.text_area("Complementary studies")

#     if st.button("➕ Add exemption"):
#         exemptions.append({
#             "id": f"exempt_{uuid.uuid4().hex[:6]}",
#             "study": study,
#             "reason": reason,
#             "justification": justification,
#             "complementary_studies": complementary,
#             "handler": "",
#             "attachments": []
#         })
#         st.success("Exemption added")


# import streamlit as st

# def exempted_study_form():
#     st.subheader("Apply for exemption (language study)")

#     study = st.selectbox(
#         "Study",
#         ["Choose study", "English B2", "Swedish B1"]
#     )

#     reason = st.selectbox(
#         "Reason for exemption",
#         ["Prior education", "Native language", "Other"]
#     )

#     justification = st.text_area("Justifications")

#     complementary = st.text_area(
#         "Complementary studies (if any)"
#     )

#     handler = st.text_input("Choose handler")

#     attachments = st.file_uploader(
#         "Attachments",
#         accept_multiple_files=True
#     )

#     return locals()