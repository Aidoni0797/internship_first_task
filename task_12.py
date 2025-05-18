import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/3/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Находим все элементы <b> и суммируем содержащиеся в них числа
bold_numbers = [float(b.text) for b in soup.find_all('b')]
total = sum(bold_numbers)

print(total)
