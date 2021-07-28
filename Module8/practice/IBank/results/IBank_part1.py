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
        try:
            self.withdraw(amount)
            target_account.deposit(amount)
        except ValueError as error:
            print('Не удалось перевести средства.', error)

    def deposit(self, amount): # TODO простое задание
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
            return
        return ValueError('Недостаточно средств')

    def full_info(self): # TODO простое задание
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport} т. +7-900-200-02-03"

    def __repr__(self): # TODO простое задание
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.balance} руб."

person1 = Account('Анатолий', '3453 233443', '72223344922')

print(person1.full_info())
person1.deposit(500)
print(person1.full_info())
print(person1)
person1.withdraw(300)
print(person1)
person2 = Account('Валентин', '5612 351843', '79934558123')
person1.transfer(person2, 100)
print(person1)
person1.transfer(person2, 300)
print(person1)
