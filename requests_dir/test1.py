import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(dir(response))
print(response.content)
print(response.text)
print(response.json())

