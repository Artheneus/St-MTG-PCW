#library import
import streamlit as st

#css import
import apps.load_local_css as lcs

class login:
    def login_form():
        lcss = lcs.load_css
        lcss.local_load('style/style.css')
        st.write("Login Text")
        login_click = st.button("Login") 
        if login_click:
            user_val = st.text_input("Username")
            pw_val = st.text_input("Password")
        pass

    def signup():
        st.write("Sign Up Text")
        regist_click = st.button("Sign Up") 
        if regist_click:
            user_val = st.text_input("Username")
            pw_val = st.text_input("Password")
        pass