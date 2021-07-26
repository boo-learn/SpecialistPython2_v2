import urllib.request

class Money:
    def __init__(self, rub, kop):
        self.rub = rub + kop//100
        self.kop = kop % 100
        self.total_kop = rub * 100 + kop
        
    def __str__(self):
        Money_str = f"{self.rub}руб.{self.kop}коп."
        return Money_str    
    
    def __add__(self, other):
        return Money(0, self.total_kop + other.total_kop)

    def __sub__(self, other):
        return Money(0, self.total_kop - other.total_kop)

    def __mul__(self, other):
        return Money(0, self.total_kop * other)
    
    def __gt__(self, other):
        return self.total_kop > other.total_kop
    
    def __lt__(self, other):
        return self.total_kop < other.total_kop

    def __mod__(self, perc):
        return Money(0, round(self.total_kop * perc/100))
    
    def convert(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        USD = self.total_kop / (requests.get(url).json()["Valute"]["USD"]['Value'] * 100)
        EUR = self.total_kop / (requests.get(url).json()["Valute"]["EUR"]['Value'] * 100)
        return f'USD = {USD}; EUR = {EUR}'
