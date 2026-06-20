import requests

response = requests.get("https://httpbin.org/json")
print("Статус:", response.status_code)
print("Ответ:", response.json())
