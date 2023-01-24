import streamlit as st

#css import
import apps.load_local_css as lcs

class about:
    def write_about():
        lcss = lcs.load_css
        lcss.local_load('style/style.css')
        st.header("About the Maker")