from click import style
import streamlit as st


with open('style/style.css') as f :
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.header("This is where my bio lies")

# contact_form = """
# <form action="https://formsubmit.co/oagung96@gmail.com" method="POST">
#     <input type="hidden" name="_captcha" value="false">
#     <input type="text" name="name" placeholder="your name" required>
#     <input type="email" name="email" placeholder="your email" required>
#     <textarea name="message" placeholder="Your Message"></textarea>
#     <button type="submit">Send</button>
# </form>
# """
# st.markdown(contact_form, unsafe_allow_html=True)

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style/style.css")