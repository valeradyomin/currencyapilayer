import os

import requests

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
url = f"http://apilayer.net/api/live?access_key={API_KEY}&currencies=USD,RUB"

response = requests.get(url)
data = response.json()

print(response.status_code)
print(response.text)

# usd_to_rub = data['quotes']['USDRUB']
# print(f"Курс USD - RUB: {usd_to_rub}")
