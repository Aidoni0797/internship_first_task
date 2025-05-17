import re
import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

total = 0
base_url = "https://parsinger.ru/html/index3_page_{}.html"

for page in range(1, 5):
    response = requests.get(base_url.format(page))
    soup = BeautifulSoup(response.text, 'lxml')
    links = [f"https://parsinger.ru/html/{a['href']}" for a in soup.find_all('a', class_='name_item')]

    for link in links:
        product_resp = requests.get(link)
        product_soup = BeautifulSoup(product_resp.text, 'lxml')
        article_text = product_soup.find('p', class_='article').text
        article_number = int(re.search(r'\d+', article_text).group())
        total += article_number

print("Сумма артикулов:", total)
