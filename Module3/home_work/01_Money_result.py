import json
import urllib.request

class Money:
    def __init__(self, value1, value2):
        self.value1 = value1 + value2 // 100
        self.value2 = value2 % 100

    def to_decimal(self):        
        return self.value1 * 100 + self.value2

    def __str__(self):
        return f"{self.value1}руб. {self.value2}коп."       

    def __add__(self, other_sum):
        return Money((self.to_decimal() + other_sum.to_decimal()) // 100, 
                    (self.to_decimal() + other_sum.to_decimal()) % 100)        

    def __sub__(self, other_sum):        
        if self.to_decimal() < other_sum.to_decimal():
            return f"Не возможно"
        else:
            return Money ((self.to_decimal() - other_sum.to_decimal()) // 100, 
                        (self.to_decimal() - other_sum.to_decimal()) % 100)          

    def __mul__(self, x):
        return Money((self.to_decimal() * x) // 100, 
                    (self.to_decimal() * x) % 100)

    def compare(self, other_sum):
        if self.to_decimal() > other_sum.to_decimal():
            return f'sum1 > sum2'
        elif self.to_decimal() < other_sum.to_decimal():
            return f'sum2 > sum1'
        else:
            return f'Они равны'

    def percent(self, perc):
        return Money(round((self.to_decimal() * perc / 100) // 100), 
                    (round(self.to_decimal() * perc / 100) % 100))        

    def convert(self, valute):
        self.valute = valute
        return f'{int(self.to_decimal() / (self.valute * 100) // 1)},'\
            f'{round((self.to_decimal() / self.valute) % 100)}'\

data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
usd = json.loads(data)['Valute']['USD']['Value']
eur = json.loads(data)['Valute']['EUR']['Value']      
perc = 50
sum1 = Money(20, 30)
sum2 = Money(150, 570)
print(sum1)
print(sum2)
print(sum2.convert(usd))
