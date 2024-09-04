import aouth
import requests


data = {
    "name": "Lada",
    "info": "blalblalb",
    "country": "Germany",
}

start = requests.post(url='http://127.0.0.1:8000/cars/', json=data, headers=aouth.headers)

if start.status_code == 201:
    print(f'Запись {start.json()} создана')
else:
    print('Ошибка.', start.text)