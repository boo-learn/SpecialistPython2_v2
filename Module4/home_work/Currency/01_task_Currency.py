import requests
from datetime import datetime


class Currency:
    def __init__(self, currency: str):

        possible_currencies = {"dollar": "usd", "euro": "eur"}
        if type(currency) != str:
            raise TypeError("Invalid type, please only str arguments")
        if currency not in possible_currencies.values() and currency not in possible_currencies.keys():
            raise ValueError('Currency not in dict of possible_currencies')

        for key, value in possible_currencies.items():
            if currency.upper() == key.upper():
                self._currency = value
            elif currency.upper() == value.upper():
                self._currency = value

    def __getitem__(self, key):
        if datetime.now().strftime('%d.%m.%Y') == key:
            url = 'https://www.cbr-xml-daily.ru/daily_json.js'
            response = requests.get(url)
        else:
            input_date = datetime.strptime(key, '%d.%m.%Y')
            date = input_date.strftime('%Y/%m/%d')
            url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
            response = requests.get(url)
        return response.json()['Valute'][self._currency.upper()]['Value']
