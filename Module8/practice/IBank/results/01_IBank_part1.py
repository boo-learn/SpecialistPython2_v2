# Сюда отправляем готовое решение IBank часть-1
# from generators import get_user_data
from abc import ABC, abstractmethod

class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposite(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        pass

    @abstractmethod
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"..."

    @abstractmethod
    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"..."

#def __init__(self, name, passport8, phone_number, start_balance=0):
#        self.name = name
#        self.passport8 = passport8
#        self.phone_number = phone_number
#        self.balance = start_balance
class Account (AccountBase):
    def transfer(self, target_account, amount):
        pass
    
    def deposite(self, amount):
        self.balance+=amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance-=amount
        else:
            print ("not enough money")
    
    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        print (self.name,', balance:', self.balance, ', passport:', self.passport8)
    
    def __repr__(self):
        pass
    
acc1 = Account('Eldar', 12345678, '+7-900-800-77-66')
print(acc1.balance)
acc1.deposite(100)
print(acc1.balance)
acc1.withdraw(20)
print(acc1.balance)
acc1.full_info()
