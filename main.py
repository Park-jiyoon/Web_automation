import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('td') # * 태그 사용 가능


for tag in td_tags:
    print(tag.get_text())