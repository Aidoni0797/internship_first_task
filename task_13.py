import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/4/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Находим все ячейки с зелёным цветом текста
green_cells = soup.find_all('td', style="color: green;")

# Извлекаем числа и суммируем
total = sum(float(cell.text) for cell in green_cells)

print(total)
