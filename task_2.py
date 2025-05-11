import os
import requests
from bs4 import BeautifulSoup

# Создаем папку для сохранения изображений
os.makedirs("images", exist_ok=True)

# Получаем HTML-страницу
url = "https://parsinger.ru/img_download/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Находим все ссылки на изображения
img_tags = soup.find_all("img")

# Скачиваем каждое изображение
for i, img in enumerate(img_tags, start=1):
    img_url = f"https://parsinger.ru/img_download/{img['src']}"
    img_data = requests.get(img_url).content
    with open(f"images/image_{i}.png", "wb") as file:
        file.write(img_data)
    print(f"Скачано изображение {i}")

print("Все изображения успешно загружены в папку 'images'.")
