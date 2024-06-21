from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Находим элемент, для которого нужно получить описание при наведении
    element = driver.find_element(By.CSS_SELECTOR, 'span.html-span.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1hl2dhg.x16tdsg8.x1vvkbs')
    print("\nElement text:\n", ' ', element.text)
    # # Создаем объект ActionChains для выполнения действий с мышью
    # action = ActionChains(driver)
    # action.click(element)
    # action.perform()
    #
    # # Ждем загрузки элемента с описанием
    # description_element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.ID, ':r2:'))
    # )
    #
    # # Получаем текст описания
    # description_text = description_element.text
    # print(f"Текст описания: {description_text}")

    time.sleep(10)
    driver.close()