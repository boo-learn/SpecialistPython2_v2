from pprint import pprint
# pip install requests
import requests
class Currency:
    def __init__(self, type):
        self.type = type

    def course(self, date):
        date = date.split(".")
        url = f'https://www.cbr-xml-daily.ru/archive/{date[2]}/{date[1]}/{date[0]}/daily_json.js'
        response = requests.get(url)
        return pprint(response.json()['Valute'][self.type]['Value'])

usd = Currency("USD")  # Создаем валюту "Доллар"
euro = Currency("EUR")


print(euro.course('10.07.2021'))
