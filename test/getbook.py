import requests

response = requests.delete(url="http://127.0.0.1:8000/book/2")

if response.status_code == 200:
    boko = response.json()
    print(boko)

