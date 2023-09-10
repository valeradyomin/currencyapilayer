from datetime import datetime
import requests
import json
import os

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
CURRENCY_RATES_FILE = "currency_rates.json"


def get_currency_rate(base: str) -> float:
    """
    Получает курс валюты от API и возвращает его в виде float
    :param base:
    :return:
    """
    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={"apikey": API_KEY}, params={"base": base})
    rate = response.json()["rates"]["RUB"]
    return rate


def save_to_json(data: dict) -> None:
    """
    Сохраняет данные в JSON-файл
    :param data:
    :return:
    """
    with open(CURRENCY_RATES_FILE, "a") as file:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], file)
        else:
            with open(CURRENCY_RATES_FILE, "r") as file:
                data_list = json.load(file)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, "w") as file:
                json.dump(data_list, file)


def main():
    while True:
        currency = input("Ведите название валюты (USD или EUR): ")
        if currency not in ("USD", "EUR"):
            print("некорректный ввод")
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Курс {currency} к рублю {rate}")
        data = {"currency": currency, "rate": rate, "timestamp": timestamp}
        save_to_json(data)

        choice = input("Выберите действие: (1 - прододжить, 2 - выйти) ")
        if choice == "1":
            continue
        elif choice == "2":
            break
        else:
            print("некорректный ввод")


if __name__ == '__main__':
    main()