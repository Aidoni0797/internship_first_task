from selenium import webdriver
from selenium.webdriver.common.by import By  # импортируем By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')

# Используем современный способ поиска по ID
button = browser.find_element(By.ID, "sale_button").click()
