from selenium import webdriver
import time

url = 'https://stepik.org'
browser = webdriver.Chrome()
time.sleep(180)
browser.get(url)

time.sleep(180)