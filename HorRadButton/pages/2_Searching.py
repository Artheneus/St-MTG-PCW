from cProfile import label
import requests, sys, os
import streamlit as st
from bs4 import BeautifulSoup
from googlesearch import search

st.header("Search your cards !")

with open('style/style.css') as f :
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.header("This is web scraper apps, to compare magic the gathering cards prices")

# try:
#     from googlesearch import search
# except ImportError:
#     print("No module named 'google' found")

# try:
#     from googlesearch import search
# except ImportError:
# #     print("No module named 'google' found ")
# coba = "enn"
SCG = []
CK = []
GF = []
query = st.text_input("Please Input Your Card Name : ")

# for a in search(query, tld='com', num=20, stop=20, pause=4):
#     if 'starcitygames.com' in a:
#         SCG.append(a)
#         # st.write(SCG)

for a in search(query, tld='com', num=15, stop=15, pause=3):
    if 'starcitygames.com' in a:
        SCG.append(a)
    
    if 'cardkingdom.com' in a:
        CK.append(a)
    
    if 'mtggoldfish.com' in a:
        GF.append(a)

for i in SCG:
    if SCG is not None:
        try:
            col1, col2 = st.columns(2)
            URL = i
            headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
            r = requests.get(URL, headers=headers)
            content = r.text
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.find("title", class_="removeSKU").get_text()
            # sets = soup.find("span", {"class": "productView-info-name productView-subtitle"}).get_text()
            price = soup.find("span", {"class": "price price--withoutTax"}).get_text()
            # with st.container()
            with col1:
                st.write(title)
            with col2:
                st.write(price)
            # with col3:
            #     st.button("Add")
            
        except:
            # print(" Opps!, error occurred. ")
            st.write("Opps!, error occurred. ")

for j in CK:
    if CK is not None:
        try:
            col1, col2 = st.columns(2)
            URL = j
            headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
            r = requests.get(URL, headers=headers)
            content = r.text
            soup = BeautifulSoup(content, 'html.parser')
            title = soup.find("meta", property="og:title")
            # sets = soup.find("span", {"class": "productView-info-name productView-subtitle"}).get_text()
            price = soup.find("span", {"class": "stylePrice"}).get_text()
            with col1:
                st.write(title["content"])
            with col2:
                st.write(price)
            # with col3:
            #     st.button("Add")
        except:
            # print(" Opps!, error occurred. ")
            st.write("Opps!, error occurred. ")

# txt1 = st.text_input(
#     "This is a placeholder for input text",
#     "Input a text here",
#     key="placeholder",  
# )

# st.write(txt1)