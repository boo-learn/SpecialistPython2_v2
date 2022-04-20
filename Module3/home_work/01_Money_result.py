import json
import urllib.request


class Money:

    def __init__(self, rubels, kopecks):
        self.rubels = rubels
        self.kopecks = kopecks
        if self.kopecks >= 100:
            self.rubels += (self.kopecks // 100)
            self.kopecks = (self.kopecks % 100)

    def transfer (self):
            return (f'{self.rubels}руб {self.kopecks}коп')

    def __add__ (self, other_money):
        rubels = self.rubels + other_money.rubels
        kopecks = self.kopecks + other_money.kopecks
        return f'{rubels}руб {kopecks}коп'


    def __sub__ (self, other_money):
        de_rub = self.rubels - other_money.rubels
        de_kop = self.kopecks - other_money.kopecks
        while de_kop < 0:
            de_rub -= 1
            de_kop += 100
        return f'{de_rub}руб {de_kop}коп'

    def __mul__ (self, count):
        rubels = self.rubels * count
        kopecks = self.kopecks * count
        return (f'{rubels}руб {kopecks}коп')

    def __gt__(self, other_money):
        if self.rubels > other_money.rubels:
            return True
        elif self.rubels < other_money.rubels:
            return False
        elif self.rubels == other_money.rubels and self.kopecks == other_money.kopecks:
            return False


    def __lt__(self, other_money):
        if self.rubels == other_money.rubels and self.kopecks == other_money.kopecks:
            return False
        else:
            return not self > other_money

    def __eq__(self, other_money):
        if self.rubels == other_money.rubels and self.kopecks == other_money.kopecks:
            return True
        else:
            return False


    def __ne__ (self, other_money):
        if self.rubels != other_money.rubels or self.kopecks != other_money.kopecks:
            return True
        else:
            return False

    def calc_procent (self, procent):
        rubels = (self.rubels / 100) * procent
        kopecks = (self.kopecks / 10000) * procent
        gen_procent = round(rubels + kopecks, 2)
        return gen_procent

    def convert (self):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        valute = data_dict.get('Valute')
        USD = valute.get('USD')
        cours = USD.get('Value')
        value = (self.rubels + (self.kopecks / 100)) / float(cours)
        return float(value)

money_sum1 = Money (120, 60)
money_sum2 = Money(120, 0)
count = 10
print(money_sum1.convert)

