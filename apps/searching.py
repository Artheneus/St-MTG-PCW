import streamlit as st
import requests
from googlesearch import search
from bs4 import BeautifulSoup

#css import
import apps.load_local_css as lcs

class searching:
    def write(inpt):
        lcss = lcs.load_css
        lcss.local_load('style/style.css')

        SCG = []

        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")


        #searching using loop from google search
        for a in search(inpt, num=15, stop=15, pause=3):
            if 'starcitygames.com' in a:
                SCG.append(a)
                # st.write(SCG)
        
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
                    # sets = soup.find("dd", class_="productView-info-name").get_text()
                    price = soup.find("span", {"class": "price price--withoutTax"}).get_text()
                    # with st.container()
                    # st.write(title + " " + price)
                    st.write(title)
                    # st.write(sets)
                    st.write(price)
                    # with col3:
                    #     st.button("Add")
                    
                except:
                    # print(" Opps!, error occurred. ")
                    st.write("Opps!, error occurred. ")
