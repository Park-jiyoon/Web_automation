import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

td_tags = soup.select('td')[:4]

for tag in td_tags:
    print(tag.get_text())