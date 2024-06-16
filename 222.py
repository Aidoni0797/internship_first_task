# import requests
# # начал как-то реагировать
# access_token = 'EAAGisEEXJEwBOZBcG1E7YZBVssWKa9r2VFteGoMADsGUeVZCC2piMv6kyEiuisuioEZBNUSwUtxFZCTHQsr5JgfxhCa8oAlIM1IFE2J9mBNkfTIMUR5P2kY8BrrxQJZCOhzWJgqidYs4WZBzJYaZByrl9YOhoH7uu5iprHFUvZCM7DrBeZCCDqASHLnnSbnnxZCmxxHMukk7CTxSKoyPtf0qf4nXWuv2ZAakcrR6ZBZAeXuwrwTcDNfdmO1PiY'
# url = 'https://graph.facebook.com/me'
# params = {
#     'access_token': access_token
# }
#
# response = requests.get(url, params=params)
# user_info = response.json()
#
# print(user_info)
# print('User ID:', user_info['id'])
# print('Name:', user_info['name'])

import requests

# Замените на ваш токен доступа
access_token = 'EAAGisEEXJEwBOyRl2Hzv3a7HB8hFU1wZCuMmplNsgOQnnxXmOqiBWF3JDfmXIc9VAZCkImpnV5kssN2CZCe7F9MQTAZB1Gci4ZCuVDrGgB9H4KIUiy4mRZAaH8PIH6eT4M2jofhf4uFRUszjtXV4cbHzYNTOd9fOVZBjAd0nxRa5oFXOA6rxMgS6a0IrGM1hzSoTB21SxkXHaOwnFX7gZB3T1LHMvlMDbZAu7DxrKwFxPlJqD2bbQ5NWXw0FF4tpmcAZDZD'

# Замените на ID страницы или 'me' для текущего пользователя
# ну и заменила где результат фиг поймешь
page_id = '1513921342864162'

# URL для получения постов страницы или пользователя
url = f'https://graph.facebook.com/v12.0/{page_id}/posts'

# Параметры запроса (указываем токен доступа и необходимые поля)
params = {
    'access_token': access_token,
    'fields': 'id,message,created_time'  # указываем запрашиваемые поля поста
}

# Выполняем GET запрос к API
response = requests.get(url, params=params)
posts_data = response.json()
print(posts_data)
# Выводим результат
if response.status_code == 200:
    for post in posts_data['data']:
        print('Post ID:', post['id'])
        print('Message:', post['message'])
        print('Created Time:', post['created_time'])
        print()
else:
    print('Ошибка при выполнении запроса:', posts_data)