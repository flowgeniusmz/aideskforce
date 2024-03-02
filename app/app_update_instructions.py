import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets.openai.api_key)

def update_assistant_instructions():
    current_instructions_value = st.session_state.assistant.instructions
    current_instructions_label = "Current Assistant Instructions"
    update_instructions_toggle_button_label = "Edit Assistant Instructions" 
    st.session_state.update_instructions_toggle_button = False
    update_instructions_toggle_button_value = st.session_state.update_instructions_toggle_button

    toggle_container = st.container(border=True)
    with toggle_container:
        update_instructions_toggle_button = st.toggle(
            label=update_instructions_toggle_button_label, 
            value=st.session_state.update_instructions_toggle_button,
            key="update_toggle_button", 
            disabled=True
            )


        if update_instructions_toggle_button:
            edit_instructions = st.text_area(
                label="Assistant Instructions",
                value=st.session_state.assistant_instructions,
                disabled=False,
                key="edit_instructions_text_area"
            )
            submit_button = st.button(
                label="Submit",
                type="primary"
            )
            if submit_button:
                asst = client.beta.assistants.update(
                    assistant_id=st.secrets.openai.assistant_id,
                    instructions=edit_instructions
                )
                st.session_state.assistant_instructions = client.beta.assistants.retrieve(assistant_id=st.secrets.openai.assistant_id).instructions
                st.success(
                    body="**SUCCESS:** The assistant instructions have been successfully updated!"
                )
        else:
            current_instructions = st.text_area(
                label="Assistant Instructions",
                value=st.session_state.assistant_instructions,
                disabled=True,
                key="current_instructions_text_area"
            )