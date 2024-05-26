from bs4 import BeautifulSoup
import pymysql
from playwright.sync_api import sync_playwright

db_connection = pymysql.connect(host='localhost', database='test', user='root', password='', port=3306, autocommit=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.facebook.com/groups/gorodpavlodarkz/posts/8066751646691924/")
    print(page.title())
    html = page.content()
    soup = BeautifulSoup(html, 'html.parser')
    content_title = soup.find('div', class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a').string
    date_post = soup.find('span', class_='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs').string
    content_text = soup.find_all('div', class_='xu06os2 x1ok221b')
    res= ''
    strversion_content_text = str(content_text[5])
    alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    for i in range(0, len(strversion_content_text)):
        if strversion_content_text[i].lower() in alphabet:
            res += strversion_content_text[i]
            if strversion_content_text[i+1].lower() == ' ':
                res+=' '
    metrics = soup.find('div', class_='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x5ve5x3')
    print("\nТitle поста:\n", content_title)
    print("\nДата поста в Facebook:\n", date_post)
    print("\nТекст поста:\n", res)
    if metrics == None:
        print('отсутствует')
    else:
        print(metrics)
    browser.close()

def write_to_db(db_connection):
    with db_connection.cursor() as cur:
        cur.execute(f"INSERT INTO title(title_post, date_post, text_post, metrics) VALUES('{content_title}','{date_post}','{res}', '{metrics}')")
    return cur.fetchall()

if __name__ == '__main__':
    write_to_db(db_connection)