import streamlit as st
import pandas as pd
from utils.json_db import load_application

st.set_page_config(layout="wide")
st.title("👤 Applicant Overview")

db = load_application("application_0001")

# Applicant info
applicant_df = pd.DataFrame(
    db["applicant"].items(),
    columns=["Field", "Value"]
)

st.subheader("Applicant Information")
st.dataframe(applicant_df, use_container_width=True)

# Guidance
st.subheader("Guidance Discussion")
guidance_df = pd.DataFrame(
    db["guidance_discussion"].items(),
    columns=["Field", "Value"]
)
st.dataframe(guidance_df, use_container_width=True)
