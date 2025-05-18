import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/2/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Находим все строки таблицы, кроме заголовка
rows = soup.find_all('tr')[1:]  # пропускаем первую строку с заголовками

# Суммируем значения из первого столбца каждой строки
total = sum(float(row.find_all('td')[0].text) for row in rows)

print(total)
