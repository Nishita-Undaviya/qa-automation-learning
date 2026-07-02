import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
print("Status code:", response.status_code)
print("Body:", response.json())