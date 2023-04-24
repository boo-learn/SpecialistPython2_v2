
import urllib.request
import json

URL1 = "https://www.cbr-xml-daily.ru/archive/"
URL2 = "/daily_json.js"

ALL_CURRENCIES_TO_OPERATE = ("AUD", "AZN", "GBP", "AMD", "BYN", "BGN", "BRL", "HUF", "VND", "HKD", "GEL", "DKK", "AED", "USD", "EUR", "EGP", "INR", "IDR", "KZT", "CAD", "QAR", "KGS", "CNY", "MDL", "NZD", "NOK", "PLN", "RON", "XDR", "SGD", "TJS", "THB", "TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "RSD", "ZAR", "KRW", "JPY")


def get_date_str(date) -> str:
    return f"{date[6:]}/{date[3:5]}/{date[0:2]}"


def try_iso_code(code) -> bool:
    return code in ALL_CURRENCIES_TO_OPERATE


class Currency:
    def __init__(self, currency_name: str = "USD"):
        currency_name = currency_name.upper()
        if currency_name == "EURO":
            currency_name = "EUR"
        if try_iso_code(currency_name):
            self.__currency_iso_code = currency_name
            self.__exchange_rate = 0
        else:
            raise ValueError("We can't operate with this currency!")

    def __str__(self) -> str:
        return f"{self.__exchange_rate}"

    def __getitem__(self, date):
        __url = f'{URL1}{get_date_str(date)}{URL2}'
        __data = b""
        try:
            __data = urllib.request.urlopen(__url).read()
        except:
            self.__exchange_rate = 0
            raise ValueError("Курс ЦБ РФ на данную дату не установлен")
        if len(__data) > 0:
            __data_dict = json.loads(__data)
            self.__exchange_rate = __data_dict["Valute"][self.__currency_iso_code]["Value"]
            return self.__exchange_rate


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("euro")  # Создаем валюту "Евро"

print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату

# print(euro['20.10.2018'])  # ← получить удаётся
# print(euro['21.10.2018'])  # ← получить не удаётся Курс ЦБ РФ на данную дату не установлен
# print(euro['22.10.2018'])  # ← получить не удаётся Курс ЦБ РФ на данную дату не установлен
# print(euro['23.10.2018'])  # ← получить удаётся

# print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
