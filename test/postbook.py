import requests


url = "http://127.0.0.1:8000/book/"

data = {
    "name": "Никита",
    "books": [{
        'title': 'Похождения Величайшего'
    }]
}

respon = requests.post(url=url, json=data)

if respon.status_code == 201:
    print('Выполнено')
else:
    print("Ошибка")