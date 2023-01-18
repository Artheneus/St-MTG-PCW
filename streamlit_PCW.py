from click import option, style
import streamlit as st
import requests
from googlesearch import search
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup
import hydralit_components as hc

st.set_page_config(layout='wide',initial_sidebar_state='collapsed')

#Home Page
def Home():
    st.title("Magic the Gathering Price Comparison Website")
    st.write("the fastest way to compare your Magic the Gathering cards through 3 biggest marketplace")

#Searching Page
def searching():
    SCG = []
    CK = []
    st.header("Search your cards !")

    # try:
    #     from googlesearch import search
    # except ImportError:
    #     print("No Module Named 'google' found")
    with st.container():
            query = st.text_input(" ", "Input your card name ", key="placeholder")
            st.button("Search")

    for a in search(query, tld='com', num=20, stop=20, pause=4):
        if 'starcitygames.com' in a:
            SCG.append(a)
            # st.write(SCG)

        if 'cardkingdom.com' in a:
            CK.append(a) 
            # st.write(CK)

    # for i in SCG:
    #     if SCG is not None:
    #         try:
    #             col1, col2 = st.columns(2)
    #             URL = i
    #             headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    #             r = requests.get(URL, headers=headers)
    #             content = r.text
    #             soup = BeautifulSoup(content, 'html.parser')
    #             title = soup.find("title", class_="removeSKU").get_text()
    #             price = soup.find("span", {"class": "price price--withoutTax"}).get_text()

    #             with col1:
    #                 st.write(title)
    #             with col2:
    #                 st.write(price)
            
    #         except:
    #             st.write("Opps!, error occurred. ")

    # for j in CK:
    #     if CK is not None:
    #         try:
    #             col1, col2 = st.columns(2)
    #             URL = j
    #             headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    #             r = requests.get(URL, headers=headers)
    #             content = r.text
    #             soup = BeautifulSoup(content, 'html.parser')
    #             title = soup.find("meta", property="og:title")
    #             price = soup.find("span", {"class": "stylePrice"}).get_text()
    #             with col1:
    #                 st.write(title["content"])
    #             with col2:
    #                 st.write(price)
                
    #         except:
    #             st.write("Opps!, error occurred. ")

#Cardlist Page
def cardList():
    st.header("This is the List where you added to the database")

#About Page
def about():
    st.header("This is where my bio lies")

#Simple Login page
def login():
    user = st.text_input("Username")
    pw = st.text_input("Password")

#signup page
def Sign_Up():
    userName = st.text_input("Username")
    passw = st.text_input("Password")
    email = st.text_input("Email")

#load css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# main execute apps
def main():
    
    local_css("style/style.css")

    # button_login = st.sidebar.button("Login")
    # if button_login == True:
    #     login()

    # with st.sidebar:
    #     selected = option_menu(
    #         "Main Menu", ["Home", 'Settings'], 
    #         icons=['house', 'gear'], menu_icon="cast", default_index=1
            
    #         # menu_title=None,
    #         # options=["Home", "Searching", "Card List", "About"],
    #         # choice = st.sidebar.selectbox("Menu", menu)
    #         # orientation="horizontal"
    #     )
    #     selected

    with st.container():
        with st.sidebar:
            with st.container():
                if st.sidebar.button("Login") == True:
                    login()
            with st.container():
                if st.sidebar.button("Sign Up") == True:
                    Sign_Up()

    # with st.container():
        # with st.sidebar:

selected = option_menu(
                    menu_title=None,
                    options=["Home", "Searching", "Card List", "About", "Login"],
                    icons=["house", "search", "list", "exclamation-circle", "key"],
                    # menu_icon="cast",
                    default_index=0,
                    orientation="horizontal",
                    styles={
                        "container" : {"border-radius" : "20px"},
                        "icon" : {"color" : "", "font-size" : "16px"},
                        "nav-link" : {"color" : "", "font-size" : "16px"},
                        "background" : {"color" : "transparent", "border-radius" : "20px"}
                    }
                )


if selected == "Home":
    Home()

elif selected == "Searching":
    searching()

elif selected == "Card List":
    cardList()

elif selected == "About":
    about()


# hide_footer = st.markdown ("""
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     header {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)

# menu_data = [
#     {'id':'searching', 'label':"Searching"},
#     {'id':'cardlist', 'label':"Card List"},
#     {'id':'about', 'label':"About Me"},
#     {'id':'signup', 'label':"Sign Up"}
# ]

# over_theme = {'txc_inactive': '#FFFFFF'}

# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
#     home_name="Home",
#     login_name="Login",
#     hide_streamlit_markers=True,
#     sticky_nav=True,
#     sticky_mode='pinned'
# )

# if menu_id == "Home":
#     Home()
# if menu_id == "searching":
#     searching()
# if menu_id == "cardlist":
#     cardList()
# if menu_id == "about":
#     about()
# if menu_id == "Login":
#     login()
# if menu_id == "signup":
#     Sign_Up()

if __name__ == '__main__':
     main()

# def main():

#     # title of the web
#     st.title("Magic the Gathering Price Comparison Website")
#     st.write("the fastest way to compare your Magic the Gathering cards through 3 biggest marketplace")

#     menu = ["Home", "Searching", "Card List", "About"]
#     choice = st.sidebar.selectbox("Menu", menu)

#     if choice == "Home":
#         Home()

#     # adding css
    
    
