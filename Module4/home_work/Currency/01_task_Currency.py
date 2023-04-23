# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py
import requests
from requests import RequestException


class Currency:
    def __init__(self, type):
        self.type = type.upper()[:3]

    def __get_exchange_value(self, day, month, year):
        url = f'https://www.cbr-xml-daily.ru/archive/{year}/{month}/{day}/daily_json.js'
        request = requests.get(url)
        if request.status_code == 404:
            request.raise_for_status()
        request_json = request.json()
        return request_json['Valute'][self.type]['Value']

    def __getitem__(self, date):
        self.day, self.month, self.year = date.split('.')
        exchange_value = self.__get_exchange_value(self.day, self.month, self.year)
        return f'{date}: 1{self.type} = {exchange_value}RUB'


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
