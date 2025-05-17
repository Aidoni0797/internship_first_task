import requests
from bs4 import BeautifulSoup
import sys
sys.stdout.reconfigure(encoding='utf-8')

base_url = "https://parsinger.ru/html/index3_page_{}.html"
result = []

for page in range(1, 5):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('a', class_='name_item')
    titles = [item.text for item in items]
    result.append(titles)

print(result)