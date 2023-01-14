import streamlit as st
import requests
# from googlesearch import search
from streamlit_option_menu import option_menu
from bs4 import BeautifulSoup

#Home Page
def Home():
    st.title("Magic the Gathering Price Comparison Website")
    st.write("the fastest way to compare your Magic the Gathering cards through 3 biggest marketplace")

#Searching Page
def searching():
    SCG = []
    CK = []
    st.header("Search your cards !")
    
    try:
        from googlesearch import search
    except ImportError:
        print("No Module Named 'google' found")
    
    with st.container():
            query = st.text_input(" ", "Input your card name ", key="placeholder")
            st.button("Search")

    # for a in search(query, tld='com', num=20, stop=20, pause=4):
    #     if 'starcitygames.com' in a:
    #         SCG.append(a)
    #         st.write(SCG)

    #     if 'cardkingdom.com' in a:
    #         CK.append(a) 
    #         st.write(CK)

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

    with st.sidebar:
        with st.container():
            if st.sidebar.button("Login") == True:
                login()
        with st.container():
            if st.sidebar.button("Sign Up") == True:
                Sign_Up()
            
        # with st.container():
        #     selected = option_menu(
        #         menu_title=None,
        #         options=["Home", "Searching", "Card List", "About"],
        #         icons=["house", "search", "list", "exclamation-circle"],
        #         # menu_icon="cast",
        #         default_index=1
        #     )

        

    # if selected == "Home":
    #     Home()

    # elif selected == "Searching":
    #     searching()

    # elif selected == "Card List":
    #     cardList()

    # elif selected == "About":
    #     about()

    



if __name__ == '__main__':
     main()
