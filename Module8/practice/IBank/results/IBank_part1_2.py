class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance  # Закрываем прямой доступ к балансу

    @property
    def balance(self):
        return self.__balance

    def __full_info(self):  # Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):  # Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        return f"{self.name} баланс: {self.__balance} руб."

    def deposit(self, amount):  # Внесение суммы на текущий счет: amount - сумма внесения
        self.__balance += amount

    def withdraw(self, amount):  # Снятие суммы с текущего счета: amount - сумма снятия
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError (f"Недостаточно средств")


# Создаем тестовый аккаунт:
account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", start_balance=500)

# Смотрим баланс:
print(account1.balance)

# Вносим сумму на счет:
account1.deposit(200)
print(account1.balance)

# Снимаем деньги со счета:
try:
    account1.withdraw(600)
except ValueError as e:
    print(e)
print(account1.balance)

# Пробуем снять еще:
try:
    account1.withdraw(300)
except ValueError as e:
    print(e)
print(account1.balance)

# Пробуем снять еще:
try:
    account1.withdraw(100)
except ValueError as e:
    print(e)
print(account1.balance)
