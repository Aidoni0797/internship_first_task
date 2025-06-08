from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
  browser.get('http://parsinger.ru/expectations/1/index.html')
  browser.find_element(By.ID, 'btn').click()