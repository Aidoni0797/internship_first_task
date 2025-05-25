import time
from selenium import webdriver

options_chrome = webdriver.ChromeOptions()

with webdriver.Chrome(options=options_chrome) as browser:
  url='https://aidoni0797.github.io/'
  browser.get(url)
  time.sleep(10)