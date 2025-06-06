from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Chrome() as browser:
    wait = WebDriverWait(browser, 10)
    target = wait.until(EC.presence_of_element_located((By.ID, 'like')))
