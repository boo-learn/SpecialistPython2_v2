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
            target_account.balance += amount
            self.balance -= amount
        else:
            raise Exception('Недостаточно средств для проведения операции')

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount:
            self.balance += amount

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            raise Exception('Недостаточно средств для проведения операции')

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."


iv = Account('Иван', '5555 222222', '+7-913-976-7642', 100)
an = Account('Андрей', '5545 112222', '+7-913-987-7642', 200)
iv.withdraw(10)
print(iv.balance)
iv.deposit(100)
print(iv.balance)
iv.transfer(an, 15)
print(iv.balance)
print(an.balance)
