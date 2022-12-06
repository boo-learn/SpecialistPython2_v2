class Roman:
        
    def __init__(self, number):
        self.number = number
        self.converted_string_number = str(self.number)
        self.number_lenght = len(str(self.number))
        if self.number_lenght < 4:
            self.converted_string_number = '0' * (4 - self.number_lenght) + self.converted_string_number
        self.complex_simple()
        
    def __str__(self):
        return f'{self.roman_number}'
    
    def complex_simple(self):
        self.roman_number = ''
        roman_numbers = [['M'],['C', 'D', 'M'] , ['X', 'L', 'C'], ['I', 'V', 'X']]
        iter = 0
        for value in self.converted_string_number:
            if int(value) == 0:
                roman_numbers[iter].clear()
            elif iter == 0:
                self.roman_number = roman_numbers[0][0] * int(value)
                iter +=1
                continue

            if int(value) >=1 and int(value) <=3:
                self.roman_number = self.roman_number + roman_numbers[iter][0] * int(value)
            elif int(value) ==4:
                self.roman_number = self.roman_number + ''.join([roman_number for roman_number in roman_numbers[iter][0:2]])
            elif int(value) ==5:
                self.roman_number = self.roman_number + roman_numbers[iter][1]
            elif int(value) > 5 and int(value) <=8:
                self.roman_number = self.roman_number + roman_numbers[iter][1] + roman_numbers[iter][0] * (int(value) - 5)
            elif int(value) == 9:
                self.roman_number = self.roman_number + roman_numbers[iter][0] + roman_numbers[iter][2]
            iter +=1


    def __add__(self,other_number):
        return Roman(self.number + other_number.number)
        
    def __sub__(self,other_number):
        return Roman(self.number - other_number.number)

    def __mul__(self, multiple_number):
        return Roman(self.number * multiple_number)
    
    def __gt__(self, other_number):
        if self.number > other_number.number:
            print(f'{self.roman_number} > {other_number.roman_number}')
        else:
            print(f'False')
        
    def __lt__(self, other_number):
        if self.number < other_number.number:
            print(f'{self.roman_number} < {other_number.roman_number}')
        else:
            print(f'False')

    def __eq__(self,other_number):
        if self.roman_number == other_number.roman_number: 
            print(f'{self.roman_number} == {other_number.roman_number}')
        else:
            print(f'False')
    def __ne__(self,other_number):
        if self.roman_number != other_number.roman_number: 
            print(f'{self.roman_number} != {other_number.roman_number}')
        else:
            print(f'False')

n1 = Roman(10)
n2 = Roman(14)
print(n1)  
print(n2)  
n3 = Roman(5)
n4 = Roman(1)
n5 = n3 + n4
print(n5)
n6 = Roman(15)
n7 = Roman(5)
n8 = n6 - n7
print(n8)
n9 = Roman(999)
n9 *= 4
print(n9)

n6 > n7
n7 < n6

n10 = Roman(15)
n10 == n6
n10 == n7
n1 != n5

# ограничение: 4-значные числа.
# Алгоритм
# 1. Выделяем (если есть) количество целых тысяч.
# Полученное значение позволить сгенерировать строку с n количеством «M» (читаем, n*1000).
# Пример: 2012 после первого пункта даст «MM»
#
# 2. Получаем остаток после деления на 1000, чтобы выделить в дальнейшем следующие значения.
#
# 3. Выделяем (если возможно), целые 500. При этом учитываем что если полученное значение равно 4 (5+4=9),
# то следует записывать как значение 1000-100, что в римский СС равнозначно «CM».
# Пример: 1887 после этого пункта даст нам «MD».
# 1945 соответственно «MCM».
#
# 4. Получаем остаток от деления на 500.
#
# 5. Делим на 100 чтобы выделить целые сотни и складываем к предыдущему результату. Учитываем что если получили 4,
# что равнозначно 400, то записываем как 500-100, то есть «CD».
# Пример: 1709 даст после этого шага «MDCCC».
#
# 6. Получаем остаток от деления на 100.
#
# 7. Выделяем из него целые полсотни. Если значение будет равно 4 (то есть 90), то записываем как 100-10,
# что равно «XC». Иначе прибавляем к строке «L»
# Пример: 1986 после всего выдаст нам «MCML».
#
# 8. Выделяем остаток от 50.
#
# 9. Выделяем целое количество десятков и складываем к строке n раз символ «X».
# При этом учитываем что 40 пишется как 50-10, то есть «XL».
# Пример: 1986 после всего выдаст нам «MCMLXXX».
#
# 10. Получаем остаток от деления на 10. Этот шаг отличается от других тем,
# что можно сразу приравнять остаток к его эквиваленту. 1=I, 7=VII и так далее.
#
# После перебора числа этим алгоритмом мы получаем примерно такое:
# 2012 == MMXII
