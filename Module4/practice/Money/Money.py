import requests
class Money:
    def __init__(self,rub,kop):
        self.kop=rub*100+kop
    def __str__(self):
        return f"{int(self.kop//100)}руб {int(round(self.kop%100))}коп"
    def __add__(self,other):
        return Money(0,self.kop+other.kop)
    def __mod__(self,percent):
        return Money(0,self.kop*percent/100)
    def convert(self):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        # Отправляем запрос на указанный url
        response = requests.get(url)
        data=response.json()
        currencies=data['Valute']
        usd=currencies["USD"]["Value"]
        eur = currencies["EUR"]["Value"]
        return f"{round(self.kop/100/usd,2)}$ или {round(self.kop/100/eur,2)}Euro"


# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1) # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

# Создаем сумму
money_sum1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum1 % 21

print(percent_sum)  # 4руб 33коп

print(money_sum1.convert())
