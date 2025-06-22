from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
import os

api_id = ___      # замени на свой
api_hash = '___'
chat_name = '___'  # можно также ID

client = TelegramClient('session_name', api_id, api_hash)

async def download_photos():
    await client.start()
    photos_folder = 'telegram_images'
    os.makedirs(photos_folder, exist_ok=True)

    async for message in client.iter_messages(chat_name):
        if message.media and isinstance(message.media, MessageMediaPhoto):
            await message.download_media(file=photos_folder)

    print("Фотографии скачаны.")

with client:
    client.loop.run_until_complete(download_photos())


#iDONi этот код изменил твою жизнь
