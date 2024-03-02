import streamlit as st
from config import pagesetup as ps, toastalerts as ta, sessionstates as ss, logging as log, chatstatus as cs
from functions import convert_unixtime as cu, array_length as al, display_chat_message as dcm, create_thread_message as tm
from openai import OpenAI
import time
from datetime import datetime
import base64

# 0. Page Config
ps.get_st_page_config()


# 0. Set Instances
client = OpenAI(api_key=st.secrets.openai.api_key)

# 0. Check Session State
if "start_chat" not in st.session_state:
    ss.get_initial_session_states()


# 1. Page Title
ps.get_assistant_title(1)

# 2. Page Overview
ps.get_overview(1)

# 3. Create Container to Display Chat Messages
chat_container = st.container(border=True, height=350)

# 4. Display Existing Messages in St.Session_State.Messages (will display initial message if no chat messages entered)
with chat_container:
    for existing_message in st.session_state.messages:
        existing_message_role = existing_message["role"]
        existing_message_content = existing_message["content"]
        with st.chat_message(existing_message_role):
            st.markdown(existing_message_content)

# 5. Set Chat_Input and Await User Input
if prompt := st.chat_input("Enter your question (Ex: A student has their third tardy. What consequences should be considered?)"):

# 6. Display Chat_Input (prompt) in chat container
    prompt_role = "user"
    prompt_content = prompt
    with chat_container:
        dcm.create_display_chat_message(varRole=prompt_role, varContent=prompt_content)

# 7. Set Toast Alert (Start) and Chat Status (Start)
    ta.toast_alert_start("Initiating response...")
    with chat_container:
        status = cs.chatstatus_start()
        

# 8. Create New Thread Message
    new_message = tm.create_new_thread_message(varThreadId=st.session_state.thread_id, varRole=prompt_role, varContent=prompt_content)

# 9. Create New Run
    st.session_state.run = client.beta.threads.runs.create(
        thread_id=st.session_state.thread_id,
        assistant_id=st.secrets.openai.assistant_id,
        additional_instructions=st.session_state.run_instructions
    )

# 10. Create Full Message Object and Append to St.SessionState Messages
    log.log_and_append_message(varRole=prompt_role, varContent=prompt_content, varMessageId=new_message.id, varRunId=st.session_state.run.id, varUnixTime=new_message.created_at)
    prompt_message = {"role": prompt_role, "content": prompt_content, "messageid": new_message.id, "runid": st.session_state.run.id, "createdatunix": new_message.created_at, "createdatdatetime": datetime.utcfromtimestamp(new_message.created_at)}

# 11. Check run status loop until run.status = complete
    while st.session_state.run.status != "completed":
        time.sleep(3)
        st.session_state.run = client.beta.threads.runs.retrieve(
            thread_id=st.session_state.thread_id,
            run_id=st.session_state.run.id
        )

# 12. Toast Alert Update and Status Update During Loop
        ta.toast_alert_waiting("Awaiting response...")
        with chat_container:
            status.write(f"Checking response status...{st.session_state.run.status}")

# 13. Toast Alert Update and Status Update when COMPLETE
    ta.toast_alert_end("Reponse Recieved!")
    with chat_container:
        
        cs.chatstatus_end(status)

# 14. Retrieve Thread Message List
    thread_messages = client.beta.threads.messages.list(
        thread_id=st.session_state.thread_id
    )
    #print(thread_messages)

# 15. Retrieve most recent assistant message by looping through each message in thread_messages and looking for the current run_id and role = "assistant"
    for thread_message in thread_messages:
        if thread_message.run_id == st.session_state.run.id and thread_message.role == "assistant":

# 16. Set Message Values
            thread_message_run_id = thread_message.run_id
            thread_message_role = thread_message.role
            thread_message_id = thread_message.id
            thread_message_unix = thread_message.created_at
            thread_message_datetime = cu.convert_unix_to_datetime(thread_message_unix)
            thread_message_text = thread_message.content[0].text
            thread_message_content = thread_message_text.value
            thread_message_annotations = thread_message_text.annotations
            thread_message_annotations_length = al.get_array_length(thread_message_annotations)
# 17. Get Citations from annotations
            citations = []
            thread_message_content_replace = thread_message_content
            if thread_message_annotations_length > 0:
                for index, annotation in enumerate(thread_message_annotations):
                    thread_message_content_replace = thread_message_content_replace.replace(annotation.text, f' [{index}]')
                    if (file_citation:=getattr(annotation, 'file_citation', None)):
                        cited_file = client.files.retrieve(file_citation.file_id)
                        citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
                    elif (file_path := getattr(annotation, 'file_path', None)):
                        cited_file = client.files.retrieve(file_path.file_id)
                        citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
                        # Note: File download functionality not implemented above for brevity
                thread_message_content_replace += "\n\nCitations:\n" + "\n".join(citations)

# 18. Add Message to St.SessionState Messages
            log.log_and_append_message(varRole=thread_message_role, varContent=thread_message_content_replace, varMessageId=thread_message_id, varRunId=thread_message_run_id, varUnixTime=thread_message_unix)
            response_message = {"role": thread_message_role, "content": thread_message_content_replace, "messageid": thread_message_id, "runid": thread_message_run_id, "createdatunix": thread_message_unix, "createdatdatetime": thread_message_datetime}

#19. Display Assistant Response
            with chat_container:
                dcm.create_display_chat_message(varRole=thread_message_role, varContent=thread_message_content_replace)
