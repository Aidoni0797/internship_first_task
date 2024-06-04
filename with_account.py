from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from bs4 import BeautifulSoup
import time

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWNhODdiZmE0YzM0YTAzOGRjYmZkMDkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NWNhODhiODAyZDlmZjFkMTI1ODliYTAifQ.ry3kq0hFKnCQmYh93Km9EgJwXYGOtWwu5xQExm20s-Q'
profile_id = '65ca8a05e0878026237463c9'
port = 3942

gl = GoLogin({
    'token': token,
    'profile_id': profile_id,
    'port': port
})

login_1 = '79896318901'
pass_1 = 'mama230260 '

chrome_driver_path = 'chromedriver.exe'

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', debugger_address)



driver = webdriver.Chrome()
driver.get('http://www.facebook.com')
data_one = driver.page_source
# по моей логике – это означает правильно ли я мыслю в эту сторону
# login_to_facebook – название функции, driver, login_1, pass_1 – принимающие переменные
def login_to_facebook(driver, login_1, pass_1):
    # login_url – переменная который содержит страницу
    login_url = 'https://www.facebook.com/login.php'
    # по моей логике driver.get – возвращает данные html страницы
    driver.get(login_url)
    # это ошибки показывает
    try:
        # email_element – переменная много чего выполняет но непонятно
        # EC.presence_of_element_located((By.ID, ‘email’)) – это условие, которое говорит Selenium ждать, пока на странице не будет найден элемент с указанным id ‘email’.
        email_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'email'))
        )
        # send_keys() – метод в SeleniumWebDriver используется для ввода текста или нажатия клавиш в текстовое поле или другой элемент веб-страницы.
        email_element.send_keys(login_1)
        # password_element – переменная которая ищет элемента с id ‘pass’
        password_element = driver.find_element(By.ID, 'pass')
        # send_keys – это метод в SeleniumWebDriver используется для ввода текста или нажатия клавиш в текстовое поле или другой элемент веб-страницы.
        password_element.send_keys(pass_1)
        # login_button – переменная которая ищет элемента с id ‘loginbutton’
        login_button = driver.find_element(By.ID, 'loginbutton')
        # click – нажатие кнопки
        login_button.click()
        # время на 3 секунды останавливает выполнение авторизации
        time.sleep(3)
        print('Авторизация прошла успешно!!!')
        # при выполнении кода в теле try возникла ошибка в теле except сообщает об ошибке
    except Exception as e:
        print('Ошибка при авторизации:', e)

# parse_data – название функции, которая принимает два переменных driver, data_one – но пока непонятно #откуда идет эти переменные
def parse_data(driver, data_one):
    if 'Facebook помогает вам всегда оставаться на связи' in str(data_one) or 'Забыли пароль' in str(data_one):
        # вызывается функция ранее обявленный под названием login_to_facebook
        login_to_facebook(driver, login_1, pass_1)
    else:
        print('Уже авторизован!!!')



    # link – это для содержание ссылки которая в своем теле содержит  переменную tag_name передает значение #искомого значения может быть могу ошибаться filters это напонятно
    link = f'https://www.facebook.com/groups/gorodpavlodarkz/posts/8066253500075072/'

    try:
        # data_ - переменная который содержит у себя функцию get_data – данная функция где объявлено #непонятно где вы  при этом он принимает два аргумента link, driver
        data_ = get_data(link, driver)

        # items  - переменная который содержит у себя функцию get_links_from_source – данная функция где #объявлено непонятно где вы  при этом он принимает один аргумент data_ - который объявлено строка выше #принимающая функцию – этот момент надо разобраться
        items = get_title_from_source(data_)

        # items – нам возвращает полученные ссылки и в цикле возвращая переменной url пошагово
        for title in items:
            # post_url – переменная также использует функции в нашем случае process_url – принимает себе #переменную в итерации url
            post_title = process_title(title)
            print('Post title:', post_title)
    # except – тело функции который в случае ошибки в теле try выполняет показывает ошибку
    except Exception as ex:
        print('Main', ex)
    # driver – закрывает переменную открытую браузер
        driver.close()


    # вот и наш долгожданная функция get_data, который мы искали, оказывается он у нас принимает два #аргумента url, driver
def get_data(url, driver):
    driver.get(url)
    for i in range(1, 5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
    data = driver.page_source
    data = str(data)
    return data

def get_title_from_source(data):
    soup = BeautifulSoup(data, 'html.parser')
    content_text = soup.find('div', class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a').string
    print(content_text)
    date_post = soup.find('span',
                          class_='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs').string
    print(date_post)
    link = soup.find('div',
                     class_='html-div xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6').string
    print(link)
    metrics = soup.find('div',
                        class_='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x5ve5x3').string
    print(metrics)
    filename = 'result.json'
    with open(filename, "w", encoding='UTF-8') as file:
        file.write("\nТекст поста:\n" + str(content_text))
        file.write("\nДата поста в Facebook:\n" + str(date_post))
        file.write("\nСсылка на вложение:\n" + str(link))
        file.write("\nМетрика:\n" + str(metrics))

def process_title(title):
    return title

if __name__ == '__main__':
    parse_data(driver, data_one)