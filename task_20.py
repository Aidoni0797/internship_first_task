import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://parsinger.ru/html/"
start_url = base_url + "index1_page_1.html"

# Получаем все ссылки на категории
response = requests.get(start_url)
soup = BeautifulSoup(response.text, 'html.parser')
categories = [base_url + a['href'] for a in soup.select('.nav_menu a')]

all_data = []

# Проходим по каждой категории
for category_url in categories:
    # Узнаем количество страниц в категории
    r = requests.get(category_url)
    s = BeautifulSoup(r.text, 'html.parser')
    pages = [base_url + a['href'] for a in s.select('.pagen a')]

    for page_url in pages:
        resp = requests.get(page_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        items = soup.find_all('div', class_='item')

        for item in items:
            name = item.find('a', class_='name_item').text.strip()
            desc = item.find_all('li')
            brand = desc[0].text.split(': ')[1]
            form_factor = desc[1].text.split(': ')[1]
            capacity = desc[2].text.split(': ')[1]
            buffer = desc[3].text.split(': ')[1]
            price = item.find('p', class_='price').text.strip().replace(' руб', '')

            all_data.append([name, brand, form_factor, capacity, buffer, price])

# Сохраняем в CSV без заголовков
with open('all_products.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_data)

print("all_products.csv")
