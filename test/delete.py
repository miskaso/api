import requests
import aouth


start = requests.delete(url='http://127.0.0.1:8000/cars/10/', headers=aouth.headers)

print(start.status_code)
if start.status_code == 204:
    print('Запись успешно удалена.')
else:
    print(f'Ошибка')
