# Разработать класс SuperStr, который наследует функциональность стандартного типа str и содержит 2 новых метода:

# 1. метод is_palindrome(), который возвращает True или False в зависимости от того,
# является ли строка палиндромом. Регистрами символов пренебрегать.
# Пустую строку считать палиндромом.

# 2. метод only_numbers(), возвращает все цифры строки.
# Пример: s = SuperStr("10 долларов - это примерно 775 рублей")
# s.only_numbers()  --> "10775"


class SuperStr(str):
    def is_palindrome(self):
        return self.lower() == self[::-1].lower()

    def only_numbers(self):
        string = ""
        for char in self:
            if char.isdigit():
                string += char
        return string


text1 = SuperStr("areera")
text2 = SuperStr("10 долларов - это примерно 775 рублей")
if text1.is_palindrome():
    print(f"{text1} является палиндромом")
else:
    print(f"{text1} не является палиндром")
print(text2.only_numbers())
