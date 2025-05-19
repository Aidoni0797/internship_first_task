import requests
from bs4 import BeautifulSoup
import json
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')
BASE_URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index3_page_1.html'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

all_products = []

# Получаем ссылки на все страницы категории
response = requests.get(START_URL, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
pages = [BASE_URL + a['href'] for a in soup.select('.pagen a')]

# Проходим по всем страницам
for page_url in pages:
    page_resp = requests.get(page_url, headers=HEADERS)
    page_soup = BeautifulSoup(page_resp.text, 'html.parser')

    # Получаем ссылки на карточки товаров
    card_links = [BASE_URL + a['href'] for a in page_soup.select('.name_item')]

    # Переходим на каждую карточку
    for card_url in card_links:
        card_resp = requests.get(card_url, headers=HEADERS)
        card_soup = BeautifulSoup(card_resp.text, 'html.parser')

        name = card_soup.find('p', id='p_header').text.strip()
        price = card_soup.find('span', id='price').text.strip()
        stock = card_soup.find('span', id='in_stock').text.strip()

        # Автоматически собираем характеристики
        description = {}
        for li in card_soup.select('ul.description li'):
            if ':' in li.text:
                key, value = li.text.split(':', 1)
                description[key.strip()] = value.strip()

        product_data = {
            'name': name,
            'price': price,
            'stock': stock,
            'description': description,
            'url': card_url
        }
        all_products.append(product_data)

        time.sleep(0.2)  # чтобы не спамить сервер

# Сохраняем результат
with open('category3_products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, indent=4, ensure_ascii=False)

print(f'Собрано товаров: {len(all_products)}')
