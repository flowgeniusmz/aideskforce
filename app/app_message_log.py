import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def get_message_log_dataframe():
    len_message_log = len(st.session_state.dataframe_messages)
    
    for msg in st.session_state.messages:
        if not msg['messageid'] == '0':
            new_row_messages = {
                "Role": msg['role'],
                "Content": msg['content'],
                "Thread Id": st.session_state.thread_id,
                "Message Id": msg['messageid'],
                "Run Id": msg['runid'],
                "Session Id": st.session_state.session_id,
                "Created At Unix": msg['createdatunix'],
                "Created At Datetime": msg['createdatdatetime']
            }
            st.session_state.dataframe_messages = st.session_state.dataframe_messages._append(new_row_messages, ignore_index=True)
    st.dataframe(st.session_state.dataframe_messages, use_container_width=True)
