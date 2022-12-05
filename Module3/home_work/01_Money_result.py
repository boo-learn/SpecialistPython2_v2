import urllib.request

class Money:
    
        def __init__(self, rubls = 0, kops = 0) -> None:
            self.rubls = rubls
            self.kops = kops
            self.conversion_money()
            
        def conversion_money(self) -> None:
            while self.kops >= 100:
                self.rubls += 1
                self.kops -= 100

        def __str__(self):
            self.conversion_money()
            return f'{self.rubls} руб {self.kops} коп'
        
        def __add__(self, other):
            temp_m = Money()
            temp_m.rubls = self.rubls + other.rubls
            temp_m.kops = self.kops + other.kops
            return f'{str(temp_m)}'

    
        def  __sub__(self, other):
            temp_m = Money()
            if self.kops < other.kops:
                temp_m.rubls = self.rubls - other.rubls - 1
                temp_m.kops = self.kops - other.kops + 100
                return f'{str(temp_m)}'
            else:
                temp_m.rubls = self.rubls - other.rubls
                temp_m.kops = self.kops - other.kops
                return f'{str(temp_m)}'
         
        def __mul__(self, number):
            self.rubls *= number
            self.kops *= number
            return f'{str(self)}'

        def __lt__(self, other):
            return self.rubls <= other.rubls and self.kops < other.kops
        
        def __gt__(self,other):
            return self.rubls >= other.rubls and self.kops > other.kops
        
        def __eq__(self,other):
            return self.rubls == other.rubls and self.kops == other.kops
        
        def __ne__(self,other):
            return not self.rubls == other.rubls and self.kops == other.kops
        
        def __mod__(self, procent):
            temp_M = Money()
            temp_M.kops = round((self.rubls * 100 + self.kops) * procent / 100)
            return f'{str(temp_M)}'

#  Не понимаю реализацию
#         def convert(self): 
#             data = urllib.request.urlopen(url).read()
            


sum1 = Money(18, 15)
sum2 = Money(12, 420)

print(sum1 + sum2)
print(sum1 - sum2)
print(sum1 * 5)

print(sum1 > sum2)
print(sum1 < sum2)
print(sum1 == sum2)
print(sum1 != sum2)


print(sum2 % 21)
