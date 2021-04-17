# from generators import get_user_data
from abc import ABC, abstractmethod
from datetime import datetime

EMPLOYEE_PASSWORD = "123"


class AccountBase(ABC):  # абстрактный класс - от него нельзя наследоваться - просто обозначает структуру
    # для наследуемых классов
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
    def deposit(self, amount):
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


class Transaction:
    DEPOSIT = 'Пополнение счета'
    WITHRAW = 'Снятие'
    TRANSFER = 'Перевод'

    def __init__(self, type, value, user_from=None, user_to=None, fee=0):
        self.date = datetime.now()
        self.type = type
        self.value = value
        self.user_from = user_from
        self.user_to = user_to
        self.fee = fee

    def __repr__(self):
        # if self.type == 'перевод средств':
        #     return f'{self.date}: {self.type} на сумму {round(self.value, 2)} от {self.user_from} ' \
        #            f'на счет пользователя {self.user_to}'
        # else:
        #     return f'{self.date}: {self.type} на сумму {round(self.value, 2)}'
        s = f'{self.date}: {self.type} на сумму {round(self.value, 2)} руб.'
        if self.user_from:
            s += f'  от {self.user_from}'
        if self.user_to:
            s += f' клиенту {self.user_to}\nКомиссия за операцию {round(self.fee, 2)} руб.'
        return s


class Account(AccountBase):
    pasports = []

    def __init__(self, name, passport8, phone_number, start_balance=0):
        try:
            AccountBase.__init__(self, name, passport8, phone_number, start_balance)
            if self.__passport8 in Account.pasports:
                raise ValueError('Аккаунт с таким паспортом уже существует!')
            Account.pasports.append(self.__passport8)

        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
        self.history = []
        self.__fee = 0.02

    def deposit(self, amount, history_flag=True):
        self.balance += amount
        if history_flag:
            self.history.append(Transaction(type=Transaction.DEPOSIT, value=amount))

    def transfer(self, target_account, amount):
        self.withdraw(amount, history_flag=False)
        target_account.deposit(amount, history_flag=False)
        self.history.append(
            Transaction(type=Transaction.TRANSFER, value=amount, user_to=target_account.name, fee=amount * self.fee))
        target_account.history.append(
            Transaction(type=Transaction.TRANSFER, value=amount, user_from=self.name, fee=amount * self.fee))

    def _check_limit(self, amount):
        return self.balance >= amount * (1 + self.fee)

    def withdraw(self, amount, history_flag=True):
        if self._check_limit(amount):
            self.balance -= amount * (1 + self.fee)
            if history_flag:
                self.history.append(Transaction(type=Transaction.WITHRAW, value=amount))
        else:
            raise ValueError('нехватка средств на балансе')

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб.; паспорт: {self.__passport8}; тел. {self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."

    @property
    def fee(self):
        return self.__fee

    @property  # чтение атрибута
    def passport8(self):
        return self.__passport8

    @passport8.setter  # запись атрибута
    def passport8(self, value):
        try:
            self.__passport8 = int(value)
        except ValueError:
            raise ValueError("Номер паспорта должен быть целым числом!")
        if len(value) != 8:
            raise Exception("В номере паспорта должно быть 8 знаков!")

    # def new_history(self, timestamp: datetime.timestamp, transaction_type, value, user_from=None, user_to=' '):
    #     self.history.append([transaction_type, value, timestamp, user_from, user_to])
    def get_history(self):
        return '\n'.join(map(str, self.history))


class CreditAccount(Account):
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=500):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.negative_limit = negative_limit
        self.__fee_positive = 0.02
        self.__fee_negative = 0.05

    def _check_limit(self, amount):
        return (self.balance + self.negative_limit) >= amount * (1 + self.fee)

    def __repr__(self):
        return '<K>' + super().__repr__()

    def full_info(self):
        return '<K>' + super().full_info()


    @property
    def fee(self):
        if self.balance < 0:
            return self.__fee_negative
        else:
            return self.__fee_positive


acc1 = Account('Иванов И.В.', '12345678', '9998887766')
acc2 = Account('Петров В.И.', '87654321', '9998887765', 200)
print(acc1, acc2, "*" * 40, sep="\n")

acc1.deposit(600)
print(acc1, acc2, "*" * 40, sep="\n")

acc1.withdraw(100)
print(acc1, acc2, "*" * 40, sep="\n")

acc1.transfer(acc2, 300)
print(acc1, acc2, "*" * 40, sep="\n")

print(acc1.full_info(), acc2.full_info(), "*" * 40, sep="\n")

acc3 = Account('Иванов И.И.', '1234567t', '9998887766')
acc4 = Account('Иванов И.И.', '1234', '9998887766')
print("*" * 40)

for i in range(len(acc1.history)):
    print(acc1.history[i])
print("*" * 40)
print(acc1.get_history())
print("*" * 40)
print(acc2.get_history())
print("*" * 40)

print(Account.pasports)
acc5 = Account('Иванов И.В.', '12345678', '9998887766')
print(Account.pasports)
print("*" * 40)

acc1_k = CreditAccount('Сидоров С.С.', '12345666', '9998887761', )
print(acc1_k)
acc1_k.transfer(acc1, 200)
print(acc1_k)
print(acc1_k.full_info())
acc1_k.transfer(acc1, 200)
print(acc1_k)
