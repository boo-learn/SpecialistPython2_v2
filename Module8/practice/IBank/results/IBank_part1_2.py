class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance  # Закрываем прямой доступ к балансу

    # TODO: совместно с преподавателем реализуйте getter для просмотра баланса
    #  Можете попробовать самостоятельно: https://pythobyte.com/using-getters-and-setters-in-python-5205-840ed13f/

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        return

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance >= 0 and amount <= self.__balance:
            self.__balance -= amount
            return
        raise ValueError

    @property
    def balance(self):
        return self.__balance

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)

# Смотрим баланс:
print(account1)
# print(account1._Account__balance)
print(account1.balance)

# Вносим сумму на счет:
account1.deposit(600)
print(account1)

account1.withdraw(1000)
print(account1.balance)
account1.withdraw(150)
print(account1.balance)

# # Снимаем деньги со счета:
# try:
#     account1.withdraw(1000)
# except ValueError as e:
#     print(e)
# print(account1)
#
# # Пробуем снять еще:
# try:
#     account1.withdraw(1000)
# except ValueError as e:
#     print(e)
# print(account1)
