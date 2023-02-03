from pprint import pprint
import requests


class Currency:
    url_cur_type = None
    text_cur_type = ""
    data = ""

    def __init__(self, type):
        if type == "usd":
            self.url_cur_type = "USD"
            self.text_cur_type = "доллара"
        elif type == "euro":
            self.url_cur_type = "EUR"
            self.text_cur_type = "евро"

    def __getitem__(self, data):
        self.data = data
        try:
            year = self.data.split(".")[2]
            month = self.data.split(".")[1]
            day = self.data.split(".")[0]
            url = 'https://www.cbr-xml-daily.ru/archive/' + year + '/' + month + '/' + day + '/daily_json.js'
            response_answer = requests.get(url).json()
            return f"Курс {self.text_cur_type} на {self.data} равен {response_answer['Valute'][self.url_cur_type.upper()]['Value']}."

        except:
            return f"Некорректная дата. Скорректируйте её и повторите попытку."


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"
print(usd[""])
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
