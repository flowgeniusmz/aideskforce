import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Set OpenAI Client
client = OpenAI(api_key=st.secrets.openai.api_key)

# 2. Function
def add_assistant_file():
    uploaded_file = st.file_uploader(
        label="Upload additional assistant file"
    )
    if uploaded_file:
        new_asst_file = client.files.create(
            file=uploaded_file,
            purpose="assistants"
        )
        new_asst_file_id = new_asst_file.id
        add_file_to_asst_response = client.beta.assistants.files.create(
            file_id=new_asst_file_id,
            assistant_id=st.session_state.assistant.id
        )
        check_id = add_file_to_asst_response.id
        if check_id:
            st.success(body="File has been added!")
        else:
            st.error(body="File was not uploaded. Please try again.")