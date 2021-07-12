# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_repeatance(s), который принимает 1 аргумент s и возвращает True или False
# в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s.
# Вернуть False, если s не является строкой, необходимо преобразовать к строке.

# 2. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

class SuperStr(str):
    def is_palindrome(self):
        return self.lower() == self[::-1].lower()

    def is_repeatance(self, s):
        if type(s) is not str or len(s) == 0 or len(self) < len(s) or len(self) % len(s) != 0:
            return False
        n_matches = len(self) // len(s)
        for i in range(n_matches):
            l_range = i * len(s)
            r_range = l_range + len(s)
            if self[l_range:r_range] != s:
                return False
        return True


s = SuperStr("ababab")
print(s.is_palindrome())
print(s.is_repeatance("ab"))
