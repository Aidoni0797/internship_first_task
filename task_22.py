import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://parsinger.ru/html/index1_page_{}.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
all_products = []

# Проходим по всем 4 страницам категории "Компьютеры"
for page in range(1, 5):
    url = BASE_URL.format(page)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', class_='item')

    for card in cards:
        name = card.find('a', class_='name_item').text.strip()
        description = [i.text.strip() for i in card.find_all('li')]
        price = card.find('p', class_='price').text.strip()

        stock_tag = card.find('span', id=lambda x: x and x.startswith('in_stock'))
        stock = stock_tag.text.strip() if stock_tag else 'Нет данных'

        product_data = {
            'name': name,
            'description': description,
            'price': price,
            'stock': stock
        }
        all_products.append(product_data)

    time.sleep(0.5)  # уважительно к серверу

# Сохраняем результат в JSON файл
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(all_products, f, indent=4, ensure_ascii=False)
