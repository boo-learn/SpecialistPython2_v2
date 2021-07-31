from abc import ABC, abstractmethod
import re


class AccountBase(ABC):
    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.name = name
        self.passport8 = passport8
        self.phone_number = phone_number
        self.balance = start_balance

    @abstractmethod
    def transfer(self, target_account, amount, is_record=True):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        pass

    @abstractmethod
    def deposit(self, amount, is_record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        pass

    @abstractmethod
    def withdraw(self, amount, is_record=True, is_fee=True):
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
    OPEN = 'открытие счета'
    CLOSE = 'закрытие счета'
    REOPEN = 'переоткрытие счета'
    DEPOSIT = 'пополнение'
    WITHDRAW = 'снятие'
    TRANSFER = 'перевод клиенту'
    INCOME = 'перевод от клиента'

    def __init__(self, type, amount, fee=0., target=None, sender=None):
        self.type = type
        self.amount = amount
        self.fee = fee
        self.target = target
        self.sender = sender

    def __str__(self):
        if self.type == Operation.OPEN:
            return f'Операция {self.type}. Начальный баланс: {self.amount} руб.'
        if self.type == Operation.CLOSE:
            res_str = f'Операция {self.type}.'
            if self.amount < 0:
                res_str += f' Перед этим осуществлено {Operation.DEPOSIT} на сумму {self.amount} руб.'
            elif self.amount > 0:
                res_str += f' Перед этим осуществлено {Operation.WITHDRAW} на сумму {self.amount} руб.'
            return res_str
        if self.type == Operation.REOPEN:
            return f'Операция {self.type}'
        if self.target is not None:
            target_phone = self.target.phone_number + ' '
        else:
            target_phone = ''
        if self.fee == 0:
            return f'Операция {self.type} {self.target} {target_phone}на сумму {self.amount} руб.'
        return f'Операция {self.type} {self.target} {target_phone}на сумму {self.amount} руб. с комиссией ' \
               f'{self.fee * self.amount:.2f} руб.'


class Account(AccountBase):
    FEE = 0.02

    def __init__(self, name, passport8, phone_number, start_balance=0):
        self.__validate(passport8, phone_number, start_balance)
        AccountBase.__init__(self, name, passport8, phone_number, start_balance)
        op = Operation(Operation.OPEN, start_balance)
        self.history = []
        self.history.append(op)
        self.in_archive = False

    def to_archive(self):
        self._account_check_status()
        balance_for_history = self.balance
        if self.balance != 0:
            self.withdraw(self.balance, is_fee=False)
        op = Operation(Operation.CLOSE, balance_for_history)
        self.history.append(op)
        self.in_archive = True

    @staticmethod
    def _validate_passport(passport):
        pattern = r"\d{4} \d{6}"
        if re.match(pattern, passport):
            return True
        return False

    @staticmethod
    def _validate_phone_number(phone_number):
        pattern = r"[+]7-\d{3}-\d{3}-\d{2}-\d{2}"

        if re.match(pattern, phone_number):
            return True
        return False

    def __validate(self, passport8, phone_number, start_balance):
        if not self._validate_passport(passport8):
            raise ValueError('Паспорт должен быть задан в определённом формате')
        if not self._validate_phone_number(phone_number):
            raise ValueError('Телефон - строка в формате: "+7-9xx-xxx-xx-xx"(с символами "+" и "-")')
        # int(passport8)
        # if len(str(passport8)) != 8:
        #     raise ValueError('Паспорт должен быть задан целым 8-ми значным числом')
        # if phone_number[:2] != '+7':
        #     raise ValueError('Телефон - строка в формате: "+7xxx-xxx-xx-xx"(с символами "+" и "-")')
        if start_balance < 0:
            raise ValueError('Начальная сумма на счету должна быть не меньше 0')
        # tmp = phone_number[2:]
        # tokens = tmp.split('-')
        # if len(tokens[0]) != 3 or len(tokens[1]) != 3 or len(tokens[2]) != 2 or len(tokens[3]) != 2:
        #     raise ValueError('Телефон - строка в формате: "+7xxx-xxx-xx-xx"(с символами "+" и "-")')

    def restore(self):
        self.in_archive = False
        op = Operation(Operation.REOPEN, None)
        self.history.append(op)

    def _account_check_status(self):
        if self.in_archive:
            raise ValueError(f'{self.phone_number}: аккаунт закрыт и отправлен в архив')

    def transfer(self, target_account, amount, is_record=True):
        """
        Перевод денег на счет другого клиента
        :param is_record:
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self._account_check_status()
        target_account._account_check_status()
        self.withdraw(amount, is_record=False)
        target_account.deposit(amount, is_record=False)
        if is_record:
            op = Operation(Operation.TRANSFER, amount, target=target_account, fee=self.FEE)
            self.history.append(op)
            op = Operation(Operation.INCOME, amount, target=self, fee=self.FEE)
            target_account.history.append(op)

    def deposit(self, amount, is_record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self._account_check_status()
        self.balance += amount
        if is_record:
            op = Operation(Operation.DEPOSIT, amount)
            self.history.append(op)

    def _has_money(self, amount, is_fee=True):
        if is_fee:
            return self.balance < amount * (1 + self.FEE)
        return self.balance < amount

    def withdraw(self, amount, is_record=True, is_fee=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        self._account_check_status()
        if self._has_money(amount, is_fee=is_fee):
            raise ValueError("На счету недостаточно средств")
        fee = 0
        fee_record = 0
        if is_fee:
            fee = self.FEE * amount
            fee_record = self.FEE
        self.balance = self.balance - amount - fee
        if is_record:
            op = Operation(Operation.WITHDRAW, amount, fee=fee_record)
            self.history.append(op)

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        self._account_check_status()
        return f"{self.name} баланс: {self.balance:.2f} руб. паспорт: {self.passport8} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        self._account_check_status()
        return f"{self.name} баланс: {self.balance:.2f} руб."

    def show_history(self):
        self._account_check_status()
        h_str = ''
        for op in self.history:
            h_str += str(op) + '\n'
        return h_str[:-1]


class CreditAccount(Account):
    FEE = 0
    NEGATIVE_BALANCE_FEE = 0.05

    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=-1000):
        Account.__init__(self, name, passport8, phone_number, start_balance)
        if negative_limit >= 0:
            raise ValueError('Лимит должен быть отрицательным числом')
        self.__negative_limit = negative_limit

    def __repr__(self):
        self._account_check_status()
        return f"{self.name} K-account баланс: {self.balance:.2f} руб."

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        self._account_check_status()
        return f"{self.name} K-account баланс: {self.balance:.2f} руб. лимит {self.__negative_limit:.2f} руб. " \
               f"паспорт: {self.passport8} т. {self.phone_number}"

    def to_archive(self):
        self._account_check_status()
        balance_for_history = self.balance
        if self.balance < 0:
            # self.deposit(-self.balance)
            raise ValueError('Нельзя убрать счет с отрицательным балансом в архив')
        elif self.balance > 0:
            self.withdraw(self.balance, is_fee=False)
        op = Operation(Operation.CLOSE, balance_for_history)
        self.history.append(op)
        self.is_archived = True

    def _has_money(self, amount, is_fee=True):
        self.FEE = self.NEGATIVE_BALANCE_FEE
        if self.balance > 0:
            self.FEE = Account.FEE
        if is_fee:
            return (self.balance + abs(self.__negative_limit)) < amount * (1 + self.FEE)
        return (self.balance + abs(self.__negative_limit)) < amount
