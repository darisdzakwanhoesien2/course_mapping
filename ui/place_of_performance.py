import streamlit as st
import uuid

def place_of_performance_form(db):
    places = db["places_of_performance"]

    for p in places:
        st.markdown(f"**{p['place_name']}** ({p['type']})")

    st.divider()
    st.subheader("Add place")

    ptype = st.radio("Type", ["education", "work", "other"])
    place_name = st.text_input("Place / Employer")
    title_fi = st.text_input("Title (FI)")
    title_en = st.text_input("Title (EN)")
    description = st.text_area("Description")
    learning = st.text_area("Learning outcomes")

    if st.button("➕ Add place"):
        places.append({
            "id": f"place_{uuid.uuid4().hex[:6]}",
            "type": ptype,
            "place_type": "",
            "place_name": place_name,
            "job_title": {"fi": title_fi, "en": title_en},
            "description": description,
            "learning_outcomes": learning,
            "attachments": []
        })
        st.success("Place added")


# import streamlit as st

# def place_of_performance_form():
#     st.subheader("Add place of performance")

#     ptype = st.radio(
#         "Type",
#         ["Educational institute", "Work experience", "Other"]
#     )

#     place_type = st.text_input("Place of performance type")
#     place_name = st.text_input("Place / Employer")
#     title_fi = st.text_input("Title (Finnish)")
#     title_en = st.text_input("Title (English)")

#     description = st.text_area("Description")
#     learning = st.text_area("Learning outcomes")

#     return {
#         "type": ptype,
#         "place_type": place_type,
#         "place_name": place_name,
#         "title_fi": title_fi,
#         "title_en": title_en,
#         "description": description,
#         "learning": learning
#     }