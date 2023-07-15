import requests
from bs4 import BeautifulSoup
import json

# page = requests.get("https://https://informburo.kz/").text
# with open('site.html', 'w', encoding='utf-8') as file:
#     file.write(page)

with open('site.html', 'r', encoding='utf-8') as file:
    page = file.read()

data = {}

soup = BeautifulSoup(page, 'lxml')
same_blocks = soup.find_all(class_='uk-overlay-primary')
for block in same_blocks:
    tag = block.find_parent('a')
    if tag.find('img') is not None:
        href = tag.get('href')
        description = tag.find('img').get('alt')
        data[description] = href

other_tags = soup.find_all(class_='uk-nav uk-nav-default')[0]
for lii in other_tags:
    tag_a = lii.find('a')
    if not tag_a == -1 and tag_a.find('time') is not None:
        href = tag_a.get('href')
        time = tag_a.find('time').text
        description = tag_a.text.split('\n')[2]
        hashtag = tag_a.text.split('\n')[3]
        data[description] = {'Ссылка': href, 'Время': time, 'Хэштег': hashtag}


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
