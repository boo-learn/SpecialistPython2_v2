# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

class SuperStr(str):

    def is_repeatance(self, s):
        temp = ''
        for i in range(int(len(self) / len(s))):
            temp += s
        return self == temp

    def is_palindrome(self):
        return self.lower() == self[::-1].lower()

a = SuperStr('aa')

print(a.is_palindrome())
print(a.is_repeatance('aa'))
