import requests
from bs4 import BeautifulSoup

# Получаем HTML страницу
url = "https://parsinger.ru/table/1/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ячейки таблицы, кроме заголовков (<th>)
td_elements = soup.find_all('td')

# Извлекаем числа, превращаем в float и собираем уникальные
unique_numbers = set(float(td.text) for td in td_elements)

# Суммируем уникальные числа
total = sum(unique_numbers)

print(total)
