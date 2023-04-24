# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py

import requests


class Currency:
    def __init__(self, type):
        self.type = None
        if type == 'usd':
            self.type = 'USD'
        if type == 'euro':
            self.type = 'EUR'

    def __getitem__(self, date):
        split_date = date.split('.')
        url = f'https://www.cbr-xml-daily.ru/archive/{split_date[2]}/{split_date[1]}/{split_date[0]}/daily_json.js'
        response = requests.get(url)
        if response.status_code != 200:
            print(response.json())
            raise ValueError
        else:
            if self.type:
                self.__value = response.json()['Valute'][self.type]['Value']
                return self.__value



usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
