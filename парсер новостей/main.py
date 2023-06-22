from bs4 import BeautifulSoup

with open('page.html', 'r', encoding='utf-8') as file:
    page = file.read()

soup = BeautifulSoup(page, 'lxml')

soup.find_parent()

same_blocks = soup.find_all(class_='uk-overlay-primary')
# for block in same_blocks:
    

# print(page)