# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в request_currency.py

import requests


class Currency:
    def __init__(self, type):
        self.valute = type.upper()

    def __getitem__(self, item):
        date = item.split('.')
        url = f"https://www.cbr-xml-daily.ru/archive/{date[2]}/{date[1]}/{date[0]}/daily_json.js"
        response = requests.get(url).json()
        if 'code' in response:
            raise ValueError('Wrong date!')
        return response['Valute'][self.valute]['Value']


usd = Currency("usd")  # Создаем валюту "Доллар"
eur = Currency("eur")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(eur['12.10.2018'])  # ← получение курса евро на указанную дату
print(eur['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
