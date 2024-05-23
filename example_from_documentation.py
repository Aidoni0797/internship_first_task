from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.facebook.com/groups/gorodpavlodarkz/posts/8066751646691924/")
    # Чтобы убрать лишние данные пишу хард код это плохо
    # обявляю переменную result и присваюваю значение полученного title
    result = page.title()
    # n переменная отвечает за длину полученной длину строки
    n = len(str(result))
    # start - переменная обявлена с целю в дальнейшем узнать и сохранить индекс начало title строки без название источника
    start = 0
    # end - переменная обявлена с целю в дальнейшем узнать и сохранить индекс конец title строки без слово Facebook
    end = 0
    # начинается цикл который в пределах строки найти знак |  и соответственно присваевает значение индексов в соответствующие переменные
    # в моем случае start и end (Строки с №18 по №22 - отвечает за эти действия)
    for i, j in enumerate(str(result)):
        if j == '|' and start == 0:
            start = i
        elif j == '|':
            end = i
    # обявляю переменную new_result чтобы в дальнейшем собрать по буквенно текст от индекса start по индекса end
    new_result = ''
    # начинается цикл который значении по шагово присваевает к переменной new_result
    for i in range(start+2, end-1):
        new_result += result[i]
    # делаем принт без лишних данных, без название источника, без слово Facebook (в моем представленн)
    print(new_result)
    browser.close()