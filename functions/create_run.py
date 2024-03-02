import streamlit as st
from functions import get_client_openai as client_oai
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)
client1 = client_oai.get_openai_client()

def create_new_run():
    new_run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=st.secrets.openai.assistant_id,
        additional_instructions=st.session_state.run_instructions
    )
    return new_run