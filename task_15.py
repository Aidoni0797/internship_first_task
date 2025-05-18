import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/5/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Получаем заголовки таблицы
headers = [th.text for th in soup.find_all('th')]

# Инициализируем словарь с нулями
column_sums = {header: 0.0 for header in headers}

# Получаем все строки таблицы, кроме заголовка
rows = soup.find_all('tr')[1:]

for row in rows:
    cells = row.find_all('td')
    for i, cell in enumerate(cells):
        value = float(cell.text)
        column_sums[headers[i]] += value

# Округляем значения до 3 знаков после запятой
rounded_sums = {key: round(value, 3) for key, value in column_sums.items()}

print(rounded_sums)
