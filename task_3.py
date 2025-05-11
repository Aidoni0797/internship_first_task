from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url)
response.encoding = 'utf-8'  # <-- Явно задаём правильную кодировку
soup = BeautifulSoup(response.text, 'lxml')

# Находим все теги с ценой — это <p class="price">
prices = soup.find_all('p', class_='price')

# Извлекаем числа, убираем "руб" и переводим в int
total = sum(int(price.text.replace(' руб', '')) for price in prices)

print('Сумма цен:', total)
