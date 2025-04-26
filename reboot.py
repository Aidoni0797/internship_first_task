# chatgpt - ты молодец, а здесь iDONi сидит не умеет, когда ты станешь человеком
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime
import re

urls = [
    'https://www.facebook.com/groups/507802040142769/posts/1508557420067221/',
    'https://www.facebook.com/groups/gorodpavlodarkz/posts/8066751646691924/',
    'https://www.facebook.com/groups/gorodpavlodarkz/posts/8066204313413324/',
]

# Настройки драйвера
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Здесь можно добавить авторизацию, если нужно

results = []

for url in urls:
    driver.get(url)
    time.sleep(5)  # подождём загрузку контента

    try:
        # Текст поста
        try:
            post_text = driver.find_element(By.XPATH, '//div[contains(@data-ad-preview, "message")]').text
        except:
            post_text = ''

        # Дата поста
        try:
            date_element = driver.find_element(By.XPATH, '//a/abbr')
            timestamp = int(date_element.get_attribute('data-utime'))
            post_datetime = datetime.fromtimestamp(timestamp)
            post_date = post_datetime.date()
        except Exception:
            timestamp = None
            post_datetime = None
            post_date = None

        # Ссылка на вложение
        try:
            attachment_link = driver.find_element(By.XPATH, '//a[contains(@href, "http")]').get_attribute('href')
        except:
            attachment_link = None

        # Метрики: лайки, комментарии, репосты
        try:
            metrics_text = driver.find_element(By.XPATH, '//div[contains(@aria-label, " reactions")]').get_attribute('aria-label')
            likes = int(re.search(r'(\d+)', metrics_text).group(1))
        except:
            likes = 0

        try:
            comments_element = driver.find_element(By.XPATH, '//span[contains(text(), "комментарий") or contains(text(), "комментария")]')
            comments = int(re.search(r'\d+', comments_element.text).group())
        except:
            comments = 0

        try:
            shares_element = driver.find_element(By.XPATH, '//span[contains(text(), "поделился") or contains(text(), "поделились")]')
            shares = int(re.search(r'\d+', shares_element.text).group())
        except:
            shares = 0

        results.append({
            "url": url,
            "text": post_text,
            "unixtime": timestamp,
            "datetime": post_datetime,
            "date": post_date,
            "attachment_link": attachment_link,
            "likes": likes,
            "comments": comments,
            "shares": shares,
        })

    except Exception as e:
        print(f"Ошибка обработки поста {url}: {e}")

driver.quit()

# Вывод результатов
for post in results:
    print(post)
