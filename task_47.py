import requests

# Замените на своё имя пользователя и токен GitHub
username = "Aidoni0797"
token = "ghp_..."  # Твой GitHub Personal Access Token

def get_users(url):
    users = []
    while url:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()
        users += [user["login"] for user in response.json()]
        url = response.links.get('next', {}).get('url')
    return users

following_url = f"https://api.github.com/users/Aidoni0797/following"
followers_url = f"https://api.github.com/users/Aidoni0797/followers"

following = set(get_users(following_url))
followers = set(get_users(followers_url))



not_following_back = following - followers

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("🔻 Эти пользователи не подписаны на тебя в ответ:\n")
    for user in sorted(not_following_back):
        f.write(f"{user}\n")

