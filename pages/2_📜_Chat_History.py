import streamlit as st
from config import pagesetup as ps
from app import app_chat_history as appchat

# 0. Page Config
ps.get_st_page_config()


# 1. Page Title
ps.get_assistant_title(2)

# 2. Page Overview
ps.get_overview(2)

# 3. Display Chat History
appchat.chat_history_display()
