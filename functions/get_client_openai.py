import streamlit as st
from openai import OpenAI

@st.cache_resource
def get_openai_client():
    client = OpenAI(api_key=st.secrets.openai.api_key)
    return client