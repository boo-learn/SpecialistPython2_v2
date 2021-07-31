# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount, target=None):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount, target=None):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount, target=None):
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


# self.history.append({'event': 'deposit', 'amount': amount, 'fee': 0})
class Operation:
    DEPOSIT = "пополнение"
    WITHDRAW = "списание"
    TRANSFER = "перевод"
    INCOME = "поступление"

    def __init__(self, type, amount, fee=0, target=None, sender=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.sender = sender


    def __str__(self):
        if self.target is not None:
            target_name = self.target.name
        else:
            target_name = ""
        return f"Операция: {self.type} на сумму {self.amount} {target_name} с комиссией {self.amount*(self.fee/100):.2f}"


class Account(AccountBase):
    FEE = 2

    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []

    def transfer(self, target_account, amount, record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)
        if record:
            op = Operation(Operation.TRANSFER, amount, target=target_account, fee=Account.FEE)
            self.history.append(op)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        if record:
            op = Operation(Operation.DEPOSIT, amount)
            self.history.append(op)
            
    def __has_money(self, amount):
        return self.balance < amount * (1 + Account.FEE / 100)

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__has_money(amount):
            raise ValueError("На счёте недостаточно средств")
        self.balance -= amount * (1 + Account.FEE / 100)
        if record:
            op = Operation(Operation.WITHDRAW, amount, fee=Account.FEE)
            self.history.append(op)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self.name} баланс:{self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        if self.target is not None:
            target_name = f' на счете клиента {self.name} {self.balance} руб.'


    def show_history(self):
        hist_str = ""
        for operation in self.history:
            hist_str += str(operation) + "\n"
        return hist_str

#     def show_balance(self, amount):
#         return amount


class CreditAcc(Account):
    
    NEG_FEE = 0.05
    POS_FEE = 0.02
    
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.__negative_limit = negative_limit

    def __repr__(self):
        return f"{self.name} K-account баланс: {self.balance} руб."
    
    def __has_money(self, amount):
        return (self.balance + abs(self.__negative_limit)) < amount * (1 + Account.FEE / 100)
    
    # def transfer(self, target_account, amount):
    #     self.withdraw(amount)
    #     target_account.deposit(amount)
    
# Сюда отправляем готовое решение IBank часть-3
# class Operation:
#     # TODO: сюда копируем реализацию класса Operation из предыдущей задачи
#     pass



# class Account:
#     pass
# 
#     # TODO: сюда копируем реализацию класса Account из предыдущей задачи
#     # TODO: добавляем комиссию
#     #  и переход/восстановление их архива. Свойство: in_archive --> True, если аккаунт в архиве, и False - если нет
    def to_archive(self):
        """
        Переводим аккаунт в архив
        """
        self.in_archive = True
# 
    def restore(self):
        """
        Восстанавливаем из архива
        """
        self.in_archive = False   
    
    

account1 = Account("Петр", "3002 123456", "+7-900-600-10-20", start_balance=300)
account2 = Account("Иван", "3002 123477", "+7-900-600-10-22", start_balance=100)
# print(account1)  # account.__str__()
account1.deposit(500)
# account1.show_balance()
# account1.withdraw(600)
# print(account1)
# try:
#     account1.transfer(account2, 200)
# except ValueError as e:
#     print(e)

print(account1.show_history())
