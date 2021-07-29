# Сюда отправляем готовое решение IBank часть-4
class Account:
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.balance = start_balance
        self.__history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, record=False)
        target_account.deposit(amount, record=False)

        op = Operation(Operation.TRANSFER, amount, target_account)
        self.__history.append(op)

        op = Operation(Operation.INCOME, amount, self)
        target_account.__history.append(op)

    def deposit(self, amount, record=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.balance += amount
        if record:
            op = Operation(Operation.DEPOSIT, amount)
            self.__history.append(op)

    def withdraw(self, amount, record=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.balance < amount:
            raise ValueError("Недостаточно средств на счете")

        self.balance -= amount
        if record:
            op = Operation(Operation.WITHDRAW, amount)
            self.__history.append(op)

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

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        hist_str = ""
        for op in self.__history:
            hist_str += str(op) + "\n"
        return hist_str


# TODO: Создаем класс для кредитного аккаунта, наследуясь от аккаунта
class CreditAccount(Account):
    FEE = 2
    FEE_KREDIT = 5
    def __init__(self, name, passport, phone_number, start_balance=0, negative_limit=0):
        Account.__init__(self, name, passport, phone_number, start_balance=0)
        self.negative_limit=negative_limit

    def __repr__(self):
        return f"<K> {self.name} баланс: {self.balance} руб."

    def withdraw(self, amount):
        if self.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            if self.balance < amount * (1 + CreditAccount.FEE):
                fee = CreditAccount.FEE_KREDIT
            else:
                fee = CreditAccount.FEE
            if self.balance-self.negative_limit >= amount * (1 + fee/100):
                self.balance -= amount * (1 + fee/100)
                op = Operation(-amount, amount * fee/100)
                self.history.append(op)
            else:
                raise ValueError("Недостаточно средств на счете")

    def transfer(self, target_account, amount):
        if self.in_archive or target_account.in_archive:
            raise ValueError("Операция невозможна. Счет закрыт")
        else:
            if self.balance < amount * (1 + CreditAccount.FEE):
                fee = CreditAccount.FEE_KREDIT
            else:
                fee = CreditAccount.FEE
            self.withdraw(amount)
            target_account.deposit(amount)
            self.history.pop()
            target_account.history.pop()
            op=Operation(-amount, amount*fee, self.name)
            self.history.append(op)
            op = Operation(amount, source=self.name)
            target_account.history.append(op)
