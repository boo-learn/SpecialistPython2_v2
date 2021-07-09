# from generators import get_user_data
from abc import ABC, abstractmethod


class AccountBase(ABC):
    used_passports = []

    def __init__(self, name, passport8, phone_number, start_balance=0):
        self._name = name
        self._passport8 = passport8
        self._phone_number = phone_number
        self._balance = start_balance
        self._operation_log = []
        self._withdraw_com_percent = 0.02
        self._in_archive = False
        if passport8 in AccountBase.used_passports:
            raise ValueError("Suggested passport number is already used.")
        else:
            AccountBase.used_passports.append(passport8)

    def to_archive(self):
        if self._balance < 0:
            raise ValueError("нельзя убрать в архив счёт с отрицательным балансом")
        self._balance = 0
        self._in_archive = True

    def in_archive(self):
        return self._in_archive

    def restore(self):
        self._in_archive = False

    def __del__(self):
        if self._passport8 in AccountBase.used_passports:
            AccountBase.used_passports.remove(self._passport8)

    # An example of a virtual getter/setter.
    @property
    @abstractmethod
    def phone(self):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @abstractmethod
    def log_operation(self, s):
        pass

    @abstractmethod
    def get_log(self):
        pass

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
    def comission(self, amount, percent):
        """
        Снятие суммы комиссии от суммы снятия
        :param amount: сумма снятия
        :param percent: процент комиссии от amount
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


class Account(AccountBase):
    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        """
        self.withdraw(amount)
        self.log_operation(f"Transfer to {target_account.phone}")
        target_account.deposit(amount)
        target_account.log_operation(f"Transfered from {self.phone}")

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone_number

    def balance(self):
        return self._balance

    def log_operation(self, s):
        self._operation_log.append(s)

    def get_log(self):
        return self._operation_log

    def deposit(self, amount):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        if amount > 0:
            self._balance += amount
            self.log_operation(f"deposit: {amount}")
        else:
            raise ValueError("Сумма пополнения должна быть положительной.")

    def withdraw(self, amount):
        """
        Снятие суммы с текущего счета, если средств достаточно.
        :param amount: сумма
        """
        comission = amount * self._withdraw_com_percent
        amount_with_com = amount + comission
        balance_left = self._balance - amount_with_com
        if balance_left >= 0:
            self._balance -= amount_with_com
            self.log_operation(f"withdraw: {amount}, comission: {comission}")
        else:
            raise ValueError("Недостаточно средств для снятия.")

    def comission(self, amount, percent):
        """
        Снятие суммы комиссии от суммы снятия
        :param amount: сумма снятия
        :param percent: процент комиссии от amount
        """
        pass

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203"
        """
        return f"{self._name} баланс: {self._balance} руб. паспорт: {self._passport8} т. {self._phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб."
        """
        return f"{self._name} баланс: {self._balance} руб."


class CreditAccount(Account):

    def __init__(self, name, passport8, phone_number, start_balance=0, negative_limit=0):
        super().__init__(name, passport8, phone_number, start_balance)
        self._credit_limit = negative_limit
        self._withdraw_com_percent_credit = 0.05
        pass

    def withdraw(self, amount):
        try:
            super().withdraw(amount)
        except ValueError:
            comission = amount * self._withdraw_com_percent_credit
            amount_with_com = amount + comission
            balance_left = self._balance - amount_with_com
            if self._credit_limit + balance_left >= 0:
                self._balance -= amount_with_com
                self.log_operation(f"withdraw: {amount}, comission: {comission}")
            else:
                raise ValueError("Превышен кредитный лимит.")
            pass

    def full_info(self):
        """
        Полная информация о счете в формате: "Иванов Иван Петрович баланс: 100 руб. паспорт: 12345678 т.89002000203 <К>"
        """
        return f"{self._name} баланс: {self._balance} руб. паспорт: {self._passport8} т. {self._phone_number} <K>"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иванов И.П. баланс: 100 руб. <K>"
        """
        return f"{self._name} баланс: {self._balance} руб. <K>"


def main():
    ac1 = Account("L. Torvalds", 11111111, 9998887766, 998)
    ac2 = Account("R. Stallman", 22222222, 9998887755, 1)
    ac_c = CreditAccount("B. Gates", 33333333, 9998887744, 100, 1000)
    ac1.deposit(1000)
    print(ac1)
    print(ac1.full_info())
    print(ac2)
    print(ac2.full_info())
    print(ac_c)
    print(ac_c.full_info())
    ac2.deposit(1000)
    ac2.transfer(ac1, 2)
    ac_c.withdraw(1000)
    print(ac1)
    print(ac2)
    print(ac1.get_log())
    print(ac2.get_log())
    print(ac_c.get_log())


if __name__ == "__main__":
    main()
