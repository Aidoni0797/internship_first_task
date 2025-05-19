import requests
from bs4 import BeautifulSoup
import json
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

BASE_CATEGORY_URL = "https://parsinger.ru/html/index{}_page_{}.html"
MAX_PAGES_PER_CATEGORY = 4  # Известно, что максимум 4 страницы на категорию
CATEGORY_COUNT = 5  # index1 to index5

all_products = []

for category_index in range(1, CATEGORY_COUNT + 1):
    for page in range(1, MAX_PAGES_PER_CATEGORY + 1):
        url = BASE_CATEGORY_URL.format(category_index, page)
        response = requests.get(url, headers=HEADERS)

        # Если ответ не 200 (например, страница не существует) — пропускаем
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='item')

        for card in cards:
            name = card.find('a', class_='name_item').text.strip()
            description = [li.text.strip() for li in card.find_all('li')]
            price = card.find('p', class_='price').text.strip()
            stock_tag = card.find('span', id=lambda x: x and x.startswith('in_stock'))
            stock = stock_tag.text.strip() if stock_tag else "Нет данных"

            product_data = {
                'name': name,
                'description': description,
                'price': price,
                'stock': stock,
                'category': f'Категория {category_index}',
                'url': url
            }
            all_products.append(product_data)

        time.sleep(0.3)  # чтобы не перегружать сервер

# Сохраняем всё в JSON
with open('all_products.json', 'w', encoding='utf-8') as file:
    json.dump(all_products, file, indent=4, ensure_ascii=False)

print(f'Собрано товаров: {len(all_products)}')
