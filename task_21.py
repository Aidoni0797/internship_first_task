import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://parsinger.ru/html/"
start_url = base_url + "index1_page_1.html"

# Заголовки для CSV
headers = [
    "Наименование", "Артикул", "Бренд", "Модель", "Тип", "Технология экрана",
    "Материал корпуса", "Материал браслета", "Размер", "Сайт производителя",
    "Наличие", "Цена", "Старая цена", "Ссылка на карточку с товаром"
]

# Получаем ссылки на все страницы в категории "watch"
response = requests.get(start_url)
soup = BeautifulSoup(response.text, 'html.parser')
page_links = [base_url + a['href'] for a in soup.select('.pagen a')]

# Получаем все ссылки на карточки товаров
product_links = []

for page_url in page_links:
    r = requests.get(page_url)
    s = BeautifulSoup(r.text, 'html.parser')
    product_links += [base_url + x['href'] for x in s.select('.name_item')]

data = []

# Обрабатываем каждую карточку
for url in product_links:
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')

    name = s.find('p', id='p_header').text.strip()
    article = s.find('p', class_='article').text.replace('Артикул: ', '').strip()
    availability = s.find('span', id='in_stock').text.replace('В наличии: ', '').strip()
    price = s.find('span', id='price').text.strip().replace(' руб', '')
    old_price = s.find('span', id='old_price').text.strip().replace(' руб', '')
    table = s.find_all('li')

    specs = [li.text.split(': ')[1] for li in table]  # 9 характеристик
    row = [name, article] + specs + [availability, price, old_price, url]
    data.append(row)

# Сохраняем в CSV
with open('watch_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print("watch_data.csv")
