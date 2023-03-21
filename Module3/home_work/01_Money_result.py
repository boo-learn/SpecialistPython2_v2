import json
import urllib.request

class Money:
    def __init__(self, rub, kop=0):
        self.rub = rub
        self.kop = kop
        self.total = self.rub * 100 + self.kop
        self.total_rub = self.total/100

    def convert(self, url):
        data = urllib.request.urlopen(url).read()
        data_dict = json.loads(data)
        valutes = ['USD', 'EUR']
        for valute in valutes:
            kurs = data_dict['Valute'][valute]['Value']
            print(f'{round(self.total_rub / kurs,2)} {valute}')

    
    def __add__(self, second):
        self.total = (self.total + second.total)
        return(self)
        
        #return f'{(self.total + second.total)//100}руб {(self.total + second.total)%100}коп'
    
    def __sub__(self, second):
        self.total = (self.total - second.total)
        return(self)
    
        #return f'{(self.total - second.total)//100}руб {(self.total - second.total)%100}коп'
    
    def __mul__(self, num):
        self.total = (self.total * num)
        return(self)
    
        #return f'{(self.total * num)//100}руб {(self.total * num)%100}коп'
    
    def __mod__(self, proc):
        self.total = round(self.total * proc / 100)
        return(self)
    
        #return f'{proc_ot_summ//100}руб {proc_ot_summ%100}коп'
    
    def __gt__(self, second):
        #return self.total > second.total
        # не совсем понимаю что происходит при решении ниже.      
        if self.total > second.total:
            return f'{self.total//100}руб {self.total%100}коп больше {second.total//100}руб {second.total%100}'
        elif self.total < second.total:
            return f'{self.total//100}руб {self.total%100}коп меньше {second.total//100}руб {second.total%100}'
        elif self.total == second.total:
            return f'{self.total//100}руб {self.total%100}коп равны {second.total//100}руб {second.total%100}'

    def __it__(self, second):
        return self.total < second.total
    
    def __eq__(self, second):
        return self.total == second.total
    
    def __str__(self):
        return f'{self.total//100}руб {self.total%100}коп'


money_sum1 = Money(100, 189)
money_sum2 = Money(100, 189)

print(money_sum1)
print(money_sum2)

#print(money_sum1 + money_sum2)

#print(money_sum1 - money_sum2)

#print(money_sum1 * 10)

#print(money_sum1 > money_sum2)

print(money_sum1 < money_sum2)

print(money_sum1 == money_sum2)

#print(money_sum1 % 21)

#url = "https://www.cbr-xml-daily.ru/daily_json.js"
#money_sum1.convert(url)
#money_sum2.convert(url)
