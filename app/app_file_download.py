import streamlit as st
import pandas as pd
from openai import OpenAI

# 1. Set OpenAI Client
client = OpenAI(api_key=st.secrets.openai.api_key)

# 2. Function
def get_file_download_dataframe():
    len_dataframe_files1 = len(st.session_state.dataframe_files1)
    print(len_dataframe_files1)
    if len_dataframe_files1 == 0:
        for file_id in st.session_state.assistant_file_ids:
            file_object = client.files.retrieve(
                file_id=file_id
            )
            #file_contents = client.files.content(
                #file_id=file_id
            #)
            #file_link = download_file_link(
            #    file_contents=file_contents,
            #    file_name=file_object1.filename,
            #    link_text="Download Link"
            #)
            new_row_files1 = {
                "Id": file_object.id,
                "Object": file_object.object,
                "Bytes": file_object.bytes,
                "Created At": file_object.created_at,
                "Name": file_object.filename ,
                "Purpose": file_object.purpose,
                #"Download Link": file_link
            }
            st.session_state.dataframe_files1 = st.session_state.dataframe_files1._append(new_row_files1, ignore_index=True)
        st.dataframe(st.session_state.dataframe_files1, use_container_width=True)
    else:
        st.dataframe(st.session_state.dataframe_files1, use_container_width=True)