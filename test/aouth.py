import requests


user = {
    "username": "admi",
    "password": "admi",
}

response = requests.post(url='http://127.0.0.1:8000/api/token/', json=user)
print(response)
if response.status_code == 200:
    print('Отправлено')
else:
    print('Ошибка')

ai = response.json().get('access')
headers = {
    "Authorization": f"Bearer {ai}"
}

goo = requests.get(url='http://127.0.0.1:8000/cars/2', headers=headers)
print(goo.json())
