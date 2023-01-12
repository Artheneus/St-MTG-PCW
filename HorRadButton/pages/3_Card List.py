import streamlit as st

with open('style/style.css') as f :
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("This is the List where you added to the database")
