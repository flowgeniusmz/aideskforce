import streamlit as st
from config import pagesetup as ps

# 0. Page Config
ps.get_st_page_config()


# 1. Page Title
ps.get_assistant_title(3)

# 2. Page Overview
ps.get_overview(3)

# 3. Page Warning

st.info(
    body="**IN PROGRESS: Actions Panel In Development:** The **Actions Panel** is currently under construction and unavailable. More information will be posted as it is available!",
            icon="⚠️"
)
