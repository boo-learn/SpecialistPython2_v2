# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.
class SuperStr (str):

    def is_repeatance(self, s: str):
        if s in self:
            s += s
        return self == s


    def is_palindrome(self):
        return self == self[::-1]

my_str = SuperStr('12321')
print(my_str.is_palindrome())

my_str = SuperStr('123123')
print(my_str.is_repeatance('120'))
