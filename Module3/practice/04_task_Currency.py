# Задание: Создать удобную структуру для работы с курсами валют на определенную дату
# Курсы валют будем брать с этого сайта: https://www.cbr-xml-daily.ru/ .
# Нас будут интересовать только курсы доллара и евро.
# Как получить курс по API со стороннего сайта - смотри в request_currency.py
# Внимание! Библиотеку requests нужно установить, выполните в консоли команду:
# pip install requests
import requests


class Currency:
    def __init__(self, type_curr):
        self.curr_id = type_curr.upper()

    def __getitem__(self, item):
        date = item.split('.')
        url = f'https://www.cbr-xml-daily.ru/archive/{date[2]}/{date[0]}/{date[1]}/daily_json.js'
        response = requests.get(url).json()
        try:
            if response.get('error') == 'Not found':
                raise ValueError
            else:
                return f'Стоимость 1 {self.curr_id} на {response["Date"][:10]} составляет ' \
                       f'{response["Valute"][self.curr_id]["Value"]} RUB.'
        except ValueError:
            print('Курс ЦБ РФ на данную дату не установлен или задана некорректная дата')


# url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# Отправляем запрос на указанный url
# Если хотим получить курсы на определенную дату, то нужно отправить запрос на :
# url: https://www.cbr-xml-daily.ru/archive/2021/04/07/daily_json.js
# /2021(год)/04(месяц)/07(день)/
# response = requests.get(url)
# pprint(response.json())


usd = Currency("usd")  # Создаем валюту "Доллар"
eur = Currency("eur")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(eur['12.10.2018'])  # ← получение курса евро на указанную дату
print(eur['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
