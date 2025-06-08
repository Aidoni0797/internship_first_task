from selenium import webdriver

with webdriver.Chrome() as browser:
  browser.get('http://parsinger.ru/window_size/1')
  browser.set_window_size(1200, 720)
  print(browser.get_window_size()["width"])
  print(browser.get_window_size()["height"])