import requests
from bs4 import BeautifulSoup

urls = "https://starcitygames.com/thing-in-the-ice-sgl-mtg-soi-92a-enf/"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
r = requests.get(urls, headers=headers)
content = r.text

soup = BeautifulSoup(content, 'html.parser')
# judul = soup.find("h3", class_="gatherer-name").get_text()
# harga = soup.find("div", class_="price-box-price").get_text()
sets = soup.find("meta", property="og:title", content=True)
sets2 = sets["content"]
if sets2.find("[SGL-MTG-SOI-92a-ENF]") !=-1:
    print("Foil")
else :
    print("Not Foil")

# judul = soup.find("meta", property="og:title", content=True)
# print(judul["content"] if judul else "No meta title given")
