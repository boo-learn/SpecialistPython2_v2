class Operation:
    # класс для хранение информации об операциях
    # Пополнение, Снятие, Перевод, Поступление
    DEPOSIT = "Пополнение"
    WITHDRAW = "Снятие"
    TRANSFER = "Перевод"
    RECEIPT = "Поступление"
    def __init__(self, type, amount, target_account=None):
        # Тут добавляем свойства для хранение информации об операции
        self.type = type
        self.amount = amount
        self.target_account = target_account

    def __repr__(self):
        """
        :return: возвращает строковое представление операции
        """
        if self.type == Operation.DEPOSIT:
            return f"{self.type} {self.amount} руб."
        elif self.type == Operation.WITHDRAW:
            return f"{self.type} {self.amount} руб. (комиссия: {self.amount * 0.01 * Account.WITHDRAW_FEE} руб.)"
        elif self.type == Operation.TRANSFER:
            return f"{self.type} {self.amount} руб. (комиссия: {self.amount * 0.01 * Account.WITHDRAW_FEE} руб.) на счет клиента: {self.target_account.name}"
        else:
            return f"{self.type} {self.amount} руб. со счета клиента: {self.target_account.name}"


class Account:
    # TODO: сюда копируем реализацию класса Account из предыдущей задачи
    # TODO: добавляем комиссию
    # TODO: запускаем тесты для проверки
    WITHDRAW_FEE = 2
    def __init__(self, name, passport, phone_number, start_balance=0):
        self.name = name
        self.passport = passport
        self.phone_number = phone_number
        self.__balance = start_balance
        self.__history = []

    def transfer(self, target_account, amount):
        """
        Перевод денег на счет другого клиента
        :param target_account: счет клиента для перевода
        :param amount: сумма перевода
        :return:
        """
        self.withdraw(amount, False)
        target_account.deposit(amount, False)
        op_transfer_to = Operation(Operation.TRANSFER, amount, target_account)
        op_transfer_in = Operation(Operation.RECEIPT, amount, self)
        self.__history.append(op_transfer_to)
        target_account.__history.append(op_transfer_in)

    def deposit(self, amount, to_history=True):
        """
        Внесение суммы на текущий счет
        :param amount: сумма
        """
        self.__balance += amount
        if to_history:
            new_op = Operation(Operation.DEPOSIT, amount)
            self.__history.append(new_op)

    def withdraw(self, amount, to_history=True):
        """
        Снятие суммы с текущего счета
        :param amount: сумма
        """
        if self.__balance < amount + amount * 0.01 * Account.WITHDRAW_FEE:
            raise ValueError("Денег на счету недостаточно!")

        self.__balance -= amount + amount * 0.01 * Account.WITHDRAW_FEE
        if to_history:
            new_op = Operation(Operation.WITHDRAW, amount)
            self.__history.append(new_op)

    @property
    def balance(self):
        return self.__balance

    def full_info(self):
        """
        Полная информация о счете в формате: "Иван баланс: 100 руб. паспорт: 3200 123456 т.+7-900-200-02-03"
        """
        return f"{self.name} баланс: {self.__balance} руб. паспорт: {self.passport} т. {self.phone_number}"

    def __repr__(self):
        """
        :return: Информацию о счете в виде строки в формате "Иван баланс: 100 руб."
        """
        return f"{self.name} баланс: {self.__balance} руб."

    def show_history(self):
        """
        :return: возвращаем историю операций в виде строки, в указанном формате
        """
        operations = ""
        for op in self.__history:
            operations += str(op) + '\n'
        return operations
