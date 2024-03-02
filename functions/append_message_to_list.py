import streamlit as st
from functions import convert_unixtime

def append_message_session_state(varRole: str, varContent: str, varMessageId: str, varRunId: str, varUnixTime: str):
    varDatetime = convert_unixtime.convert_unix_to_datetime(varUnixTime=varUnixTime)
    message_to_append = {"role": varRole, "content": varContent, "messageid": varMessageId, "runid": varRunId, "createdatunix": varUnixTime, "createdatdatetime": varDatetime}
    st.session_state.messages.append(message_to_append)

