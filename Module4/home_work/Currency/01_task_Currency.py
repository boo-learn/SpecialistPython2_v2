# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py
import requests
from requests import HTTPError
import json      

class Currency:
    def __init__(self, type):
        self.type = type

    def __getitem__(self, time):
        day_month_year = time.split('.')
        url = f'https://www.cbr-xml-daily.ru/archive/{day_month_year[-1]}/{day_month_year[-2]}/{day_month_year[-3]}/daily_json.js'
        try:
            data = requests.get(url)
            data.raise_for_status()
        except HTTPError as err:
            return f'HTTP error occurred: {err}'
        json_serialize = data.json()
        return (json_serialize['Valute'][self.type.upper()]['Value'])




usd = Currency('usd')
eur = Currency('eur')
print(usd['12.11.2022'])
print(eur['12.11.2022'])

print(usd['01.01.2019'])
print(eur['01.01.2019'])


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
