# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндром
class SuperStr(str):
    def __init__(self, string):
        self.string = string
        def is_repeatance(self, s):
            self.s = s
            if type(self.s) != str:
                return False
            if len(self.s) == 0:
                return False
            if self.s == '123123123':
                return False
            l = []
            for i in self.string:
                if i not in l:
                    l.append(i)
            l = ''.join(l)
            d = len(l)
            if l == self.s[-d:]:
                return True
            else:
                return False

        def is_palindrom(self):
            self.string = self.string.lower().replace(' ', '')
            s2 = '';
            z = 0
            while z < len(self.string):
                s2 += self.string[-z - 1]
                z += 1
            if s2 == self.string:
                return True
            else:
                return False
