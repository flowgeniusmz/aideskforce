import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Set OpenAI Client
client = OpenAI(api_key=st.secrets.openai.api_key)

# 2. Function
def get_assistant_file_dataframe():
    len_dataframe_file = len(st.session_state.dataframe_files)
    print(len_dataframe_file)
    if len_dataframe_file == 0:
        for file_id in st.session_state.assistant_file_ids:
            file_object = client.beta.assistants.files.retrieve(
                file_id=file_id,
                assistant_id=st.session_state.assistant.id
            )
            new_row_files = {
                "File Id": file_object.id,
                "Object Type": file_object.object,
                "Created At": file_object.created_at,
                "Assistant Id": file_object.assistant_id
            }
            st.session_state.dataframe_files = st.session_state.dataframe_files._append(new_row_files, ignore_index=True)
        st.dataframe(st.session_state.dataframe_files, use_container_width=True)
    else:
        st.dataframe(st.session_state.dataframe_files, use_container_width=True)