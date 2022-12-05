import urllib.request
import json


class Money:
    
       
    def __init__(self, rubles=0, pennies=0) -> None:
        self.rubles = rubles
        self.pennies = pennies
        self.correct_money_input()

    def show(self):
        return f'{self.rubles} руб {self.pennies} коп'

    def correct_money_input(self):
        if self.pennies // 100 != 0:
            self.rubles = self.rubles + self.pennies // 100
            self.pennies %= 100           

    def __str__(self):
        self.correct_money_input()
        return f'{self.rubles} руб {self.pennies} коп'
        
    def __add__(self, other_money_sum):
        temp_results = Money()     
        temp_results.rubles = self.rubles + other_money_sum.rubles
        temp_results.pennies = self.pennies + other_money_sum.pennies
        return f'{str(temp_results)}'

    def __sub__(self, other_money_sum):        
        temp_results = Money()
        if self.pennies >= other_money_sum.pennies: 
            temp_results.rubles = self.rubles - other_money_sum.rubles
            temp_results.pennies = self.pennies - other_money_sum.pennies
            return f'{str(temp_results)}'
        else:             
            self.rubles -= 1
            self.pennies += 100
            temp_results.rubles = self.rubles - other_money_sum.rubles
            temp_results.pennies = self.pennies - other_money_sum.pennies
            return f'{str(temp_results)}'

    def __mul__(self, value):
        temp_results = Money()
        temp_results.rubles = self.rubles * value
        temp_results.pennies = self.pennies * value
        return f'{str(temp_results)}'

    def __gt__(self, other_money_sum):
        return self.rubles >= other_money_sum.rubles and self.pennies > other_money_sum.pennies
                
    def __lt__(self, other_money_sum):
        return self.rubles <= other_money_sum.rubles and self.pennies < other_money_sum.pennies

    def __eq__(self,other_money_sum):
        return self.rubles == other_money_sum.rubles and self.pennies == other_money_sum.pennies

    def __ne__(self,other_money_sum):
        return not self.__eq__(other_money_sum)

    def __mod__(self,percent_value):
        temp_results = Money()
        temp_results.pennies = round(((self.rubles * 100 + self.pennies) * percent_value) / 100)
        return f'{str(temp_results)}'

    def convert(self):        
        rubles_pennies = float('.'.join([str(self.rubles), str(self.pennies)]))
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        convert_result = {}
        data = urllib.request.urlopen(url).read()
        data_json = json.loads(data)
        convert_result['usd'] = round(rubles_pennies / float(data_json['Valute']['USD']['Value']), 2)
        convert_result['eur'] = round(rubles_pennies / float(data_json['Valute']['EUR']['Value']), 2)
        return convert_result
        
            
          
money_sum1 = Money(45,11)
print(money_sum1)
money_sum2 = Money(5,94)
print(money_sum2)
money_result = money_sum1 + money_sum2
print(money_result)

money_sum3 = Money(45,79)
money_sum4 = Money(5,99)
money_result = money_sum3 - money_sum4
print(money_result)

money_sum5 = Money(45,179)
money_result = money_sum5 * 3
print(money_result)

print(money_sum2 > money_sum4)
print(money_sum2 < money_sum4)


money_sum6 = Money(5,65)
money_sum7 = Money(5,67)
print(money_sum6 > money_sum7)
print(money_sum6 < money_sum7)

print(money_sum2 == money_sum4)
print(money_sum2 != money_sum4)

money_sum8 = Money(20, 60)
percent_sum = money_sum8 % 21
print(percent_sum)

money_sum9=Money(1200,195)
print(money_sum9.convert())

