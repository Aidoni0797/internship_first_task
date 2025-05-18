import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/5/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

total = 0

rows = soup.find_all('tr')[1:]  # Пропускаем заголовок

for row in rows:
    orange_value = None
    blue_value = None
    for td in row.find_all('td'):
        style = td.get('style')
        if style == 'background-color: orange;':
            orange_value = float(td.text)
        elif style == 'background-color: #87CEFA;':
            blue_value = float(td.text)
    if orange_value is not None and blue_value is not None:
        total += orange_value * blue_value

print(total)
