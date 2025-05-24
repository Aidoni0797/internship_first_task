import requests

# ��������� JSON � �����
url = "https://parsinger.ru/downloads/get_json/res.json"
response = requests.get(url)
data = response.json()

# ������� ������� ��� �������� ���������� ������� �� ����������
category_counts = {
    "watch": 0,
    "mobile": 0,
    "mouse": 0,
    "hdd": 0,
    "headphones": 0
}

# �������� �� ������� ������ � ��������� ���������� � ��������������� ���������
for item in data:
    category = item["category"]
    quantity = item["count"]
    category_counts[category] += quantity

# ������� ���������
print(category_counts)
