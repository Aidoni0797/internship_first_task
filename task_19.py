import requests
from bs4 import BeautifulSoup
import csv

# URL шаблон для 4 страниц
base_url = "https://parsinger.ru/html/index4_page_{}.html"
pages = [base_url.format(i) for i in range(1, 5)]

# Заголовки CSV
headers = ["Наименование", "Бренд", "Форм-фактор", "Ёмкость", "Объём буф. памяти", "Цена"]
data = []

# Сбор данных со всех страниц
for url in pages:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='item')

    for item in items:
        name = item.find('a', class_='name_item').text.strip()
        description = item.find_all('li')
        brand = description[0].text.split(': ')[1]
        form_factor = description[1].text.split(': ')[1]
        capacity = description[2].text.split(': ')[1]
        buffer = description[3].text.split(': ')[1]
        price = item.find('p', class_='price').text.strip().replace(' руб', '')

        data.append([name, brand, form_factor, capacity, buffer, price])

# Сохраняем в CSV-файл
with open('hdd_data.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Пишем заголовки
    writer.writerows(data)    # Пишем данные

print("hdd_data.csv")
