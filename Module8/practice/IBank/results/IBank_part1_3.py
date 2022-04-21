class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.__balance>amount:
            target_account.__balance+=amount
            self.__balance-=amount
        else:
            raise ValueError('Недостаточно средств на счете')


    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - amount > 0:
            self.__balance -= amount
        else:
            raise ValueError('Недостаточно средств на счете')

    def full_info(self):
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.__balance} руб."


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
try:
    account1.transfer(account2, 500)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
try:
    account1.transfer(account2, 600)
except ValueError as e:
    print(e)

# Проверяем изменения баланса:
print(account1)
print(account2)

