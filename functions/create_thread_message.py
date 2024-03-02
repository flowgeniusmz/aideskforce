import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def create_new_thread_message(varThreadId: str, varRole: str, varContent: str):
    new_thread_message = client.beta.threads.messages.create(
        thread_id=varThreadId,
        role=varRole,
        content=varContent
    )
    return new_thread_message