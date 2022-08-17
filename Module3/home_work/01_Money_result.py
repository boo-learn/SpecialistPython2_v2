import json
import urllib.request

class Money:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        if self.value2 > 99:
            self.value1 += self.value2 // 100
            self.value2 = self.value2 % 100

    def to_decimal(self):
        return self.value1 * 100 + self.value2

    def __str__(self):
        return f"{self.value1}руб. {self.value2}коп."

    def addition(self, other_sum):
        return f'{(self.to_decimal() + other_sum.to_decimal()) // 100}руб. '\
                f'{(self.to_decimal() + other_sum.to_decimal()) % 100}коп.'\
        

    def subtract(self, other_sum):        
        if self.to_decimal() < other_sum.to_decimal():
            return f"Не возможно"
        else:            
            return f'{(self.to_decimal() - other_sum.to_decimal()) // 100}руб. '\
                    f'{(self.to_decimal() - other_sum.to_decimal()) % 100}коп.'\

    def multip(self, x):
        return f'{(self.to_decimal() * x) // 100}руб. '\
                    f'{(self.to_decimal() * x) % 100}коп.'\

    def compare(self, other_sum):
        if self.to_decimal() > other_sum.to_decimal():
            return f'sum1 > sum2'
        elif self.to_decimal() < other_sum.to_decimal():
            return f'sum2 > sum1'
        else:
            return f'Они равны'

    def percent(self, perc):
        perc1 = Money(round((self.to_decimal() * perc / 100) // 100), 
                    (round(self.to_decimal() * perc / 100) % 100))
        return perc1

    def convert(self):
        data = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read()
        data_dict = json.loads(data)
        kurs = data_dict['Valute']['USD']['Value']        
        return f'{round((self.to_decimal() / (kurs * 100)) // 100)}дол. '\
            f'{round((self.to_decimal() / kurs) % 100)}цент.'\
        

perc = 20
sum1 = Money(20, 130)
sum2 = Money(40, 570)
print(sum1)
print(sum2)
print(sum2.convert())
print(sum2.percent(perc))
