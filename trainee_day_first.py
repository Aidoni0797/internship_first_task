import requests
from bs4 import BeautifulSoup
def main():
    url = 'https://www.facebook.com/groups/gorodpavlodarkz/posts/8066253500075072/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_text = soup.find('div', class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a')
    print(content_text)
    date_post = soup.find('span', class_='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs')
    print(date_post)
    link = soup.find('div',
                          class_='html-div xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6')
    print(link)
    metrics = soup.find('div',
                     class_='x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x5ve5x3')
    print(metrics)
    filename = 'result.json'
    with open(filename, "w", encoding='UTF-8') as file:
        file.write("\nТекст поста:\n" + str(content_text))
        file.write("\nДата поста в Facebook:\n" + str(date_post))
        file.write("\nСсылка на вложение:\n" + str(link))
        file.write("\nМетрика:\n" + str(metrics))
if __name__ == '__main__':
    main()
