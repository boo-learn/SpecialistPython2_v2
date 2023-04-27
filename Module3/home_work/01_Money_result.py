import urllib.request, json


class Money:
    def __init__(self, rub = 0, kop = 0):
        self.__rub = rub
        self.__kop = int(kop)
        self.__negative_flag = False
        self.__url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        self.__money_round()

    def __money_round(self):
        if self.__rub < 0:
            self.__rub = 0
        if self.__kop < 0:
            self.__kop = 0
        if self.__kop >= 100:
            self.__rub += self.__kop // 100
            self.__kop = self.__kop % 100

    def __money_in_kop(self):
        return self.__rub * 100 + self.__kop
    
    def show(self):
        return self.__rub, self.__kop

    def __abs(self, value):
        if value < 0:
            return -value
        else:
            return value

    def is_negative(self):
        return self.__negative_flag

    def __str__(self):
        return f'{self.__rub},{self.__kop}'

    def __add__(self, other_money):
        new_money_rub = self.__rub + other_money.__rub
        new_money_kop = self.__kop + other_money.__kop
        return Money(new_money_rub, new_money_kop)

    def __sub__(self, other_money):
        new_money_in_kop = self.__money_in_kop() - other_money.__money_in_kop()
        if new_money_in_kop < 0:
            new_money = Money(kop=self.__abs(new_money_in_kop))
            new_money.__negative_flag = True
            return new_money
        else:
            return Money(kop=new_money_in_kop)

    def __mul__(self, k: int):
        new_money_in_kop = self.__money_in_kop() * self.__abs(k)
        return Money(kop=new_money_in_kop)

    def __gt__(self, other_money):
        return self.__money_in_kop() > other_money.__money_in_kop()

    def __lt__(self, other_money):
        return not (self.__gt__(other_money))

    def __eq__(self, other_money):
        return self.__money_in_kop() == other_money.__money_in_kop()

    def __ne__(self, other_money):
        return not self.__eq__(other_money)

    def convert(self):
        data = urllib.request.urlopen(self.__url).read()
        data_dict = json.loads(data)
        usd_key = data_dict['Valute']['USD']['Value']
        eur_key = data_dict['Valute']['EUR']['Value']
        new_money_in_usd = Money(kop=self.__money_in_kop() / usd_key)
        new_money_in_eur = Money(kop=self.__money_in_kop() / eur_key)
        return [new_money_in_usd, new_money_in_eur]
