# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.
 class SuperStr(str):
     def is_repeatanse(self,s):
         for i in self.split(s):
             if i != '':
                 return False
         return True
     def is_poly(self):
         return self ==self[::-1]
         
             
 n = SuperStr('ssssssss')
 print(n.is_repeatanse('ss'))
 print(n.is_poly())
