import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
  target = browser.find_element(By.ID, 'like')
  actions = ActionChains(browser)
  # "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д."
  actions.move_to_element(target)
  # "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д."
  actions.click()
  # "тут может находится любой код, от time.sleep() до перехода в новую вкладку и т.д."
  actions.perform()