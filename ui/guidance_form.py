import streamlit as st

def guidance_form(db):
    g = db["guidance_discussion"]

    g["date"] = str(st.date_input(
        "Guidance discussion date",
        value=None if not g.get("date") else None
    ))
    g["advisor"] = st.text_input("Advisor", g.get("advisor", ""))


# import streamlit as st

# def guidance_form():
#     st.subheader("Guidance discussion (optional)")
#     date = st.date_input("Discussion date")
#     advisor = st.text_input("Advisor")
#     return date, advisor