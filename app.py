#Import Library
import streamlit as st
from streamlit_option_menu import option_menu

#Import Class
import apps.home as hm
import apps.searching as sc
import apps.cardlist as cl
import apps.login as lg
import apps.about as ab

#import css
import apps.load_local_css as lcs

st.set_page_config(initial_sidebar_state='collapsed')


with st.sidebar:
    selected = option_menu(
                        menu_title="Main Menu",
                        options=["Home", 'Searching', 'Card List', 'About', 'Login', 'SignUp'],
                        icons=['house', 'search', 'list', 'exclamation-circle', 'key'],
                        menu_icon="cast",
                        default_index=0
                    )
    option = st.selectbox("Login / Sign Up",
    ('Login','Signup'))
if selected == "Home":
    hmt = hm.home
    hmt.home_main()

elif selected == "Searching":
    lcss = lcs.load_css
    lcss.local_load('style/style.css')
    st.header("Search your cards !")
    inpt = st.text_input(label="Search : ", placeholder="Enter your card name",key='text')
    button_click = st.button('search')
    if button_click:
        sct = sc.searching
        sct.write(inpt)

elif selected == "Card List":
    clt = cl.cardlist
    clt.listing()

elif selected == "About":
    abt = ab.about
    abt.write_about()
    pass

elif selected == "Login":
    lgt = lg.login
    lgt.login_form()
    lgt.signup()