# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py
import requests

class Currency:
    def __init__(self, type):
        self.type = type

    def __getitem__(self, item):
        data = '/'.join(item.split('.')[::-1])
        url = f'https://www.cbr-xml-daily.ru/archive/{data}/daily_json.js'
        try:
            response = requests.get(url)
            return f"Курс {self.type} на {item} = {response.json()['Valute'][f'{self.type.upper()}']['Value']}"
        except KeyError:
            return 'Неверная дата!'




usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("eur")  # Создаем валюту "Евро"
print(usd['28.10.2021'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
