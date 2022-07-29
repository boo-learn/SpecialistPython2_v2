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
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        balance = self.get_balance()
        if amount > balance:
            raise ValueError('Баланс меньше снимаемой суммы')
        self.set_balance(balance - amount)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.get_balance()} руб. паспорт: {self.passport} т.{self.phone_number}"

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.get_balance()} руб."


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)

# Смотрим баланс:
print(account1)

# Вносим сумму на счет:
account1.deposit(600)
print(account1)

# Снимаем деньги со счета:
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)

# Пробуем снять еще:
try:
    account1.withdraw(1000)
except ValueError as e:
    print(e)
print(account1)
