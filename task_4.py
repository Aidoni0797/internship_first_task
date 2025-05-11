from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/hdd/4/4_1.html'
response = requests.get(url)
response.encoding = 'utf-8'  # Обязательно! для корректной работы с русским текстом
soup = BeautifulSoup(response.text, 'lxml')

# Находим старую и новую цены
old_price = soup.find('span', id='old_price').text  # например: '11000 руб'
new_price = soup.find('span', id='price').text      # например: '8800 руб'

# Удаляем " руб" и переводим в числа
old = int(old_price.replace(' руб', '').strip())
new = int(new_price.replace(' руб', '').strip())

# Считаем скидку
discount = (old - new) * 100 / old

# Округляем до 1 знака после запятой
print(round(discount, 1))
