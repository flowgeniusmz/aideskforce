import streamlit as st
import pandas as pd
import csv
from functions import convert_unixtime

def add_message_to_log(varRole: str, varContent: str,  varMessageId: str, varRunId: str, varUnixTime: str):
    message_log_path = st.secrets.streamlit.data_message_log_path
    varDatetime = convert_unixtime.convert_unix_to_datetime(varUnixTime=varUnixTime)
    new_log_row = {
        "Role": varRole,
        "Content": varContent,
        "Thread Id": st.session_state.thread_id,
        "Message Id": varMessageId,
        "Run Id": varRunId,
        "Session Id": st.session_state.session_id,
        "Created At Unix": varUnixTime,
        "Created At Datetime": varDatetime
    }
    with open(file=message_log_path, mode="a", encoding="utf-8") as file:
        fieldnames = list(new_log_row.keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(new_log_row)

