# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в helpers/request_currency.py
from datetime import datetime
import requests


class Currency:
    def __init__(self, type):
        types = {"euro": "EUR", "usd": "USD"}
        if type in types:
            self.type = types.get(type)
        else:
            print(f"Валюта не поддерживается: {type}")
            del self
            return

    def __getitem__(self, input_date):
        input_date_format = r'%d.%m.%Y'
        input_date = datetime.strptime(input_date, input_date_format).date()
        current_date = datetime.today().date()
        if input_date > current_date:
            raise ValueError(f"Дата {input_date} больше текущей")
        elif input_date == current_date:
            url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        else:
            api_date_format = r'%Y/%m/%d'
            api_date = input_date.strftime(api_date_format)
            url = f'https://www.cbr-xml-daily.ru/archive/{api_date}/daily_json.js'
        response = requests.get(url)
        data_dict = response.json()
        valute = data_dict.get("Valute").get(self.type)
        if valute:
            return valute.get("Value")
        else:
            print(f'В ответе валюта не найдена: "{self.type}"')
            return



usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd['26.12.2022'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
# print(usd['31.12.2030']) # в случае некорректной выбрасываем исключение (из будущего)
# print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
