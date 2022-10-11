import urllib.request
import json

class Money:
    def __init__(self, ruble, penny):
        self.ruble = ruble
        self.penny = penny
    
    def __str__(self):
        if self.penny > 99 or self.penny < 0: 
            self.ruble += self.penny // 100 
            self.penny = self.penny % 100
        return f"{self.ruble} рублей {self.penny} копеек"
        
    def __add__(self, other_money):
        return Money(self.ruble + other_money.ruble, self.penny + other_money.penny)
    
    def __sub__(self,other_money):
        return Money(self.ruble - other_money.ruble, self.penny - other_money.penny)
    
    def __mul__(self, x):
        return Money(self.ruble * x, self.penny * x)
    
    def __gt__(self, other_money):
        return self.ruble*100 + self.penny > other_money.ruble*100 + other_money.penny
    
    def __lt__(self, other_money):
        return self.ruble*100 + self.penny < other_money.ruble*100 + other_money.penny
    
    def __eq__(self, other_money):
        return self.ruble*100 + self.penny == other_money.ruble*100 + other_money.penny
    
    def __mod__(self, x):
        allpenny = round(((self.ruble * 100 + self.penny) * x / 100))
        return Money(allpenny // 100 , allpenny % 100)
    
    def convert(self,money_type):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js' 
        data = urllib.request.urlopen(url).read() 
        data_dict = json.loads(data)
        return round((self.ruble * 100 + self.penny) / 100 / data_dict["Valute"][money_type]["Value"],2)
    
    
# money_sum1 = Money(20, 120)
# # Выводим сумму, с учетом минимального кол-ва копеек
# print(money_sum1) 

# # Создаем две денежные суммы
# money_sum1 = Money(20, 60)
# money_sum2 = Money(10, 45)

# # Складываем суммы
# money_result = money_sum1 + money_sum2
# print(money_result)  # 31руб 5коп

# if money_sum1 > money_sum2:
#     print(f'{money_sum1} больше {money_sum2}')
# elif money_sum1 > money_sum2:
#     print(f'{money_sum1} меньше {money_sum2}')
# else:
#     print(f'{money_sum1} и {money_sum2} равны')  

# # Создаем две денежные суммы
# money_sum1 = Money(20, 60)

# # Находим 21% от суммы
# percent_sum = money_sum1 % 21

# print(percent_sum)  # 4руб 33коп

# money1 = Money(80,50)
# convert_to = "JPY"
# print(convert_to, money1.convert(convert_to))
