import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = 'https://parsinger.ru/html/'
CATEGORY_URL_TEMPLATE = 'https://parsinger.ru/html/index{}_page_1.html'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

all_products = []

# Проходим по всем 5 категориям
for category_index in range(1, 6):
    category_url = CATEGORY_URL_TEMPLATE.format(category_index)
    category_resp = requests.get(category_url, headers=HEADERS)
    category_soup = BeautifulSoup(category_resp.text, 'html.parser')

    # Получаем все страницы внутри категории
    page_links = [BASE_URL + a['href'] for a in category_soup.select('.pagen a')]

    for page_url in page_links:
        page_resp = requests.get(page_url, headers=HEADERS)
        page_soup = BeautifulSoup(page_resp.text, 'html.parser')

        # Ссылки на карточки товаров
        card_links = [BASE_URL + a['href'] for a in page_soup.select('.name_item')]

        for card_url in card_links:
            card_resp = requests.get(card_url, headers=HEADERS)
            card_soup = BeautifulSoup(card_resp.text, 'html.parser')

            name = card_soup.find('p', id='p_header').text.strip()
            price = card_soup.find('span', id='price').text.strip()
            stock = card_soup.find('span', id='in_stock').text.strip()

            # Автоматическое извлечение характеристик
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

            time.sleep(0.1)  # вежливое ожидание

# Сохраняем в JSON
with open('all_categories_products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, indent=4, ensure_ascii=False)

print(f'Собрано товаров: {len(all_products)}')
