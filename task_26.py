import requests

# Загружаем JSON с сайта
url = "https://parsinger.ru/downloads/get_json/res.json"
response = requests.get(url)
data = response.json()

# Создаем словарь для хранения количества товаров по категориям
category_counts = {
    "watch": 0,
    "mobile": 0,
    "mouse": 0,
    "hdd": 0,
    "headphones": 0
}

# Проходим по каждому товару и добавляем количество в соответствующую категорию
for item in data:
    category = item["category"]
    quantity = item["count"]
    category_counts[category] += quantity

# Выводим результат
print(category_counts)
