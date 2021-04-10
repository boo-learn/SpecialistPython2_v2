# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

# 2. метод only_numbers(), возвращает все цифры строки.
# Пример: s = SuperStr("10 долларов - это примерно 775 рублей")
# s.only_numbers()  --> "10775"


class SuperStr(str):
    def is_palindrome(self):
        return list(reversed(self)) == list(self)

    def only_numbers(self):
        nums = ""
        for let in self:
            if let.isnumeric():
                nums += let
        return nums


s = SuperStr("test")
if s.is_palindrome():
    print(f"{s} палиндром")
else:
    print(f"{s} НЕ палиндром")

s = SuperStr("10 долларов - это примерно 775 рублей")
