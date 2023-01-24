import streamlit as st

#css import
import apps.load_local_css as lcs

class cardlist:
    def listing():
        lcss = lcs.load_css
        lcss.local_load('style/style.css')
        st.header("Card Listing")