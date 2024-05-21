import pymysql
from playwright.sync_api import sync_playwright
db_connection = pymysql.connect(host='localhost', database='test', user='root', password='', autocommit=True)
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.facebook.com/groups/gorodpavlodarkz/posts/8066751646691924/")
    title_page = page.title()
    print(page.title())
    browser.close()
def write_to_db(db_connection):
    with db_connection.cursor() as cur:
        cur.execute(f"INSERT INTO title(title_page) VALUES('{title_page}')")
    return cur.fetchall()
if __name__ == '__main__':
    write_to_db(db_connection)