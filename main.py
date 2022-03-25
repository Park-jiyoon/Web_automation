import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
music_page = response.text

soup = BeautifulSoup(music_page, 'html.parser')

popular_artists = []

for tag in soup.select('ul.popular__order li'):
    popular_artists.append(list(tag.stripped_strings)[1])

print(popular_artists)