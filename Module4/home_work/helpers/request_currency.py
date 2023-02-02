from pprint import pprint
import requests


class Currency:
    USD = "usd"

    def __init__(self, type: str):
        if type.lower() == "euro":
            type = "eur"
        self.type = type.upper()
        self.url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __str__(self) -> str:
        return f"Текущий курс {self.type}: {requests.get(self.url).json()['Valute'][self.type]['Value']}"

    def __getitem__(self, date: str) -> str:
        f_date = '/'.join(date.split(".")[-1::-1])
        url = f"https://www.cbr-xml-daily.ru/archive/{f_date}/daily_json.js"
        try:
            result = f"Курс {self.type} на {date}: {requests.get(url).json()['Valute'][self.type]['Value']}"
            return result
        except KeyError:
            return "Неправильная дата"


usd = Currency("usd")
euro = Currency("euro")
zar = Currency("zar")

print(usd)
print(euro)
print(zar)

print(usd['13.11.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение


# немного  криво реализовал конструктор, так как евро в ответе api имеет ключ EUR
# не хватает знаний как правильно описать в классе проверку по списоку валют :
# ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', 'EUR',
#  'EGP', 'INR', 'IDR', 'KZT', 'CAD', 'QAR', 'KGS', 'CNY', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', 'XDR', 'SGD',
#  'TJS', 'THB', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'RSD', 'ZAR', 'KRW', 'JPY']
