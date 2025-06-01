from selenium import webdriver

with webdriver.Chrome() as webdriver:
  webdriver.get('https://ya.ru/')
  cookies = webdriver.get_cookies()
  for cookie in cookies:
    print(cookie['name']) # cookie['value'] чтобы получить их значение