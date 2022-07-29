import urllib.request

class Money:
    
    def __init__(self, rub = 0, cop = 0):
        self.rub = rub 
        self.cop = cop
        if self.cop>99:
            self.rub += cop//100
            self.cop = cop%100
     
     
    def __str__(self):
        return f"{self.rub} руб {self.cop} коп"    
     
    def __add__(self,other_sum):
        rub = self.rub + other_sum.rub
        cop = self.cop + other_sum.cop
        if cop>99:
            rub += cop//100
            cop = cop%100
        return f"{round(rub)} руб {round(cop)} коп"
    
    def __sub__(self,other_sum):
        rub = self.rub - other_sum.rub
        cop = self.cop - other_sum.cop
        if self.cop>99:
            rub += cop//100
            cop = cop%100
        return f"{round(rub)} руб {round(cop)} коп"
    
    def __mul__(self,other_sum):
        rub = self.rub * other_sum.rub
        cop = self.cop * other_sum.cop
        if cop>99:
            rub += cop//100
            cop = cop%100
        return f"{round(rub)} руб {round(cop)} коп"
    
    def __truediv__(self,other_sum):
        rub = self.rub / other_sum.rub
        cop = self.cop / other_sum.cop
        if cop>99:
            rub += cop//100
            cop = cop%100
        return f"{round(rub)} руб {round(cop)} коп"
                   
            
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

print(money_sum1 - money_sum2)


# Не хватает времени разобраться с этим. Будет время позже буду разбираться
# data = urllib.request.urlopen(https://www.cbr-xml-daily.ru/daily_json.js).read()
# 
# data_dict = json.loads(data)
# 
# print(data)
            
            
