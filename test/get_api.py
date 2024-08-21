import requests

response = requests.get(url='http://127.0.0.1:8000/cars/2')
if response.status_code == 200:
    cars = response.json()
    print(cars)