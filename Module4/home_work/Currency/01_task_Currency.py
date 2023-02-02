from pprint import pprint

import requests


class Currency:
    def __init__(self, type):
        self.type = type

    def __getitem__(self, key: str):
        key = key.split('.')
        key[0], key[-1] = key[-1], key[0]
        key = '/'.join(key)
        url = f"https://www.cbr-xml-daily.ru/archive/{key}/daily_json.js"
        response = requests.get(url)
        response_json = response.json()
        if "error" in response_json:
            return response_json['explanation']
        if self.type == "usd":
            return response_json['Valute']['USD']['Value']
        else:
            return response_json['Valute']['EUR']['Value']


# Отправляем запрос на указанный url
usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"

print(usd['22.04.2009'])  # ← получение курса доллара на указанную дату
print(euro['20.06.2019'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение

