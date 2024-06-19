from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Попробуйте спарсить данную ссылку в течение часа, запустив цикл и проверив, нормально ли все отработает.
j = 0
# Созданный цикл нормально отработал в течение часа
while j < 10:
    j += 1
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com/groups/507802040142769/posts/1508557420067221/")
    time.sleep(10)
    click_button = driver.find_element(By.CLASS_NAME, "x92rtbv").click()
    # текст поста верный (точь в точь совпадает с ответом из тестового задания), не учитывая верхних четырех строк
    content = driver.find_element(By.CSS_SELECTOR, 'div.x1y332i5')
    print("\nТекст поста:\n", ' ', content.text)
    time.sleep(10)
    driver.close()