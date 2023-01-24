import streamlit as st

#css import
import apps.load_local_css as lcs

class home:
    def home_main():
        lcss = lcs.load_css
        lcss.local_load('style/style.css')
        st.title("Magic the Gathering Price Comparison Website")
        st.subheader("the fastest way to compare your Magic the Gathering cards through 3 biggest marketplace")