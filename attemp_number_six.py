import requests

def get_facebook_post_details(access_token, group_id, post_id):
    url = f"https://graph.facebook.com/v20.0/{group_id}_{post_id}"
    params = {
        'access_token': access_token,
        'fields': 'id,message,created_time,from,permalink_url'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    ACCESS_TOKEN = 'EAAGisEEXJEwBOxoTvhJerQ8TWV0ZATLgk8i6ZBZB2RuayzTYOzsZAVQkJX2uElEcOTOhJfgTZCQEDp8j9RYjMdKf4ZBcXDOzFBj27vl5ugZCriIWbDL65qB4w7sAAKLwdFGp2qAZAiDoymtA2ZCuMzCu0rBCtkdrtLlByj5y7UoZBDmqvHW0ct5qAxVzpe6rZAdd2fbD4CiFv87hngugHxSJZA0OoLjPAAViKm960oOZAEyKs0iEDXbUx71yKTL7ZBmbZAcmQZDZD'
    GROUP_ID = '507802040142769'
    POST_ID = '1508557420067221'

    post_details = get_facebook_post_details(ACCESS_TOKEN, GROUP_ID, POST_ID)
    if post_details:
        print(post_details)