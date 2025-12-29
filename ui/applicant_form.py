import streamlit as st

def applicant_form(db):
    a = db["applicant"]

    a["name"] = st.text_input("Name", a.get("name", ""))
    a["student_id"] = st.text_input("Student ID", a.get("student_id", ""))
    a["email"] = st.text_input("Email", a.get("email", ""))
    a["degree_program"] = st.text_input("Degree program", a.get("degree_program", ""))
    a["office"] = st.text_input("Office", a.get("office", ""))
    a["arrival_group"] = st.text_input("Arrival group", a.get("arrival_group", ""))
    a["specialisation_option"] = st.text_input(
        "Specialisation option", a.get("specialisation_option", "")
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        a["degree_scope"] = st.number_input("Degree scope", value=a.get("degree_scope", 120))
    with col2:
        a["completed_credits"] = st.number_input(
            "Completed credits", value=a.get("completed_credits", 0)
        )
    with col3:
        a["performance_scope"] = st.number_input(
            "Performance scope", value=a.get("performance_scope", 0)
        )

    a["start_date"] = str(st.date_input("Start date"))
    a["end_date"] = str(st.date_input("End date"))


# import streamlit as st

# def applicant_form():
#     st.subheader("Applicant information")

#     return (
#         st.text_input("Name"),
#         st.text_input("Student ID"),
#         st.text_input("Email"),
#         st.text_input("Degree program"),
#         st.text_input("Office"),
#         st.text_input("Arrival group"),
#         st.text_input("Specialisation option"),
#         st.number_input("Degree scope (ECTS)", 0.0),
#         st.number_input("Completed credits", 0.0),
#         st.number_input("Performance scope", 0.0),
#         st.date_input("Start date"),
#         st.date_input("End date")
#     )