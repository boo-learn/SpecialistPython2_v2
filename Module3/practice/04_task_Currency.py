from datetime import datetime, date
from typing import Union

import requests


class Currency:
    """Валюта"""
    URL_CURRENT_DATA = 'https://www.cbr-xml-daily.ru/daily_json.js'
    URL_DAILY_BASE = 'https://www.cbr-xml-daily.ru/archive/'
    URL_DAILY_END = '/daily_json.js'

    def __init__(self, name):
        self.__generate_char_code(name)
        self.__generate_currency_data()

    def __str__(self):
        return f'Currency {self.char_code}: {round(self.value, 2)}р.'

    def __getitem__(self, item):
        return round(self.get_current_day_currency(item), 2)

    def __generate_char_code(self, name: str):
        """Получает сырое название валюты и возвращает правильное наименование"""
        self.char_code = name.upper()[:3]

    def __get_currencies_dict(self, url):
        """Делает запрос и возвращает JSON """
        return requests.get(url).json()['Valute']

    def __generate_currency_data(self):
        """Генерирует аттрибуты класса на основе полученных от ЦБ данных и названия валюты"""
        try:
            currency_data = self.__get_currencies_dict(self.URL_CURRENT_DATA)[self.char_code]
            self.value = currency_data['Value']
        except KeyError:
            print('Вы ввели неправильное имя валюты, либо её нет в списке. Будьте внимательней.\n'
                  'Правильно вот так: "eur", "euro", "EUR", "USD", "usd" и т.д. ')
            raise KeyError
        self.values_dict = {f"{datetime.now().strftime('%Y/%m/%d')}": self.value}

    def __convert_string_to_datetime(self, string: str) -> datetime:
        """Получает строку и конвертирует её в datetime"""
        patterns = ['%d.%m.%Y', '%Y.%m.%d', '%d/%m/%Y', '%Y/%m/%d']
        for pattern in patterns:
            try:
                string = datetime.strptime(string, pattern)
                break
            except ValueError:
                continue
        return string

    def __convert_datetime_to_right_string(self, day: datetime) -> str:
        """Получает datetime и конвертирует его в нужную для запроса строку"""
        try:
            day = day.strftime('%Y/%m/%d')
        except AttributeError:
            print('Вы ввели неправильную дату')
            raise AttributeError
        return day

    def __search_for_day_in_saved_list(self, day: str) -> float:
        """Получает строку с датой и проверяет есть-ли уже спарсенные значения на эту дату"""
        for key in self.values_dict:
            if day == key:
                return self.values_dict[key]
        return None

    def get_current_day_currency(self, day: Union[datetime, date, str]):
        """Получает объект datetime или строку и делает запрос курс в конкретную дату"""
        if type(day) == str:    # Преобразуем полученную строку в объект datetime
            day = self.__convert_string_to_datetime(day)
        day = self.__convert_datetime_to_right_string(day)

        early_parsed_data = self.__search_for_day_in_saved_list(day)    # Проверяем парсились-ли эти данные ранее
        if early_parsed_data:
            return early_parsed_data

        url = self.URL_DAILY_BASE + day + self.URL_DAILY_END
        res = requests.get(url).json()['Valute'][self.char_code]['Value']
        self.values_dict[day] = res
        return round(res, 2)


if __name__ == '__main__':
    usd = Currency("usd")  # Создаем валюту "Доллар"
    euro = Currency("euro")  # Создаем валюту "Евро"
    print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
    print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
    # print(euro['12.14.2018'])  # ← в случае некорректной выбрасываем исключение
    print(usd[datetime.now()])    # А так же можно доставать и через datetime
