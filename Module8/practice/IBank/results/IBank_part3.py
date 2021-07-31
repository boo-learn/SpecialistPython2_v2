# Сюда отправляем готовое решение IBank часть-3
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


class Operation:
    DEPOSIT = 'пополнение'
    WITHDRAW = 'снятие'
    TRANSFER = 'перевод'
    INCOME = 'поступление'

    def __init__(self, type, amount, fee=0, target=None, sender=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.sender = sender

    def __str__(self):
        if self.target is not None:
            target_name = self.target
            return f'Операция: {self.type}, на сумму: {self.amount}, на счет: {target_name}, коммисия: {self.amount * (self.fee / 100)}'
        elif self.sender is not None:
            sender_name = self.sender
            return f'Операция: {self.type}, на сумму: {self.amount}, от: {sender_name}, коммисия: {self.amount*(self.fee/100)}'
        else:
            return f'Операция: {self.type}, на сумму: {self.amount}, коммисия: {self.amount * (self.fee / 100)}'


class Account(AccountBase):
    FEE = 2

    def __init__(self, name, passport8, phone_number, start_balance=0):
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        self.history = []
        self.in_archive = False
        revision = self.passport8.split(' ')
        if len(revision[0]) != 4 or len(revision[1]) != 6:
            raise ValueError("Incorrect format of the passport number(need: xxxx  xxxxxx)")
          #"+7-xxx-xxx-xx-xx"
        area1 = self.phone_number[3:6]
        area2 = self.phone_number[7:10]
        area3 = self.phone_number[11:13]
        area4 = self.phone_number[-2:]
        if self.phone_number != f'+7-{area1}-{area2}-{area3}-{area4}':
            raise ValueError("Please insert your phone number in format: +7-xxx-xxx-xx-xx")

    def transfer(self, target_account, amount, record=True):
        if self.in_archive == False:
            self.withdraw(amount, record=False)
            target_account.deposit(amount, record=False)
            if record:
                op = Operation(Operation.TRANSFER, amount, target=target_account.name, fee=Account.FEE)
                self.history.append(op)
                op = Operation(Operation.INCOME, amount, sender=self.name, fee=Account.FEE)
                target_account.history.append(op)

    def deposit(self, amount, record=True):
        if self.in_archive == False:
            self.balance += amount
            if record:
                op = Operation(Operation.DEPOSIT, amount)
                self.history.append(op)

    def __enough_money(self, amount):
        return self.balance < amount * (1 + Account.FEE/100)

    def withdraw(self, amount, record=True):
        if self.in_archive == False:
            if self.__enough_money(amount):
                raise ValueError("Isn't enough money")

            self.balance -= amount * (1 + Account.FEE/100)
            if record:
                op = Operation(Operation.WITHDRAW, amount, fee=Account.FEE)
                self.history.append(op)

    def full_info(self):
        return f"{self.name} баланс: {self.balance} руб. паспорт: {self.passport8} т.{self.phone_number}"

    def __repr__(self):
        return f"{self.name} баланс: {self.balance} руб."

    def show_history(self):
        hist_str = ''
        for operation in self.history:
            hist_str += str(operation) + '\n'
        return hist_str

    def to_archive(self):
        if self.balance > 0:
            self.balance = 0
        self.in_archive = True

    def restore(self):
        self.in_archive = False


class CreditAcc(Account):
    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        self.__negative_limit = negative_limit
        self.history = []

    def __repr__(self):
        return f"{self.name} K-account баланс: {self.balance} руб."

    def __enough_money(self, amount):
        if self.balance < 0:
            Account.FEE = 5
        return (self.balance + abs(self.__negative_limit)) < amount * (1 + Account.FEE / 100)

    def withdraw(self, amount, record=True):
        if self.__enough_money(amount):
            raise ValueError("Isn't enough money")

        self.balance -= amount * (1 + Account.FEE / 100)
        if record:
            op = Operation(Operation.WITHDRAW, amount, fee=Account.FEE)
            self.history.append(op)

    def transfer(self, target_account, amount, record=True):
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)
        if record:
            op = Operation(Operation.TRANSFER, amount, fee=Account.FEE)
            self.history.append(op)
            
