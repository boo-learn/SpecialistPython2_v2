class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

    def full_info(self):
        return f"{self.name} баланс: {self.balance}. Паспорт: {self.passport} т. {self.phone_number}"


    def __repr__(self):
        return f"{self.name} баланс: {self.balance}."


    def deposit(self, amount):
        new_balance = self.balance + amount
        self.balance = new_balance
        return new_balance

    def withdraw(self, amount):
        new_balance = self.balance - amount
        if new_balance >= 0:
            self.balance = new_balance
            return new_balance
        else:
            return ValueError




# Создаем тестовый аккаунт:
account1 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 500)

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

