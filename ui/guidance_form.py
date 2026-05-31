import streamlit as st
from datetime import date


def guidance_form(db: dict) -> None:
    """Render the guidance discussion fields."""
    g = db.get("guidance_discussion", {})
    db["guidance_discussion"] = g

    # If a date already exists in the JSON, show it as the default.
    default_date = None
    if g.get("date"):
        try:
            default_date = date.fromisoformat(g["date"])
        except ValueError:
            default_date = None

    g["date"] = str(st.date_input("Guidance discussion date", value=default_date))
    g["advisor"] = st.text_input("Advisor", g.get("advisor", ""))
