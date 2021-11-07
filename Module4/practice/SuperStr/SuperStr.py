# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

class SuperStr(str):
    def is_repeatance(self, s):
        if len(self) % len(s) == 0 and s* (len(self) // len(s)) in self:
            return True
        return False

    def is_palindrome(self):
        if self == self[::-1]:
            return True
        return False


st = SuperStr('qwqw')

print(st.is_repeatance('qw'))


print(st.is_palindrome())
