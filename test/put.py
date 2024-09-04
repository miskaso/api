import requests
import aouth


data = {
    "name": "Новая",
    "info": "Это описание было изменено.",
    "country": "Kyrgyzstan",
}

start = requests.put(url='http://127.0.0.1:8000/cars/10/', json=data, headers=aouth.headers)

print(start.status_code)
if start.status_code == 201:
    print('Запись успешно изменена.')
elif start.status_code == 200:
    print('Что то успешно выполнено.')
else:
    print(f'Ошибка {start.text}')