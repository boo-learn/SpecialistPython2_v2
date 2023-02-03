# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py

import requests

class Currency:
    def __init__(self, type):
        self.currency = type

    def __getitem__(self, date):
        date = date.split('.')
        date = date[::-1]
        date = '/'.join(date)

        url = f'https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js'
        response = requests.get(url)
        response_result = response.json()

        if 'error' in response_result:
            return response_result['explanation']

        if self.currency == "usd":
            return response_result['Valute']['USD']['Value']
        elif self.currency == "euro":
            return response_result['Valute']['EUR']['Value']


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"

print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
