class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __str__(self):
        rubls_in_kop = self.kop // 100
        return f'{self.rub + rubls_in_kop}руб {self.kop % 100}коп'

    def __add__(self, two_money):
        return Money(self.rub + two_money.rub, self.kop + two_money.kop)

    def __sub__(self, two_money):
        return Money(self.rub - two_money.rub, self.kop - two_money.kop)

    def __mul__(self, x):
        return Money(self.rub * x, self.kop * x)

    def __gt__(self, two_money):
        return self.rub + self.kop // 100 + self.kop % 100 > two_money.rub + two_money.kop // 100 + two_money.kop % 100

    def __lt__(self, two_money):
        return not self > two_money and not self == two_money

    def __eq__(self, two_money):
        return self.rub == two_money.rub and self.kop == two_money.kop

    def convert(self):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        k_usd = data_dict['Valute']['USD']['Value']
        k_eur = data_dict['Valute']['EUR']['Value']
        rub_for_convert = self.rub + self.kop / 100
        return f'Конвертация USD:{rub_for_convert*k_usd} , EUR: {rub_for_convert*k_eur}'
