import requests, sys, os
import streamlit as st
from bs4 import BeautifulSoup

st.header("MTG Goldfish Scraper")

with open('style/style.css') as f :
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# urls = "https://www.mtggoldfish.com/price/Shadows+over+Innistrad/Thing+in+the+Ice#online"
# headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
# r = requests.get(urls, headers=headers)
# content = r.text

# col1, col2 = st.columns(2)
# soup = BeautifulSoup(content, 'html.parser')
# judul = soup.find("h3", class_="gatherer-name").get_text()
# sets = soup.find("span", class_="price-card-name-set-name").get_text()
# harga = soup.find("div", class_="price-box-price").get_text()

# with col1:
#     st.write(judul,sets)
# with col2:
#     st.write(harga)

# soup = BeautifulSoup(content, 'html.parser')
# judul = soup.find("h3", class_="gatherer-name").get_text()
# harga = soup.find("div", class_="price-box-price").get_text()
# print(judul.prettify())

# ====================================testing ground====================================

