import os

import requests

MY_API = os.getenv("EXCHANGE_RATE_API_KEY")

# url_tmp = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"
url = "https://api.apilayer.com/exchangerates_data/latest?symbols={RUB}&base={USD}"

# response = requests.get(url)

# print(response.status_code)


payload = {}
headers= {
  "apikey": "FodPH5fhQQUWxKDQVHC4cwzK5hV3ArNg"
}

response = requests.request("GET", url, headers=headers, data = payload)
print(response.status_code)
