специально загрузил не совсем рабочий вариант

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
        if self.__balance < amount:
            raise ValueError("Недостаточно денег")
        elif self.__balance > amount:
            self.__balance -= amount
            target_account[self.__balance] += amount

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount:
            raise ValueError('Недостаточно средств')
        else:
            self.__balance -= amount

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


account1 = Account("Иван", "3230 634563", "+7-900-765-12-34", 1000)
account2 = Account("Алексей", "+7-901-744-22-99", "3232 456124", 200)

print(account1)
print(account2)

# Переводим деньги с первого аккаунт на второй:
account1.transfer(account2, 500)

# Проверяем изменения баланса:
print(account1)
print(account2)

# Переводим еще с первого аккаунт на второй:
account1.transfer(account2, 600)

# Проверяем изменения баланса:
print(account1)
print(account2)
