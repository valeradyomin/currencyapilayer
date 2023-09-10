import requests

url = "https://api.github.com/search/repositories"

params = {"q": "python", "sort": "stars"}
response = requests.get(url, params=params)

print(response.json())

