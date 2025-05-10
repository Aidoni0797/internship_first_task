import requests
import os

# URL на видеофайл (предположим, конкретный файл указан)
url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'

# Скачиваем файл по частям
response = requests.get(url, stream=True)
filename = 'video.mp4'

with open(filename, 'wb') as video:
    for piece in response.iter_content(chunk_size=100_000):
        if piece:  # чтобы не писать пустые чанки
            video.write(piece)

# Получаем размер файла
size_bytes = os.path.getsize(filename)
size_mb = size_bytes / (1024 * 1024)
print(f'Размер файла: {size_mb:.2f} MB')
