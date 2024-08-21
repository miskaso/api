import requests


data = {
    'name': 'Lamborgini',
    'country': 'Germany',
    'info': 'Au32'}

response = requests.post(url='http://127.0.0.1:8000/cars/', json=data)
if response.status_code == 201:
    print('Запись добавлена.')
else:
    print(f"ОШибка! {response.text}-{response.status_code}")
