import streamlit as st
from functions import convert_unixtime
import warnings

def append_message_dataframe(varRole: str, varContent: str, varMessageId: str, varRunId: str, varUnixTime: str):
    varDatetime = convert_unixtime.convert_unix_to_datetime(varUnixTime=varUnixTime)
    new_dataframe_row = {
        "Role": varRole,
        "Content": varContent,
        "Thread Id": st.session_state.thread_id,
        "Message Id": varMessageId,
        "Run Id": varRunId,
        "Session Id": st.session_state.session_id,
        "Created At Unix": varUnixTime,
        "Created At Datetime": varDatetime
    }
    with warnings.catch_warnings():
        warnings.simplefilter(action='ignore', category=FutureWarning)
        st.session_state.dataframe_messages._append(new_dataframe_row, ignore_index=True)