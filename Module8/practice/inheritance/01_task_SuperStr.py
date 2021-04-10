# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

# 2. метод only_numbers(), возвращает все цифры строки.
# Пример: s = SuperStr("10 долларов - это примерно 775 рублей")
# s.only_numbers()  --> "10775"

class SuperStr(str):
    def is_palindrome(self):
        rev = ''.join(reversed(self)) 
        if (self == rev): 
            return True
        return False
    
    def only_numbers(self):
        num_str = ''
        for char in self:  
            if char.isnumeric():
                num_str += char
        return num_str


s = SuperStr("textrtxet")
if s.is_palindrome():
    print(f"{s} палиндром")
else:
    print(f"{s} НЕ палиндром")
    
s2 = SuperStr("10 долларов - это примерно 775 рублей")
print(s2.only_numbers())
