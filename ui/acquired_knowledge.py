import streamlit as st
import uuid

def acquired_knowledge_form(db):
    places = db["places_of_performance"]
    knowledge = db["acquired_knowledge"]

    if not places:
        st.warning("Add places of performance first")
        return

    for k in knowledge:
        st.markdown(f"- **{k['credit_transfer_type']}** ({k['assessment']})")

    st.divider()
    st.subheader("Add acquired knowledge")

    credit_type = st.selectbox("Credit transfer type", ["replacement", "inclusion"])
    assessment = st.text_input("Assessment (grade / pass)")
    completion_date = st.date_input("Completion date")
    linked_places = st.multiselect(
        "Linked places",
        options=[p["id"] for p in places],
        format_func=lambda x: next(p["place_name"] for p in places if p["id"] == x)
    )
    justification = st.text_area("Justification")

    if st.button("➕ Add knowledge"):
        knowledge.append({
            "id": f"knowledge_{uuid.uuid4().hex[:6]}",
            "credit_transfer_type": credit_type,
            "handler": "",
            "assessment": assessment,
            "completion_date": str(completion_date),
            "linked_places": linked_places,
            "justification": justification
        })
        st.success("Knowledge added")


# import streamlit as st

# def acquired_knowledge_form(places):
#     st.subheader("Previously acquired knowledge")

#     credit_type = st.selectbox(
#         "Credit transfer type",
#         ["Replacement", "Inclusion"]
#     )

#     handler = st.text_input("Choose handler")

#     st.divider()

#     assessment = st.text_input(
#         "Assessment (full numbers or pass)"
#     )

#     linked_places = st.multiselect(
#         "Places of performance and attachments",
#         options=[p["place_name"] for p in places]
#     )

#     completion_date = st.date_input("Date of completion")

#     justification = st.text_area("Justifications")

#     return {
#         "credit_type": credit_type.lower(),
#         "handler": handler,
#         "assessment": assessment,
#         "linked_places": linked_places,
#         "completion_date": completion_date,
#         "justification": justification
#     }