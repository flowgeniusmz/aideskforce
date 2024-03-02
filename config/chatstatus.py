import streamlit as st


def chatstatus_start():
    chat_status = st.status(
        label="Initiating response...",
        expanded=False,
        state="running"
    )
    return chat_status

def chatstatus_end(varChatstatus):
    varChatstatus.update(
            label="Response recieved!",
            expanded=False,
            state="complete"
        )
    
