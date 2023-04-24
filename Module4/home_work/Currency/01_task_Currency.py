import requests
from datetime import datetime


class Currency:
    def __init__(self, currency):
        possible_currencies = {"dollar": "usd", "euro": "eur"}
        for key, value in possible_currencies.items():
            if currency == key:
                self._currency = value
            elif currency == value:
                self._currency = value

    def __getitem__(self, key):
        input_date = datetime.strptime(key, '%d.%m.%Y')
        date = str(input_date.strftime('%Y/%m/%d'))
        url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
        response = requests.get(url)
        return response.json()['Valute'][self._currency.upper()]['Value']
