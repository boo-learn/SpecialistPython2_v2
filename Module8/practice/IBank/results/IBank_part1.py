# Сюда отправляем готовое решение IBank часть-1
class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
        else:
            raise ValueError("Перевод невозможен. Недостаточно средств на счете")

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Недостаточно средств на счете")

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


account1 = Account("Иван", "1122 523632", "+7-900-200-02-03")
print(account1)
print(account1.full_info())
account1.deposit(100)
print(account1)
account1.withdraw(50)
print(account1)
account2 = Account("Вася", "3344 123456", "+7-911-156-25-78", 1000)
account1.transfer(account2, 30)
print(account1)
print(account2)
