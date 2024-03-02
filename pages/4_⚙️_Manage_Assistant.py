import streamlit as st
from config import pagesetup as ps
from app import app_chat_history, app_assistant_files, app_file_download, app_assistant_tools, app_message_log, app_add_assistant_file, app_update_instructions

# 0. Page Config
ps.get_st_page_config()


# 1. Page Title
ps.get_assistant_title(4)

# 2. Page Overview
ps.get_overview(4)

# 3. Set  Containers
main_container = st.container(border=True)
with main_container:
    ps.get_blue_header("Basic Information")
    details_container = st.container()
    ps.get_blue_header("Detailed Information")
    tabs_container = st.container(border=True)

# 4. Details Container
with details_container:
    cc_details = st.columns(3)
    with cc_details[0]:
        asst_name = st.text_input(
            label="Assistant Name",
            value=st.session_state.assistant_name,
            disabled=True
        )
    with cc_details[1]:
        asst_model = st.text_input(
            label="Assistant Model",
            value=st.session_state.assistant_model,
            disabled=True
        )
    with cc_details[2]:
        asst_desc = st.text_input(
            label="Assistant Description",
            value=st.session_state.assistant_description,
            disabled=True
        )
    asst_inst = st.text_area(
        label="Assistant Instructions", 
        value=st.session_state.assistant_instructions,
        disabled=True,
        height=400 
    )

# 5. Tabs Container
tab_names = ['Assistant Files', 'Tools', 'File Download', 'Message Log', 'Add Assistant File', 'Chat History', 'Update Assistant Instructions']
with tabs_container:
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(tabs=tab_names)
    with tab1:
        ps.set_gray_header("Assistant Files")
        exp_about_1 = st.expander(label="About", expanded=False)
        with exp_about_1:
            st.markdown("View assistant files. Not downloadable.")
        app_assistant_files.get_assistant_file_dataframe()
    with tab2:
        ps.set_gray_header("Tool List")
        exp_about_2 = st.expander(label="About", expanded=False)
        with exp_about_2:
            st.markdown("View assistant tools.")
        app_assistant_tools.get_assistant_tools_dataframe()
    with tab3:
        ps.set_gray_header("Downloadable Files")
        exp_about_3 = st.expander(label="About", expanded=False)
        with exp_about_3:
            st.markdown("View downloadable files.")
        app_file_download.get_file_download_dataframe()
    with tab4:
        ps.set_gray_header("Message Log")
        exp_about_4 = st.expander(label="About", expanded=False)
        with exp_about_4:
            st.markdown("View message log.")
        app_message_log.get_message_log_dataframe()
    with tab5:
        ps.set_gray_header("Add Assistant File")
        exp_about_5 = st.expander(label="About", expanded=False)
        with exp_about_5:
            st.markdown("Add assistant file")
        app_add_assistant_file.add_assistant_file()
    with tab6:
        ps.set_gray_header("Chat History")
        exp_about_6 = st.expander(label="About", expanded=False)
        with exp_about_6:
            st.markdown("View your chat history")
        st.divider()
        app_chat_history.chat_history_display()
    with tab7:
        ps.set_gray_header("Update Assistant Instructions")
        exp_about_7 = st.expander(label="About", expanded=False)
        with exp_about_7:
            st.markdown("Change the assistant instructions.")
        app_update_instructions.update_assistant_instructions()
        
