import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Set OpenAI Client
client = OpenAI(api_key=st.secrets.openai.api_key)

# 2. Function
def get_assistant_tools_dataframe():
    len_tools_dataframe = len(st.session_state.dataframe_tools)
    if len_tools_dataframe == 0:
        for tool in st.session_state.assistant_tools:
            new_row_tools = {
                "Type": tool.type
            }
            st.session_state.dataframe_tools = st.session_state.dataframe_tools._append(new_row_tools, ignore_index=True)
        st.dataframe(st.session_state.dataframe_tools, use_container_width=True)
    else:
        st.dataframe(st.session_state.dataframe_tools, use_container_width=True)