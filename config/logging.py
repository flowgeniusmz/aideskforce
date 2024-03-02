import streamlit as st
from functions import append_message_to_dataframe, append_message_to_list, log_message

def log_and_append_message(varRole: str, varContent: str, varMessageId: str, varRunId: str, varUnixTime: str):
    # append to st.session_state.messages
    append_message_to_list.append_message_session_state(
        varRole=varRole,
        varContent=varContent,
        varMessageId=varMessageId,
        varRunId=varRunId,
        varUnixTime=varUnixTime
    )

    # append to st.session_state_dataframe_messages
    append_message_to_dataframe.append_message_dataframe(
        varRole=varRole,
        varContent=varContent,
        varMessageId=varMessageId,
        varRunId=varRunId,
        varUnixTime=varUnixTime
    )

    # log message to data/message_log.csv
    log_message.add_message_to_log(
        varRole=varRole,
        varContent=varContent,
        varMessageId=varMessageId,
        varRunId=varRunId,
        varUnixTime=varUnixTime
    )
