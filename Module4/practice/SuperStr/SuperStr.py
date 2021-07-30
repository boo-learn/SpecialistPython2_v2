# Разработать класс SuperStr, который наследует функциональность
# стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и
# возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым
# количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать
# к строке.

# 2. метод is_palindrome(), который возвращает True или False в
# зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.


class SuperStr(str):

    def is_repeatence(self, s):
        if not isinstance(s, str):
            return False
        return self == s * (len(self) // len(s))

    def is_palindrome(self):
        return self == self[::-1]


print(SuperStr('121').is_palindrome())
print(SuperStr('').is_palindrome())
print(SuperStr(13).is_palindrome())
print(SuperStr('1213').is_palindrome())
print(SuperStr('121212').is_repeatence('12'))
print(SuperStr('121212').is_repeatence('121'))
