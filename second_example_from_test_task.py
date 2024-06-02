from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/groups/507802040142769/posts/1508557420067221/")
i = 0
try:
    title = driver.title
    button_x = driver.find_element(By.CLASS_NAME, "x92rtbv").click()
    element = driver.find_element(By.TAG_NAME, 'div')
    elements = element.find_elements(By.TAG_NAME, 'span')
    # Пишу хард код это плохо по другому пока не получается
    for e in elements:
        i += 1
        if i == 15:
            print("\nДата поста в Facebook:\n", ' ', e.text)
        if i == 53:
            print("\nТекст поста:\n", ' ', e.text)
except:
    print('Error')
time.sleep(100)
driver.quit()