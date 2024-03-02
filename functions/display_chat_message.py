import streamlit as st

def create_display_chat_message(varRole: str, varContent: str):
    with st.chat_message(name=varRole):
        st.markdown(body=varContent)